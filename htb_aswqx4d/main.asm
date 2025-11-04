            ; CALL XREF from section..text @ +0x11
┌ 3372: fcn.00001530 ();
│           ; var int64_t var_51h @ rbp-0x51
│           ; var int64_t var_50h @ rbp-0x50
│           ; var int64_t var_40h @ rbp-0x40
│           ; var int64_t var_38h @ rbp-0x38
│           ; var int64_t var_2eh @ rbp-0x2e
│           ; var int64_t var_2ah @ rbp-0x2a
│           ; var int64_t var_28h @ rbp-0x28
│           ; var int64_t var_ff8h @ rsp+0xff8
│           ; var int64_t var_ff8h_2 @ rsp+0x1028
│           ; var int64_t var_ff8h_3 @ rsp+0x1068
│           ; var int64_t var_ff8h_4 @ rsp+0x1098
│           ; var int64_t var_18h_2 @ rsp+0x10b8
│           ; var int64_t var_ff8h_5 @ rsp+0x10e8
│           ; var int64_t var_ff8h_6 @ rsp+0x1128
│           ; var int64_t var_ff8h_7 @ rsp+0x1168
│           ; var int64_t var_ff8h_8 @ rsp+0x1198
│           ; var int64_t var_b8h @ rsp+0x1258
│           ; var int64_t var_sp_38h @ rsp+0x1298
│           ; var int64_t var_sp_28h @ rsp+0x12c8
│           ; var int64_t var_18h @ rsp+0x12e8
│           0x00001530      f30f1efa       endbr64
│           0x00001534      55             push rbp
│           0x00001535      bfe0000000     mov edi, 0xe0               ; size_t size
│           0x0000153a      4889e5         mov rbp, rsp
│           0x0000153d      4156           push r14
│           0x0000153f      4155           push r13
│           0x00001541      4154           push r12
│           0x00001543      53             push rbx
│           0x00001544      4883ec30       sub rsp, 0x30
│           0x00001548      64488b042528.  mov rax, qword fs:[0x28]
│           0x00001551      488945d8       mov qword [var_28h], rax
│           0x00001555      31c0           xor eax, eax
│           0x00001557      4889e3         mov rbx, rsp
│           0x0000155a      e8d1fbffff     call sym.imp.malloc         ;  void *malloc(size_t size)
│           0x0000155f      4889057a5f00.  mov qword [0x000074e0], rax ; [0x74e0:8]=0
│           0x00001566      4989c5         mov r13, rax
│           0x00001569      4839dc         cmp rsp, rbx
│       ┌─< 0x0000156c      7415           je 0x1583
│       │   ; CODE XREF from fcn.00001530 @ 0x1581
│      ┌──> 0x0000156e      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x00001575      48838c24f80f.  or qword [var_18h], 0
│      ╎│   0x0000157e      4839dc         cmp rsp, rbx
│      └──< 0x00001581      75eb           jne 0x156e
│       │   ; CODE XREF from fcn.00001530 @ 0x156c
│       └─> 0x00001583      4883ec20       sub rsp, 0x20
│           0x00001587      48834c241800   or qword [var_18h], 0
│           0x0000158d      b84d2a0000     mov eax, 0x2a4d             ; 'M*'
│           0x00001592      b901000000     mov ecx, 1
│           0x00001597      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x0000159c      488d359c3d00.  lea rsi, [0x0000533f]
│           0x000015a3      668945d6       mov word [var_2ah], ax
│           0x000015a7      4989e4         mov r12, rsp
│           0x000015aa      b82a000000     mov eax, 0x2a               ; '*'
│           0x000015af      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│       ┌─< 0x000015b6      eb20           jmp 0x15d8
..
│       │   ; CODE XREF from fcn.00001530 @ 0x15ea
│      ┌──> 0x000015c0      89c2           mov edx, eax
│      ╎│   0x000015c2      480fafd7       imul rdx, rdi
│      ╎│   0x000015c6      48c1ea22       shr rdx, 0x22
│      ╎│   0x000015ca      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x000015cd      01d2           add edx, edx
│      ╎│   0x000015cf      29d0           sub eax, edx
│      ╎│   0x000015d1      4898           cdqe
│      ╎│   0x000015d3      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x15b6
│      ╎└─> 0x000015d8      32040e         xor al, byte [rsi + rcx]
│      ╎    0x000015db      4188440cff     mov byte [r12 + rcx - 1], al
│      ╎    0x000015e0      89c8           mov eax, ecx
│      ╎    0x000015e2      4883c101       add rcx, 1
│      ╎    0x000015e6      4883f91c       cmp rcx, 0x1c
│      └──< 0x000015ea      75d4           jne 0x15c0
│           0x000015ec      ba07000000     mov edx, 7                  ; int prot
│           0x000015f1      4531c9         xor r9d, r9d                ; size_t offset
│           0x000015f4      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x000015fa      31ff           xor edi, edi                ; void*addr
│           0x000015fc      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00001601      be1b000000     mov esi, 0x1b               ; size_t length
│           0x00001606      e805fbffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x0000160b      498b542410     mov rdx, qword [r12 + 0x10]
│           0x00001610      f3410f6f0424   movdqu xmm0, xmmword [r12]
│           0x00001616      48895010       mov qword [rax + 0x10], rdx
│           0x0000161a      410fb7542418   movzx edx, word [r12 + 0x18]
│           0x00001620      0f1100         movups xmmword [rax], xmm0
│           0x00001623      66895018       mov word [rax + 0x18], dx
│           0x00001627      410fb654241a   movzx edx, byte [r12 + 0x1a]
│           0x0000162d      88501a         mov byte [rax + 0x1a], dl
│           0x00001630      4889dc         mov rsp, rbx
│           0x00001633      498985a80000.  mov qword [r13 + 0xa8], rax
│           0x0000163a      4c8b2d9f5e00.  mov r13, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00001641      4839dc         cmp rsp, rbx
│       ┌─< 0x00001644      7415           je 0x165b
│       │   ; CODE XREF from fcn.00001530 @ 0x1659
│      ┌──> 0x00001646      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x0000164d      48838c24f80f.  or qword [var_sp_28h], 0
│      ╎│   0x00001656      4839dc         cmp rsp, rbx
│      └──< 0x00001659      75eb           jne 0x1646
│       │   ; CODE XREF from fcn.00001530 @ 0x1644
│       └─> 0x0000165b      4883ec30       sub rsp, 0x30
│           0x0000165f      48834c242800   or qword [var_sp_28h], 0
│           0x00001665      b901000000     mov ecx, 1
│           0x0000166a      b82a000000     mov eax, 0x2a               ; '*'
│           0x0000166f      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x00001674      41be4d2a0000   mov r14d, 0x2a4d            ; 'M*'
│           0x0000167a      488d355e3a00.  lea rsi, [0x000050df]
│           0x00001681      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│           0x00001688      4989e4         mov r12, rsp
│           0x0000168b      66448975d6     mov word [var_2ah], r14w
│       ┌─< 0x00001690      eb1e           jmp 0x16b0
..
│       │   ; CODE XREF from fcn.00001530 @ 0x16c2
│      ┌──> 0x00001698      89c2           mov edx, eax
│      ╎│   0x0000169a      480fafd7       imul rdx, rdi
│      ╎│   0x0000169e      48c1ea22       shr rdx, 0x22
│      ╎│   0x000016a2      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x000016a5      01d2           add edx, edx
│      ╎│   0x000016a7      29d0           sub eax, edx
│      ╎│   0x000016a9      4898           cdqe
│      ╎│   0x000016ab      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x1690
│      ╎└─> 0x000016b0      32040e         xor al, byte [rsi + rcx]
│      ╎    0x000016b3      4188440cff     mov byte [r12 + rcx - 1], al
│      ╎    0x000016b8      89c8           mov eax, ecx
│      ╎    0x000016ba      4883c101       add rcx, 1
│      ╎    0x000016be      4883f92b       cmp rcx, 0x2b
│      └──< 0x000016c2      75d4           jne 0x1698
│           0x000016c4      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x000016c9      ba07000000     mov edx, 7                  ; int prot
│           0x000016ce      31ff           xor edi, edi                ; void*addr
│           0x000016d0      4531c9         xor r9d, r9d                ; size_t offset
│           0x000016d3      be2a000000     mov esi, 0x2a               ; '*' ; size_t length
│           0x000016d8      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x000016de      e82dfaffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x000016e3      498b542420     mov rdx, qword [r12 + 0x20]
│           0x000016e8      b901000000     mov ecx, 1
│           0x000016ed      f3410f6f0c24   movdqu xmm1, xmmword [r12]
│           0x000016f3      f3410f6f5424.  movdqu xmm2, xmmword [r12 + 0x10]
│           0x000016fa      41bb4d2a0000   mov r11d, 0x2a4d            ; 'M*'
│           0x00001700      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x00001705      488d35b33d00.  lea rsi, [0x000054bf]
│           0x0000170c      48895020       mov qword [rax + 0x20], rdx
│           0x00001710      410fb7542428   movzx edx, word [r12 + 0x28]
│           0x00001716      4c8d65af       lea r12, [var_51h]
│           0x0000171a      0f1108         movups xmmword [rax], xmm1
│           0x0000171d      66895028       mov word [rax + 0x28], dx
│           0x00001721      0f115010       movups xmmword [rax + 0x10], xmm2
│           0x00001725      4889dc         mov rsp, rbx
│           0x00001728      498985900000.  mov qword [r13 + 0x90], rax
│           0x0000172f      4c8b2daa5d00.  mov r13, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00001736      b82a000000     mov eax, 0x2a               ; '*'
│           0x0000173b      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│           0x00001742      6644895dd6     mov word [var_2ah], r11w
│       ┌─< 0x00001747      eb1f           jmp 0x1768
..
│       │   ; CODE XREF from fcn.00001530 @ 0x1779
│      ┌──> 0x00001750      89c2           mov edx, eax
│      ╎│   0x00001752      480fafd7       imul rdx, rdi
│      ╎│   0x00001756      48c1ea22       shr rdx, 0x22
│      ╎│   0x0000175a      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x0000175d      01d2           add edx, edx
│      ╎│   0x0000175f      29d0           sub eax, edx
│      ╎│   0x00001761      4898           cdqe
│      ╎│   0x00001763      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x1747
│      ╎└─> 0x00001768      32040e         xor al, byte [rsi + rcx]
│      ╎    0x0000176b      4188040c       mov byte [r12 + rcx], al
│      ╎    0x0000176f      89c8           mov eax, ecx
│      ╎    0x00001771      4883c101       add rcx, 1
│      ╎    0x00001775      4883f91a       cmp rcx, 0x1a
│      └──< 0x00001779      75d5           jne 0x1750
│           0x0000177b      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00001780      ba07000000     mov edx, 7                  ; int prot
│           0x00001785      31ff           xor edi, edi                ; void*addr
│           0x00001787      4531c9         xor r9d, r9d                ; size_t offset
│           0x0000178a      be19000000     mov esi, 0x19               ; size_t length
│           0x0000178f      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x00001795      e876f9ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x0000179a      488b55c0       mov rdx, qword [var_40h]
│           0x0000179e      f30f6f5db0     movdqu xmm3, xmmword [var_50h]
│           0x000017a3      41ba4d2a0000   mov r10d, 0x2a4d            ; 'M*'
│           0x000017a9      b901000000     mov ecx, 1
│           0x000017ae      488d35aa3a00.  lea rsi, [0x0000525f]
│           0x000017b5      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x000017ba      48895010       mov qword [rax + 0x10], rdx
│           0x000017be      0fb655c8       movzx edx, byte [var_38h]
│           0x000017c2      0f1118         movups xmmword [rax], xmm3
│           0x000017c5      885018         mov byte [rax + 0x18], dl
│           0x000017c8      4889dc         mov rsp, rbx
│           0x000017cb      498985c00000.  mov qword [r13 + 0xc0], rax
│           0x000017d2      4c8b2d075d00.  mov r13, qword [0x000074e0] ; [0x74e0:8]=0
│           0x000017d9      b82a000000     mov eax, 0x2a               ; '*'
│           0x000017de      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│           0x000017e5      66448955d6     mov word [var_2ah], r10w
│       ┌─< 0x000017ea      eb1c           jmp 0x1808
..
│       │   ; CODE XREF from fcn.00001530 @ 0x1819
│      ┌──> 0x000017f0      89c2           mov edx, eax
│      ╎│   0x000017f2      480fafd7       imul rdx, rdi
│      ╎│   0x000017f6      48c1ea22       shr rdx, 0x22
│      ╎│   0x000017fa      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x000017fd      01d2           add edx, edx
│      ╎│   0x000017ff      29d0           sub eax, edx
│      ╎│   0x00001801      4898           cdqe
│      ╎│   0x00001803      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x17ea
│      ╎└─> 0x00001808      32040e         xor al, byte [rsi + rcx]
│      ╎    0x0000180b      4188040c       mov byte [r12 + rcx], al
│      ╎    0x0000180f      89c8           mov eax, ecx
│      ╎    0x00001811      4883c101       add rcx, 1
│      ╎    0x00001815      4883f913       cmp rcx, 0x13
│      └──< 0x00001819      75d5           jne 0x17f0
│           0x0000181b      ba07000000     mov edx, 7                  ; int prot
│           0x00001820      4531c9         xor r9d, r9d                ; size_t offset
│           0x00001823      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x00001829      31ff           xor edi, edi                ; void*addr
│           0x0000182b      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00001830      be12000000     mov esi, 0x12               ; size_t length
│           0x00001835      e8d6f8ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x0000183a      f30f6f65b0     movdqu xmm4, xmmword [var_50h]
│           0x0000183f      0fb755c0       movzx edx, word [var_40h]
│           0x00001843      0f1120         movups xmmword [rax], xmm4
│           0x00001846      66895010       mov word [rax + 0x10], dx
│           0x0000184a      4889dc         mov rsp, rbx
│           0x0000184d      4c8b358c5c00.  mov r14, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00001854      49894558       mov qword [r13 + 0x58], rax
│           0x00001858      4839dc         cmp rsp, rbx
│       ┌─< 0x0000185b      7415           je 0x1872
│       │   ; CODE XREF from fcn.00001530 @ 0x1870
│      ┌──> 0x0000185d      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x00001864      48838c24f80f.  or qword [var_sp_38h], 0
│      ╎│   0x0000186d      4839dc         cmp rsp, rbx
│      └──< 0x00001870      75eb           jne 0x185d
│       │   ; CODE XREF from fcn.00001530 @ 0x185b
│       └─> 0x00001872      4883ec40       sub rsp, 0x40
│           0x00001876      48834c243800   or qword [var_sp_38h], 0
│           0x0000187c      b901000000     mov ecx, 1
│           0x00001881      b82a000000     mov eax, 0x2a               ; '*'
│           0x00001886      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x0000188b      41b94d2a0000   mov r9d, 0x2a4d             ; 'M*'
│           0x00001891      488d35673a00.  lea rsi, [0x000052ff]
│           0x00001898      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│           0x0000189f      4989e5         mov r13, rsp
│           0x000018a2      6644894dd6     mov word [var_2ah], r9w
│       ┌─< 0x000018a7      eb1f           jmp 0x18c8
..
│       │   ; CODE XREF from fcn.00001530 @ 0x18da
│      ┌──> 0x000018b0      89c2           mov edx, eax
│      ╎│   0x000018b2      480fafd7       imul rdx, rdi
│      ╎│   0x000018b6      48c1ea22       shr rdx, 0x22
│      ╎│   0x000018ba      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x000018bd      01d2           add edx, edx
│      ╎│   0x000018bf      29d0           sub eax, edx
│      ╎│   0x000018c1      4898           cdqe
│      ╎│   0x000018c3      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x18a7
│      ╎└─> 0x000018c8      32040e         xor al, byte [rsi + rcx]
│      ╎    0x000018cb      4188440dff     mov byte [r13 + rcx - 1], al
│      ╎    0x000018d0      89c8           mov eax, ecx
│      ╎    0x000018d2      4883c101       add rcx, 1
│      ╎    0x000018d6      4883f939       cmp rcx, 0x39
│      └──< 0x000018da      75d4           jne 0x18b0
│           0x000018dc      ba07000000     mov edx, 7                  ; int prot
│           0x000018e1      4531c9         xor r9d, r9d                ; size_t offset
│           0x000018e4      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x000018ea      31ff           xor edi, edi                ; void*addr
│           0x000018ec      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x000018f1      be38000000     mov esi, 0x38               ; '8' ; size_t length
│           0x000018f6      e815f8ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x000018fb      f3410f6f6d00   movdqu xmm5, xmmword [r13]
│           0x00001901      f3410f6f7510   movdqu xmm6, xmmword [r13 + 0x10]
│           0x00001907      f3410f6f7d20   movdqu xmm7, xmmword [r13 + 0x20]
│           0x0000190d      498b5530       mov rdx, qword [r13 + 0x30]
│           0x00001911      0f1128         movups xmmword [rax], xmm5
│           0x00001914      48895030       mov qword [rax + 0x30], rdx
│           0x00001918      0f117010       movups xmmword [rax + 0x10], xmm6
│           0x0000191c      0f117820       movups xmmword [rax + 0x20], xmm7
│           0x00001920      4889dc         mov rsp, rbx
│           0x00001923      49894648       mov qword [r14 + 0x48], rax
│           0x00001927      4c8b35b25b00.  mov r14, qword [0x000074e0] ; [0x74e0:8]=0
│           0x0000192e      4839dc         cmp rsp, rbx
│       ┌─< 0x00001931      7415           je 0x1948
│       │   ; CODE XREF from fcn.00001530 @ 0x1946
│      ┌──> 0x00001933      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x0000193a      48838c24f80f.  or qword [var_b8h], 0
│      ╎│   0x00001943      4839dc         cmp rsp, rbx
│      └──< 0x00001946      75eb           jne 0x1933
│       │   ; CODE XREF from fcn.00001530 @ 0x1931
│       └─> 0x00001948      4881ecc00000.  sub rsp, 0xc0
│           0x0000194f      48838c24b800.  or qword [var_b8h], 0
│           0x00001958      b901000000     mov ecx, 1
│           0x0000195d      b82a000000     mov eax, 0x2a               ; '*'
│           0x00001962      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x00001967      41b84d2a0000   mov r8d, 0x2a4d             ; 'M*'
│           0x0000196d      488d35ab3600.  lea rsi, [0x0000501f]
│           0x00001974      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│           0x0000197b      4989e5         mov r13, rsp
│           0x0000197e      66448945d6     mov word [var_2ah], r8w
│       ┌─< 0x00001983      eb1b           jmp 0x19a0
..
│       │   ; CODE XREF from fcn.00001530 @ 0x19b5
│      ┌──> 0x00001988      89c2           mov edx, eax
│      ╎│   0x0000198a      480fafd7       imul rdx, rdi
│      ╎│   0x0000198e      48c1ea22       shr rdx, 0x22
│      ╎│   0x00001992      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x00001995      01d2           add edx, edx
│      ╎│   0x00001997      29d0           sub eax, edx
│      ╎│   0x00001999      4898           cdqe
│      ╎│   0x0000199b      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x1983
│      ╎└─> 0x000019a0      32040e         xor al, byte [rsi + rcx]
│      ╎    0x000019a3      4188440dff     mov byte [r13 + rcx - 1], al
│      ╎    0x000019a8      89c8           mov eax, ecx
│      ╎    0x000019aa      4883c101       add rcx, 1
│      ╎    0x000019ae      4881f9b40000.  cmp rcx, 0xb4
│      └──< 0x000019b5      75d1           jne 0x1988
│           0x000019b7      ba07000000     mov edx, 7                  ; int prot
│           0x000019bc      4531c9         xor r9d, r9d                ; size_t offset
│           0x000019bf      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x000019c5      31ff           xor edi, edi                ; void*addr
│           0x000019c7      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x000019cc      beb3000000     mov esi, 0xb3               ; size_t length
│           0x000019d1      e83af7ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x000019d6      f3410f6f4500   movdqu xmm0, xmmword [r13]
│           0x000019dc      f3410f6f4d10   movdqu xmm1, xmmword [r13 + 0x10]
│           0x000019e2      f3410f6f5520   movdqu xmm2, xmmword [r13 + 0x20]
│           0x000019e8      410fb795b000.  movzx edx, word [r13 + 0xb0]
│           0x000019f0      0f1100         movups xmmword [rax], xmm0
│           0x000019f3      f3410f6f5d30   movdqu xmm3, xmmword [r13 + 0x30]
│           0x000019f9      f3410f6f6540   movdqu xmm4, xmmword [r13 + 0x40]
│           0x000019ff      0f114810       movups xmmword [rax + 0x10], xmm1
│           0x00001a03      f3410f6f6d50   movdqu xmm5, xmmword [r13 + 0x50]
│           0x00001a09      f3410f6f7560   movdqu xmm6, xmmword [r13 + 0x60]
│           0x00001a0f      668990b00000.  mov word [rax + 0xb0], dx
│           0x00001a16      f3410f6f7d70   movdqu xmm7, xmmword [r13 + 0x70]
│           0x00001a1c      0f115020       movups xmmword [rax + 0x20], xmm2
│           0x00001a20      410fb695b200.  movzx edx, byte [r13 + 0xb2]
│           0x00001a28      f3410f6f8580.  movdqu xmm0, xmmword [r13 + 0x80]
│           0x00001a31      f3410f6f8d90.  movdqu xmm1, xmmword [r13 + 0x90]
│           0x00001a3a      0f115830       movups xmmword [rax + 0x30], xmm3
│           0x00001a3e      f3410f6f95a0.  movdqu xmm2, xmmword [r13 + 0xa0]
│           0x00001a47      8890b2000000   mov byte [rax + 0xb2], dl
│           0x00001a4d      0f116040       movups xmmword [rax + 0x40], xmm4
│           0x00001a51      0f116850       movups xmmword [rax + 0x50], xmm5
│           0x00001a55      0f117060       movups xmmword [rax + 0x60], xmm6
│           0x00001a59      0f117870       movups xmmword [rax + 0x70], xmm7
│           0x00001a5d      0f1180800000.  movups xmmword [rax + 0x80], xmm0
│           0x00001a64      0f1188900000.  movups xmmword [rax + 0x90], xmm1
│           0x00001a6b      0f1190a00000.  movups xmmword [rax + 0xa0], xmm2
│           0x00001a72      4889dc         mov rsp, rbx
│           0x00001a75      498986880000.  mov qword [r14 + 0x88], rax
│           0x00001a7c      4c8b355d5a00.  mov r14, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00001a83      4839dc         cmp rsp, rbx
│       ┌─< 0x00001a86      7415           je 0x1a9d
│       │   ; CODE XREF from fcn.00001530 @ 0x1a9b
│      ┌──> 0x00001a88      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x00001a8f      48838c24f80f.  or qword [var_ff8h_8], 0
│      ╎│   0x00001a98      4839dc         cmp rsp, rbx
│      └──< 0x00001a9b      75eb           jne 0x1a88
│       │   ; CODE XREF from fcn.00001530 @ 0x1a86
│       └─> 0x00001a9d      4883ec30       sub rsp, 0x30
│           0x00001aa1      48834c242800   or qword [rsp + 0x28], 0
│           0x00001aa7      bf4d2a0000     mov edi, 0x2a4d             ; 'M*'
│           0x00001aac      b901000000     mov ecx, 1
│           0x00001ab1      b82a000000     mov eax, 0x2a               ; '*'
│           0x00001ab6      488d35c23700.  lea rsi, [0x0000527f]
│           0x00001abd      66897dd6       mov word [var_2ah], di
│           0x00001ac1      4989e5         mov r13, rsp
│           0x00001ac4      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x00001ac9      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│       ┌─< 0x00001ad0      eb1e           jmp 0x1af0
..
│       │   ; CODE XREF from fcn.00001530 @ 0x1b02
│      ┌──> 0x00001ad8      89c2           mov edx, eax
│      ╎│   0x00001ada      480fafd7       imul rdx, rdi
│      ╎│   0x00001ade      48c1ea22       shr rdx, 0x22
│      ╎│   0x00001ae2      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x00001ae5      01d2           add edx, edx
│      ╎│   0x00001ae7      29d0           sub eax, edx
│      ╎│   0x00001ae9      4898           cdqe
│      ╎│   0x00001aeb      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x1ad0
│      ╎└─> 0x00001af0      32040e         xor al, byte [rsi + rcx]
│      ╎    0x00001af3      4188440dff     mov byte [r13 + rcx - 1], al
│      ╎    0x00001af8      89c8           mov eax, ecx
│      ╎    0x00001afa      4883c101       add rcx, 1
│      ╎    0x00001afe      4883f926       cmp rcx, 0x26
│      └──< 0x00001b02      75d4           jne 0x1ad8
│           0x00001b04      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00001b09      ba07000000     mov edx, 7                  ; int prot
│           0x00001b0e      31ff           xor edi, edi                ; void*addr
│           0x00001b10      4531c9         xor r9d, r9d                ; size_t offset
│           0x00001b13      be25000000     mov esi, 0x25               ; '%' ; size_t length
│           0x00001b18      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x00001b1e      e8edf5ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x00001b23      418b5520       mov edx, dword [r13 + 0x20]
│           0x00001b27      f3410f6f5d00   movdqu xmm3, xmmword [r13]
│           0x00001b2d      be4d2a0000     mov esi, 0x2a4d             ; 'M*'
│           0x00001b32      f3410f6f6510   movdqu xmm4, xmmword [r13 + 0x10]
│           0x00001b38      b901000000     mov ecx, 1
│           0x00001b3d      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x00001b42      895020         mov dword [rax + 0x20], edx
│           0x00001b45      410fb65524     movzx edx, byte [r13 + 0x24]
│           0x00001b4a      0f1118         movups xmmword [rax], xmm3
│           0x00001b4d      885024         mov byte [rax + 0x24], dl
│           0x00001b50      0f116010       movups xmmword [rax + 0x10], xmm4
│           0x00001b54      4889dc         mov rsp, rbx
│           0x00001b57      4c8b2d825900.  mov r13, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00001b5e      498986a00000.  mov qword [r14 + 0xa0], rax
│           0x00001b65      b82a000000     mov eax, 0x2a               ; '*'
│           0x00001b6a      668975d6       mov word [var_2ah], si
│           0x00001b6e      488d358a3900.  lea rsi, [0x000054ff]
│           0x00001b75      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│       ┌─< 0x00001b7c      eb1a           jmp 0x1b98
..
│       │   ; CODE XREF from fcn.00001530 @ 0x1ba9
│      ┌──> 0x00001b80      89c2           mov edx, eax
│      ╎│   0x00001b82      480fafd7       imul rdx, rdi
│      ╎│   0x00001b86      48c1ea22       shr rdx, 0x22
│      ╎│   0x00001b8a      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x00001b8d      01d2           add edx, edx
│      ╎│   0x00001b8f      29d0           sub eax, edx
│      ╎│   0x00001b91      4898           cdqe
│      ╎│   0x00001b93      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x1b7c
│      ╎└─> 0x00001b98      32040e         xor al, byte [rsi + rcx]
│      ╎    0x00001b9b      4188040c       mov byte [r12 + rcx], al
│      ╎    0x00001b9f      89c8           mov eax, ecx
│      ╎    0x00001ba1      4883c101       add rcx, 1
│      ╎    0x00001ba5      4883f915       cmp rcx, 0x15
│      └──< 0x00001ba9      75d5           jne 0x1b80
│           0x00001bab      ba07000000     mov edx, 7                  ; int prot
│           0x00001bb0      4531c9         xor r9d, r9d                ; size_t offset
│           0x00001bb3      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x00001bb9      31ff           xor edi, edi                ; void*addr
│           0x00001bbb      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00001bc0      be14000000     mov esi, 0x14               ; size_t length
│           0x00001bc5      e846f5ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x00001bca      f30f6f6db0     movdqu xmm5, xmmword [var_50h]
│           0x00001bcf      8b55c0         mov edx, dword [var_40h]
│           0x00001bd2      0f1128         movups xmmword [rax], xmm5
│           0x00001bd5      895010         mov dword [rax + 0x10], edx
│           0x00001bd8      4889dc         mov rsp, rbx
│           0x00001bdb      4c8b35fe5800.  mov r14, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00001be2      49894570       mov qword [r13 + 0x70], rax
│           0x00001be6      4839dc         cmp rsp, rbx
│       ┌─< 0x00001be9      7415           je 0x1c00
│       │   ; CODE XREF from fcn.00001530 @ 0x1bfe
│      ┌──> 0x00001beb      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x00001bf2      48838c24f80f.  or qword [var_ff8h_7], 0
│      ╎│   0x00001bfb      4839dc         cmp rsp, rbx
│      └──< 0x00001bfe      75eb           jne 0x1beb
│       │   ; CODE XREF from fcn.00001530 @ 0x1be9
│       └─> 0x00001c00      4883ec40       sub rsp, 0x40
│           0x00001c04      48834c243800   or qword [rsp + 0x38], 0
│           0x00001c0a      b94d2a0000     mov ecx, 0x2a4d             ; 'M*'
│           0x00001c0f      b82a000000     mov eax, 0x2a               ; '*'
│           0x00001c14      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x00001c19      488d35ff3400.  lea rsi, [0x0000511f]
│           0x00001c20      66894dd6       mov word [var_2ah], cx
│           0x00001c24      4989e5         mov r13, rsp
│           0x00001c27      b901000000     mov ecx, 1
│           0x00001c2c      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│       ┌─< 0x00001c33      eb1b           jmp 0x1c50
..
│       │   ; CODE XREF from fcn.00001530 @ 0x1c62
│      ┌──> 0x00001c38      89c2           mov edx, eax
│      ╎│   0x00001c3a      480fafd7       imul rdx, rdi
│      ╎│   0x00001c3e      48c1ea22       shr rdx, 0x22
│      ╎│   0x00001c42      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x00001c45      01d2           add edx, edx
│      ╎│   0x00001c47      29d0           sub eax, edx
│      ╎│   0x00001c49      4898           cdqe
│      ╎│   0x00001c4b      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x1c33
│      ╎└─> 0x00001c50      32040e         xor al, byte [rsi + rcx]
│      ╎    0x00001c53      4188440dff     mov byte [r13 + rcx - 1], al
│      ╎    ; DATA XREF from entry.init0 @ +0x115
│      ╎    0x00001c58      89c8           mov eax, ecx
│      ╎    0x00001c5a      4883c101       add rcx, 1
│      ╎    0x00001c5e      4883f93c       cmp rcx, 0x3c
│      └──< 0x00001c62      75d4           jne 0x1c38
│           0x00001c64      ba07000000     mov edx, 7                  ; int prot
│           0x00001c69      4531c9         xor r9d, r9d                ; size_t offset
│           0x00001c6c      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x00001c72      31ff           xor edi, edi                ; void*addr
│           0x00001c74      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00001c79      be3b000000     mov esi, 0x3b               ; ';' ; size_t length
│           0x00001c7e      e88df4ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x00001c83      498b5530       mov rdx, qword [r13 + 0x30]
│           0x00001c87      f3410f6f7500   movdqu xmm6, xmmword [r13]
│           0x00001c8d      f3410f6f7d10   movdqu xmm7, xmmword [r13 + 0x10]
│           0x00001c93      f3410f6f4520   movdqu xmm0, xmmword [r13 + 0x20]
│           0x00001c99      48895030       mov qword [rax + 0x30], rdx
│           0x00001c9d      410fb75538     movzx edx, word [r13 + 0x38]
│           0x00001ca2      0f1130         movups xmmword [rax], xmm6
│           0x00001ca5      66895038       mov word [rax + 0x38], dx
│           0x00001ca9      410fb6553a     movzx edx, byte [r13 + 0x3a]
│           0x00001cae      0f117810       movups xmmword [rax + 0x10], xmm7
│           0x00001cb2      88503a         mov byte [rax + 0x3a], dl
│           0x00001cb5      0f114020       movups xmmword [rax + 0x20], xmm0
│           0x00001cb9      4889dc         mov rsp, rbx
│           0x00001cbc      49894668       mov qword [r14 + 0x68], rax
│           0x00001cc0      4c8b35195800.  mov r14, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00001cc7      4839dc         cmp rsp, rbx
│       ┌─< 0x00001cca      7415           je 0x1ce1
│       │   ; CODE XREF from fcn.00001530 @ 0x1cdf
│      ┌──> 0x00001ccc      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x00001cd3      48838c24f80f.  or qword [var_ff8h_6], 0
│      ╎│   0x00001cdc      4839dc         cmp rsp, rbx
│      └──< 0x00001cdf      75eb           jne 0x1ccc
│       │   ; CODE XREF from fcn.00001530 @ 0x1cca
│       └─> 0x00001ce1      4883ec40       sub rsp, 0x40
│           0x00001ce5      48834c243800   or qword [rsp + 0x38], 0
│           0x00001ceb      ba4d2a0000     mov edx, 0x2a4d             ; 'M*'
│           0x00001cf0      b901000000     mov ecx, 1
│           0x00001cf5      b82a000000     mov eax, 0x2a               ; '*'
│           0x00001cfa      488d355e3400.  lea rsi, [0x0000515f]
│           0x00001d01      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x00001d06      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│           0x00001d0d      4989e5         mov r13, rsp
│           0x00001d10      668955d6       mov word [var_2ah], dx
│       ┌─< 0x00001d14      eb22           jmp 0x1d38
..
│       │   ; CODE XREF from fcn.00001530 @ 0x1d4a
│      ┌──> 0x00001d20      89c2           mov edx, eax
│      ╎│   0x00001d22      480fafd7       imul rdx, rdi
│      ╎│   0x00001d26      48c1ea22       shr rdx, 0x22
│      ╎│   0x00001d2a      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x00001d2d      01d2           add edx, edx
│      ╎│   0x00001d2f      29d0           sub eax, edx
│      ╎│   0x00001d31      4898           cdqe
│      ╎│   0x00001d33      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x1d14
│      ╎└─> 0x00001d38      32040e         xor al, byte [rsi + rcx]
│      ╎    0x00001d3b      4188440dff     mov byte [r13 + rcx - 1], al
│      ╎    0x00001d40      89c8           mov eax, ecx
│      ╎    0x00001d42      4883c101       add rcx, 1
│      ╎    0x00001d46      4883f936       cmp rcx, 0x36
│      └──< 0x00001d4a      75d4           jne 0x1d20
│           0x00001d4c      ba07000000     mov edx, 7                  ; int prot
│           0x00001d51      4531c9         xor r9d, r9d                ; size_t offset
│           0x00001d54      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x00001d5a      31ff           xor edi, edi                ; void*addr
│           0x00001d5c      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00001d61      be35000000     mov esi, 0x35               ; '5' ; size_t length
│           0x00001d66      e8a5f3ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x00001d6b      418b5530       mov edx, dword [r13 + 0x30]
│           0x00001d6f      f3410f6f4d00   movdqu xmm1, xmmword [r13]
│           0x00001d75      f3410f6f5510   movdqu xmm2, xmmword [r13 + 0x10]
│           0x00001d7b      f3410f6f5d20   movdqu xmm3, xmmword [r13 + 0x20]
│           0x00001d81      895030         mov dword [rax + 0x30], edx
│           0x00001d84      410fb65534     movzx edx, byte [r13 + 0x34]
│           0x00001d89      0f1108         movups xmmword [rax], xmm1
│           0x00001d8c      885034         mov byte [rax + 0x34], dl
│           0x00001d8f      0f115010       movups xmmword [rax + 0x10], xmm2
│           0x00001d93      0f115820       movups xmmword [rax + 0x20], xmm3
│           0x00001d97      4889dc         mov rsp, rbx
│           0x00001d9a      498906         mov qword [r14], rax
│           0x00001d9d      4c8b353c5700.  mov r14, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00001da4      488d05f5f4ff.  lea rax, [0x000012a0]
│           0x00001dab      49894678       mov qword [r14 + 0x78], rax
│           0x00001daf      4839dc         cmp rsp, rbx
│       ┌─< 0x00001db2      7415           je 0x1dc9
│       │   ; CODE XREF from fcn.00001530 @ 0x1dc7
│      ┌──> 0x00001db4      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x00001dbb      48838c24f80f.  or qword [var_ff8h_5], 0
│      ╎│   0x00001dc4      4839dc         cmp rsp, rbx
│      └──< 0x00001dc7      75eb           jne 0x1db4
│       │   ; CODE XREF from fcn.00001530 @ 0x1db2
│       └─> 0x00001dc9      4883ec30       sub rsp, 0x30
│           0x00001dcd      48834c242800   or qword [rsp + 0x28], 0
│           0x00001dd3      b84d2a0000     mov eax, 0x2a4d             ; 'M*'
│           0x00001dd8      b901000000     mov ecx, 1
│           0x00001ddd      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x00001de2      488d35b63300.  lea rsi, [0x0000519f]
│           0x00001de9      668945d6       mov word [var_2ah], ax
│           0x00001ded      4989e5         mov r13, rsp
│           0x00001df0      b82a000000     mov eax, 0x2a               ; '*'
│           0x00001df5      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│       ┌─< 0x00001dfc      eb1a           jmp 0x1e18
..
│       │   ; CODE XREF from fcn.00001530 @ 0x1e2a
│      ┌──> 0x00001e00      89c2           mov edx, eax
│      ╎│   0x00001e02      480fafd7       imul rdx, rdi
│      ╎│   0x00001e06      48c1ea22       shr rdx, 0x22
│      ╎│   0x00001e0a      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x00001e0d      01d2           add edx, edx
│      ╎│   0x00001e0f      29d0           sub eax, edx
│      ╎│   0x00001e11      4898           cdqe
│      ╎│   0x00001e13      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x1dfc
│      ╎└─> 0x00001e18      32040e         xor al, byte [rsi + rcx]
│      ╎    0x00001e1b      4188440dff     mov byte [r13 + rcx - 1], al
│      ╎    0x00001e20      89c8           mov eax, ecx
│      ╎    0x00001e22      4883c101       add rcx, 1
│      ╎    0x00001e26      4883f929       cmp rcx, 0x29
│      └──< 0x00001e2a      75d4           jne 0x1e00
│           0x00001e2c      ba07000000     mov edx, 7                  ; int prot
│           0x00001e31      4531c9         xor r9d, r9d                ; size_t offset
│           0x00001e34      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x00001e3a      31ff           xor edi, edi                ; void*addr
│           0x00001e3c      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00001e41      be28000000     mov esi, 0x28               ; '(' ; size_t length
│           0x00001e46      e8c5f2ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x00001e4b      f3410f6f6500   movdqu xmm4, xmmword [r13]
│           0x00001e51      f3410f6f6d10   movdqu xmm5, xmmword [r13 + 0x10]
│           0x00001e57      498b5520       mov rdx, qword [r13 + 0x20]
│           0x00001e5b      0f1120         movups xmmword [rax], xmm4
│           0x00001e5e      48895020       mov qword [rax + 0x20], rdx
│           0x00001e62      0f116810       movups xmmword [rax + 0x10], xmm5
│           0x00001e66      4889dc         mov rsp, rbx
│           0x00001e69      498986800000.  mov qword [r14 + 0x80], rax
│           0x00001e70      4c8b35695600.  mov r14, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00001e77      4839dc         cmp rsp, rbx
│       ┌─< 0x00001e7a      7415           je 0x1e91
│       │   ; CODE XREF from fcn.00001530 @ 0x1e8f
│      ┌──> 0x00001e7c      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x00001e83      48838c24f80f.  or qword [var_18h_2], 0
│      ╎│   0x00001e8c      4839dc         cmp rsp, rbx
│      └──< 0x00001e8f      75eb           jne 0x1e7c
│       │   ; CODE XREF from fcn.00001530 @ 0x1e7a
│       └─> 0x00001e91      4883ec20       sub rsp, 0x20
│           0x00001e95      48834c241800   or qword [var_18h_2], 0
│           0x00001e9b      b84d2a0000     mov eax, 0x2a4d             ; 'M*'
│           0x00001ea0      b901000000     mov ecx, 1
│           0x00001ea5      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x00001eaa      488d35ce3400.  lea rsi, [0x0000537f]
│           0x00001eb1      668945d6       mov word [var_2ah], ax
│           0x00001eb5      4989e5         mov r13, rsp
│           0x00001eb8      b82a000000     mov eax, 0x2a               ; '*'
│           0x00001ebd      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│       ┌─< 0x00001ec4      eb22           jmp 0x1ee8
..
│       │   ; CODE XREF from fcn.00001530 @ 0x1efa
│      ┌──> 0x00001ed0      89c2           mov edx, eax
│      ╎│   0x00001ed2      480fafd7       imul rdx, rdi
│      ╎│   0x00001ed6      48c1ea22       shr rdx, 0x22
│      ╎│   0x00001eda      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x00001edd      01d2           add edx, edx
│      ╎│   0x00001edf      29d0           sub eax, edx
│      ╎│   0x00001ee1      4898           cdqe
│      ╎│   0x00001ee3      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x1ec4
│      ╎└─> 0x00001ee8      32040e         xor al, byte [rsi + rcx]
│      ╎    0x00001eeb      4188440dff     mov byte [r13 + rcx - 1], al
│      ╎    0x00001ef0      89c8           mov eax, ecx
│      ╎    0x00001ef2      4883c101       add rcx, 1
│      ╎    0x00001ef6      4883f921       cmp rcx, 0x21
│      └──< 0x00001efa      75d4           jne 0x1ed0
│           0x00001efc      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00001f01      be20000000     mov esi, 0x20               ; "@" ; size_t length
│           0x00001f06      31ff           xor edi, edi                ; void*addr
│           0x00001f08      4531c9         xor r9d, r9d                ; size_t offset
│           0x00001f0b      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x00001f11      ba07000000     mov edx, 7                  ; int prot
│           0x00001f16      e8f5f1ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x00001f1b      f3410f6f7500   movdqu xmm6, xmmword [r13]
│           0x00001f21      f3410f6f7d10   movdqu xmm7, xmmword [r13 + 0x10]
│           0x00001f27      b901000000     mov ecx, 1
│           0x00001f2c      488d359c3200.  lea rsi, [0x000051cf]
│           0x00001f33      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x00001f38      0f1130         movups xmmword [rax], xmm6
│           0x00001f3b      0f117810       movups xmmword [rax + 0x10], xmm7
│           0x00001f3f      4c8b2d9a5500.  mov r13, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00001f46      4889dc         mov rsp, rbx
│           0x00001f49      49894640       mov qword [r14 + 0x40], rax
│           0x00001f4d      488d058cf4ff.  lea rax, [0x000013e0]
│           0x00001f54      49894538       mov qword [r13 + 0x38], rax
│           0x00001f58      b84d2a0000     mov eax, 0x2a4d             ; 'M*'
│           0x00001f5d      668945d6       mov word [var_2ah], ax
│           0x00001f61      b82a000000     mov eax, 0x2a               ; '*'
│           0x00001f66      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│       ┌─< 0x00001f6d      eb19           jmp 0x1f88
..
│       │   ; CODE XREF from fcn.00001530 @ 0x1f99
│      ┌──> 0x00001f70      89c2           mov edx, eax
│      ╎│   0x00001f72      480fafd7       imul rdx, rdi
│      ╎│   0x00001f76      48c1ea22       shr rdx, 0x22
│      ╎│   0x00001f7a      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x00001f7d      01d2           add edx, edx
│      ╎│   0x00001f7f      29d0           sub eax, edx
│      ╎│   0x00001f81      4898           cdqe
│      ╎│   0x00001f83      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x1f6d
│      ╎└─> 0x00001f88      32040e         xor al, byte [rsi + rcx]
│      ╎    0x00001f8b      4188040c       mov byte [r12 + rcx], al
│      ╎    0x00001f8f      89c8           mov eax, ecx
│      ╎    0x00001f91      4883c101       add rcx, 1
│      ╎    0x00001f95      4883f915       cmp rcx, 0x15
│      └──< 0x00001f99      75d5           jne 0x1f70
│           0x00001f9b      ba07000000     mov edx, 7                  ; int prot
│           0x00001fa0      4531c9         xor r9d, r9d                ; size_t offset
│           0x00001fa3      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x00001fa9      31ff           xor edi, edi                ; void*addr
│           0x00001fab      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00001fb0      be14000000     mov esi, 0x14               ; size_t length
│           0x00001fb5      e856f1ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x00001fba      f30f6f45b0     movdqu xmm0, xmmword [var_50h]
│           0x00001fbf      8b55c0         mov edx, dword [var_40h]
│           0x00001fc2      0f1100         movups xmmword [rax], xmm0
│           0x00001fc5      895010         mov dword [rax + 0x10], edx
│           0x00001fc8      4889dc         mov rsp, rbx
│           0x00001fcb      4c8b350e5500.  mov r14, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00001fd2      498985b80000.  mov qword [r13 + 0xb8], rax
│           0x00001fd9      4839dc         cmp rsp, rbx
│       ┌─< 0x00001fdc      7415           je 0x1ff3
│       │   ; CODE XREF from fcn.00001530 @ 0x1ff1
│      ┌──> 0x00001fde      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x00001fe5      48838c24f80f.  or qword [var_ff8h_4], 0
│      ╎│   0x00001fee      4839dc         cmp rsp, rbx
│      └──< 0x00001ff1      75eb           jne 0x1fde
│       │   ; CODE XREF from fcn.00001530 @ 0x1fdc
│       └─> 0x00001ff3      4883ec30       sub rsp, 0x30
│           0x00001ff7      48834c242800   or qword [rsp + 0x28], 0
│           0x00001ffd      b84d2a0000     mov eax, 0x2a4d             ; 'M*'
│           0x00002002      b901000000     mov ecx, 1
│           0x00002007      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x0000200c      488d35cc3300.  lea rsi, [0x000053df]
│           0x00002013      668945d6       mov word [var_2ah], ax
│           0x00002017      4989e5         mov r13, rsp
│           0x0000201a      b82a000000     mov eax, 0x2a               ; '*'
│           0x0000201f      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│       ┌─< 0x00002026      eb20           jmp 0x2048
..
│       │   ; CODE XREF from fcn.00001530 @ 0x205a
│      ┌──> 0x00002030      89c2           mov edx, eax
│      ╎│   0x00002032      480fafd7       imul rdx, rdi
│      ╎│   0x00002036      48c1ea22       shr rdx, 0x22
│      ╎│   0x0000203a      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x0000203d      01d2           add edx, edx
│      ╎│   0x0000203f      29d0           sub eax, edx
│      ╎│   0x00002041      4898           cdqe
│      ╎│   0x00002043      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x2026
│      ╎└─> 0x00002048      32040e         xor al, byte [rsi + rcx]
│      ╎    0x0000204b      4188440dff     mov byte [r13 + rcx - 1], al
│      ╎    0x00002050      89c8           mov eax, ecx
│      ╎    0x00002052      4883c101       add rcx, 1
│      ╎    0x00002056      4883f926       cmp rcx, 0x26
│      └──< 0x0000205a      75d4           jne 0x2030
│           0x0000205c      ba07000000     mov edx, 7                  ; int prot
│           0x00002061      4531c9         xor r9d, r9d                ; size_t offset
│           0x00002064      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x0000206a      31ff           xor edi, edi                ; void*addr
│           0x0000206c      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00002071      be25000000     mov esi, 0x25               ; '%' ; size_t length
│           0x00002076      e895f0ffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x0000207b      418b5520       mov edx, dword [r13 + 0x20]
│           0x0000207f      f3410f6f4d00   movdqu xmm1, xmmword [r13]
│           0x00002085      f3410f6f5510   movdqu xmm2, xmmword [r13 + 0x10]
│           0x0000208b      895020         mov dword [rax + 0x20], edx
│           0x0000208e      410fb65524     movzx edx, byte [r13 + 0x24]
│           0x00002093      0f1108         movups xmmword [rax], xmm1
│           0x00002096      885024         mov byte [rax + 0x24], dl
│           0x00002099      0f115010       movups xmmword [rax + 0x10], xmm2
│           0x0000209d      4889dc         mov rsp, rbx
│           0x000020a0      49894608       mov qword [r14 + 8], rax
│           0x000020a4      4c8b35355400.  mov r14, qword [0x000074e0] ; [0x74e0:8]=0
│           0x000020ab      4839dc         cmp rsp, rbx
│       ┌─< 0x000020ae      7415           je 0x20c5
│       │   ; CODE XREF from fcn.00001530 @ 0x20c3
│      ┌──> 0x000020b0      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x000020b7      48838c24f80f.  or qword [var_ff8h_3], 0
│      ╎│   0x000020c0      4839dc         cmp rsp, rbx
│      └──< 0x000020c3      75eb           jne 0x20b0
│       │   ; CODE XREF from fcn.00001530 @ 0x20ae
│       └─> 0x000020c5      4883ec40       sub rsp, 0x40
│           0x000020c9      48834c243800   or qword [rsp + 0x38], 0
│           0x000020cf      b84d2a0000     mov eax, 0x2a4d             ; 'M*'
│           0x000020d4      b901000000     mov ecx, 1
│           0x000020d9      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x000020de      488d351a3100.  lea rsi, [0x000051ff]
│           0x000020e5      668945d6       mov word [var_2ah], ax
│           0x000020e9      4989e5         mov r13, rsp
│           0x000020ec      b82a000000     mov eax, 0x2a               ; '*'
│           0x000020f1      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│       ┌─< 0x000020f8      eb1e           jmp 0x2118
..
│       │   ; CODE XREF from fcn.00001530 @ 0x212a
│      ┌──> 0x00002100      89c2           mov edx, eax
│      ╎│   0x00002102      480fafd7       imul rdx, rdi
│      ╎│   0x00002106      48c1ea22       shr rdx, 0x22
│      ╎│   0x0000210a      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x0000210d      01d2           add edx, edx
│      ╎│   0x0000210f      29d0           sub eax, edx
│      ╎│   0x00002111      4898           cdqe
│      ╎│   0x00002113      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x20f8
│      ╎└─> 0x00002118      32040e         xor al, byte [rsi + rcx]
│      ╎    0x0000211b      4188440dff     mov byte [r13 + rcx - 1], al
│      ╎    0x00002120      89c8           mov eax, ecx
│      ╎    0x00002122      4883c101       add rcx, 1
│      ╎    0x00002126      4883f933       cmp rcx, 0x33
│      └──< 0x0000212a      75d4           jne 0x2100
│           0x0000212c      ba07000000     mov edx, 7                  ; int prot
│           0x00002131      4531c9         xor r9d, r9d                ; size_t offset
│           0x00002134      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x0000213a      31ff           xor edi, edi                ; void*addr
│           0x0000213c      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00002141      be32000000     mov esi, 0x32               ; '2' ; size_t length
│           0x00002146      e8c5efffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x0000214b      f3410f6f5d00   movdqu xmm3, xmmword [r13]
│           0x00002151      f3410f6f6510   movdqu xmm4, xmmword [r13 + 0x10]
│           0x00002157      f3410f6f6d20   movdqu xmm5, xmmword [r13 + 0x20]
│           0x0000215d      410fb75530     movzx edx, word [r13 + 0x30]
│           0x00002162      0f1118         movups xmmword [rax], xmm3
│           0x00002165      66895030       mov word [rax + 0x30], dx
│           0x00002169      0f116010       movups xmmword [rax + 0x10], xmm4
│           0x0000216d      0f116820       movups xmmword [rax + 0x20], xmm5
│           0x00002171      4889dc         mov rsp, rbx
│           0x00002174      498986b00000.  mov qword [r14 + 0xb0], rax
│           0x0000217b      4c8b355e5300.  mov r14, qword [0x000074e0] ; [0x74e0:8]=0
│           0x00002182      4839dc         cmp rsp, rbx
│       ┌─< 0x00002185      7415           je 0x219c
│       │   ; CODE XREF from fcn.00001530 @ 0x219a
│      ┌──> 0x00002187      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x0000218e      48838c24f80f.  or qword [var_ff8h_2], 0
│      ╎│   0x00002197      4839dc         cmp rsp, rbx
│      └──< 0x0000219a      75eb           jne 0x2187
│       │   ; CODE XREF from fcn.00001530 @ 0x2185
│       └─> 0x0000219c      4883ec30       sub rsp, 0x30
│           0x000021a0      48834c242800   or qword [rsp + 0x28], 0
│           0x000021a6      b901000000     mov ecx, 1
│           0x000021ab      b82a000000     mov eax, 0x2a               ; '*'
│           0x000021b0      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x000021b5      41bb4d2a0000   mov r11d, 0x2a4d            ; 'M*'
│           0x000021bb      488d355d3300.  lea rsi, [0x0000551f]
│           0x000021c2      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│           0x000021c9      4989e5         mov r13, rsp
│           0x000021cc      6644895dd6     mov word [var_2ah], r11w
│       ┌─< 0x000021d1      eb1d           jmp 0x21f0
..
│       │   ; CODE XREF from fcn.00001530 @ 0x2202
│      ┌──> 0x000021d8      89c2           mov edx, eax
│      ╎│   0x000021da      480fafd7       imul rdx, rdi
│      ╎│   0x000021de      48c1ea22       shr rdx, 0x22
│      ╎│   0x000021e2      8d1452         lea edx, [rdx + rdx*2]
│      ╎│   0x000021e5      01d2           add edx, edx
│      ╎│   0x000021e7      29d0           sub eax, edx
│      ╎│   0x000021e9      4898           cdqe
│      ╎│   0x000021eb      0fb64405d2     movzx eax, byte [rbp + rax - 0x2e]
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x21d1
│      ╎└─> 0x000021f0      32040e         xor al, byte [rsi + rcx]
│      ╎    0x000021f3      4188440dff     mov byte [r13 + rcx - 1], al
│      ╎    0x000021f8      89c8           mov eax, ecx
│      ╎    0x000021fa      4883c101       add rcx, 1
│      ╎    0x000021fe      4883f922       cmp rcx, 0x22
│      └──< 0x00002202      75d4           jne 0x21d8
│           0x00002204      ba07000000     mov edx, 7                  ; int prot
│           0x00002209      4531c9         xor r9d, r9d                ; size_t offset
│           0x0000220c      41b8ffffffff   mov r8d, 0xffffffff         ; -1 ; int fd
│           0x00002212      31ff           xor edi, edi                ; void*addr
│           0x00002214      b922000000     mov ecx, 0x22               ; '\"' ; int flags
│           0x00002219      be21000000     mov esi, 0x21               ; '!' ; size_t length
│           0x0000221e      e8edeeffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
│           0x00002223      f3410f6f7500   movdqu xmm6, xmmword [r13]
│           0x00002229      f3410f6f7d10   movdqu xmm7, xmmword [r13 + 0x10]
│           0x0000222f      410fb65520     movzx edx, byte [r13 + 0x20]
│           0x00002234      0f1130         movups xmmword [rax], xmm6
│           0x00002237      885020         mov byte [rax + 0x20], dl
│           0x0000223a      0f117810       movups xmmword [rax + 0x10], xmm7
│           0x0000223e      4889dc         mov rsp, rbx
│           0x00002241      498986c80000.  mov qword [r14 + 0xc8], rax
│           0x00002248      4c8b35915200.  mov r14, qword [0x000074e0] ; [0x74e0:8]=0
│           0x0000224f      4839dc         cmp rsp, rbx
│       ┌─< 0x00002252      7415           je 0x2269
│       │   ; CODE XREF from fcn.00001530 @ 0x2267
│      ┌──> 0x00002254      4881ec001000.  sub rsp, segment.LOAD1      ; 0x1000
│      ╎│   0x0000225b      48838c24f80f.  or qword [var_ff8h], 0
│      ╎│   0x00002264      4839dc         cmp rsp, rbx
│      └──< 0x00002267      75eb           jne 0x2254
│       │   ; CODE XREF from fcn.00001530 @ 0x2252
│       └─> 0x00002269      4883ec30       sub rsp, 0x30
│           0x0000226d      48834c242800   or qword [rsp + 0x28], 0
│           0x00002273      b901000000     mov ecx, 1
│           0x00002278      b82a000000     mov eax, 0x2a               ; '*'
│           0x0000227d      bfabaaaaaa     mov edi, 0xaaaaaaab
│           0x00002282      41ba4d2a0000   mov r10d, 0x2a4d            ; 'M*'
│           0x00002288      488d35303000.  lea rsi, [0x000052bf]
│           0x0000228f      c745d22a0b21.  mov dword [var_2eh], 0x21210b2a ; '*\v!!'
│           0x00002296      4989e5         mov r13, rsp
│           0x00002299      66448955d6     mov word [var_2ah], r10w
│       ┌─< 0x0000229e      eb18           jmp 0x22b8
        │   ; CODE XREF from fcn.00001530 @ 0x22ca
..
│      ╎│   ; CODE XREF from fcn.00001530 @ 0x229e
│      ╎└─> 0x000022b8      32040e         xor al, byte [rsi + rcx]
│      ╎    0x000022bb      4188440dff     mov byte [r13 + rcx - 1], al
│      ╎    0x000022c0      89c8           mov eax, ecx
│      ╎    0x000022c2      4883c101       add rcx, 1
│      ╎    0x000022c6      4883f926       cmp rcx, 0x26
└      └──< 0x000022ca      75d4           jne 0x22a0
