import re
from pathlib import Path

CONSTS = {
    0x2A239824,
    0x8A73EA61,
    0xBA3CBD99,
    0xDDBDD50D,
    0xF3444305,
    0x47272423,
    0x1517DD9C,
    0xB639B429,
}


def parse_log(path: Path):
    values = []
    lines = path.read_text().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("before handler=2"):
            entries = []
            j = i + 1
            while j < len(lines) and lines[j].startswith("  ["):
                m = re.search(r"\[(\d+)\] = 0x([0-9a-fA-F]+)", lines[j])
                if not m:
                    break
                idx = int(m.group(1))
                val = int(m.group(2), 16)
                entries.append((idx, val))
                j += 1
            if len(entries) >= 2:
                top_idx, top_val = entries[0]
                next_idx, next_val = entries[1]
                if top_val & 0xFFFFFFFF in CONSTS:
                    values.append((top_val & 0xFFFFFFFF, next_val & 0xFFFFFFFF))
            i = j
        else:
            i += 1
    return values


def main():
    log_path = Path("handler_log.txt")
    vals = parse_log(log_path)
    for c, comp in vals:
        print(f"expected={c:#010x} computed={comp:#010x}")


if __name__ == "__main__":
    main()
