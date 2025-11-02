import re, json
from pathlib import Path

def parse_log(path):
    lines = Path(path).read_text().splitlines()
    ops = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"before handler=(\d+) sp=(\d+)", line)
        if not m:
            i += 1
            continue
        op_id = int(m.group(1))
        sp_before = int(m.group(2))
        before_vals = []
        j = i + 1
        while j < len(lines) and lines[j].startswith("  "):
            mb = re.search(r"\[(\d+)\] = 0x([0-9a-f]+)", lines[j])
            if not mb:
                break
            before_vals.append((int(mb.group(1)), int(mb.group(2), 16)))
            j += 1
        sp_after = None
        if j < len(lines) and lines[j].startswith("after handler="):
            m2 = re.match(r"after handler=\d+ sp=(\d+)", lines[j])
            if m2:
                sp_after = int(m2.group(1))
            j += 1
        after_vals = []
        while j < len(lines) and lines[j].startswith("  "):
            ma = re.search(r"\[(\d+)\] = 0x([0-9a-f]+)", lines[j])
            if not ma:
                break
            after_vals.append((int(ma.group(1)), int(ma.group(2), 16)))
            j += 1
        op = {
            "id": op_id,
            "sp_before": sp_before,
            "sp_after": sp_after,
            "before": before_vals,
            "after": after_vals,
            "imm": None,
        }
        ops.append(op)
        i = j
    return ops

def annotate_immediates(ops):
    for op in ops:
        if op["id"] == 15:
            if op["after"]:
                op["imm"] = op["after"][0][1] & 0xffffffff
        elif op["id"] == 10:
            if op["before"] and op["after"]:
                new_val = op["after"][0][1]
                src_idx = None
                for idx, val in op["before"]:
                    if val == new_val:
                        src_idx = idx
                        break
                if src_idx is not None:
                    imm = (op["sp_before"] - 1) - src_idx
                    op["imm"] = imm & 0xffffffff

if __name__ == "__main__":
    import sys
    log_path = sys.argv[1]
    out_path = sys.argv[2]
    ops = parse_log(log_path)
    annotate_immediates(ops)
    Path(out_path).write_text(json.dumps(ops))
