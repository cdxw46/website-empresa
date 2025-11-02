#define _GNU_SOURCE
#include <sys/types.h>
#include <sys/ptrace.h>
#include <sys/mman.h>
#include <dlfcn.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <inttypes.h>

void *recorded_maps[256];
size_t recorded_sizes[256];
int recorded_count;
static void *main_struct_ptr;
static FILE *handler_log;
static int handlers_wrapped;

typedef void (*handler_fn)(void *, void *, void *, void *, void *);
static handler_fn orig_handlers[256];

static void log_stack_state(int idx, void *stack_ptr, void *sp_ptr, const char *phase) {
    if (!handler_log) {
        return;
    }
    int sp = *(int *)sp_ptr;
    uint64_t *stack = (uint64_t *)stack_ptr;
    fprintf(handler_log, "%s handler=%d sp=%d\n", phase, idx, sp);
    int limit = sp < 16 ? sp : 16;
    for (int i = 0; i < limit; i++) {
        fprintf(handler_log, "  [%d] = 0x%016" PRIx64 "\n", i, stack[i]);
    }
}

static void call_original(int idx, void *a, void *b, void *c, void *d, void *e) {
    log_stack_state(idx, c, d, "before");
    handler_fn fn = orig_handlers[idx];
    if (fn) {
        fn(a, b, c, d, e);
    }
    log_stack_state(idx, c, d, "after");
}

#define DEFINE_WRAPPER(ID) \
    static void wrapper_##ID(void *a, void *b, void *c, void *d, void *e) { \
        call_original(ID, a, b, c, d, e); \
    }

DEFINE_WRAPPER(0)
DEFINE_WRAPPER(1)
DEFINE_WRAPPER(2)
DEFINE_WRAPPER(3)
DEFINE_WRAPPER(4)
DEFINE_WRAPPER(5)
DEFINE_WRAPPER(7)
DEFINE_WRAPPER(8)
DEFINE_WRAPPER(9)
DEFINE_WRAPPER(10)
DEFINE_WRAPPER(11)
DEFINE_WRAPPER(12)
DEFINE_WRAPPER(13)
DEFINE_WRAPPER(14)
DEFINE_WRAPPER(15)
DEFINE_WRAPPER(17)
DEFINE_WRAPPER(18)
DEFINE_WRAPPER(19)
DEFINE_WRAPPER(20)
DEFINE_WRAPPER(21)
DEFINE_WRAPPER(22)
DEFINE_WRAPPER(23)

static void wrapper_16_custom(void *a, void *b, void *c, void *d, void *e) {
    log_stack_state(16, c, d, "before");
    handler_fn fn = orig_handlers[16];
    if (fn) {
        fn(a, b, c, d, e);
    }
    int sp = *(int *)d;
    if (sp > 0) {
        uint64_t *stack = (uint64_t *)c;
        stack[sp - 1] = 1;
    }
    log_stack_state(16, c, d, "after");
}

static void wrapper_6_custom(void *a, void *b, void *c, void *d, void *e) {
    log_stack_state(6, c, d, "before");
    handler_fn fn = orig_handlers[6];
    if (fn) {
        fn(a, b, c, d, e);
    }
    int sp = *(int *)d;
    if (sp > 0) {
        uint64_t *stack = (uint64_t *)c;
        stack[sp - 1] = 1;
    }
    log_stack_state(6, c, d, "after");
}

static handler_fn wrapper_table[] = {
    wrapper_0, wrapper_1, wrapper_2, wrapper_3,
    wrapper_4, wrapper_5, wrapper_6_custom, wrapper_7,
    wrapper_8, wrapper_9, wrapper_10, wrapper_11,
    wrapper_12, wrapper_13, wrapper_14, wrapper_15,
    wrapper_16_custom, wrapper_17, wrapper_18, wrapper_19,
    wrapper_20, wrapper_21, wrapper_22, wrapper_23
};

long ptrace(enum __ptrace_request request, ...) {
    (void)request;
    errno = 0;
    return 0;
}

void *mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset) {
    static void *(*real_mmap)(void *, size_t, int, int, int, off_t);
    if (!real_mmap) {
        real_mmap = dlsym(RTLD_NEXT, "mmap");
    }
    void *result = real_mmap(addr, length, prot, flags, fd, offset);
    if (result != MAP_FAILED && recorded_count < (int)(sizeof(recorded_maps) / sizeof(recorded_maps[0]))) {
        recorded_maps[recorded_count] = result;
        recorded_sizes[recorded_count] = length;
        recorded_count++;
        fprintf(stderr, "[hook] mmap(%p, %zu, %d, %d, %d, %ld)\n",
                result, length, prot, flags, fd, (long)offset);
    }
    return result;
}

void *malloc(size_t size) {
    static void *(*real_malloc)(size_t);
    if (!real_malloc) {
        real_malloc = dlsym(RTLD_NEXT, "malloc");
    }
    void *result = real_malloc(size);
    if (result && size == 0xe0) {
        main_struct_ptr = result;
        fprintf(stderr, "[hook] main struct allocated at %p\n", result);
    }
    return result;
}

ssize_t getline(char **lineptr, size_t *n, FILE *stream) {
    static ssize_t (*real_getline)(char **, size_t *, FILE *);
    if (!real_getline) {
        real_getline = dlsym(RTLD_NEXT, "getline");
    }
    const char *forced = getenv("OVERRIDE_INPUT");
    if (!forced) {
        return real_getline(lineptr, n, stream);
    }
    size_t forced_len = strlen(forced);
    size_t required = forced_len + 2; /* include \n and null */
    if (!lineptr) {
        errno = EINVAL;
        return -1;
    }
    if (*lineptr == NULL || *n < required) {
        char *newptr = realloc(*lineptr, required);
        if (!newptr) {
            return -1;
        }
        *lineptr = newptr;
        *n = required;
    }
    memcpy(*lineptr, forced, forced_len);
    (*lineptr)[forced_len] = '\n';
    (*lineptr)[forced_len + 1] = '\0';
    static int dumped = 0;
    if (main_struct_ptr && !dumped) {
        dumped = 1;
        FILE *dump = fopen("/workspace/htb_aswqx4d/struct_dump.bin", "wb");
        if (dump) {
            fwrite(main_struct_ptr, 1, 0xe0, dump);
            fclose(dump);
        }
        uint64_t ptrs[28];
        memcpy(ptrs, main_struct_ptr, sizeof(ptrs));
        uint64_t lo = UINT64_MAX;
        uint64_t hi = 0;
        int map_index[28];
        for (size_t i = 0; i < 28; i++) {
            uint64_t val = ptrs[i];
            int idx = -1;
            for (int j = 0; j < recorded_count; j++) {
                if ((uint64_t)recorded_maps[j] == val) {
                    idx = j;
                    break;
                }
            }
            map_index[i] = idx;
            if (idx == -1 && val) {
                if (val < lo) lo = val;
                if (val > hi) hi = val;
            }
        }
        if (lo != UINT64_MAX && hi >= lo) {
            size_t span = (size_t)(hi - lo + 0x200);
            void *base = (void *)(uintptr_t)lo;
            FILE *rdump = fopen("/workspace/htb_aswqx4d/heap_region.bin", "wb");
            if (rdump) {
                fwrite(base, 1, span, rdump);
                fclose(rdump);
            }
        }
        if (!handlers_wrapped) {
            handlers_wrapped = 1;
            if (!handler_log) {
                handler_log = fopen("/workspace/htb_aswqx4d/handler_log.txt", "w");
            }
            for (size_t i = 0; i < 28; i++) {
                int idx = map_index[i];
                if (idx < 0 || idx >= (int)(sizeof(wrapper_table) / sizeof(wrapper_table[0]))) {
                    continue;
                }
                if (idx == 5) { /* skip dispatcher */
                    continue;
                }
                orig_handlers[idx] = (handler_fn)ptrs[i];
                ((handler_fn *)main_struct_ptr)[i] = wrapper_table[idx];
            }
        }
    }
    return (ssize_t)(forced_len + 1);
}
