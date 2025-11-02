from pathlib import Path

from compute_outputs import run_with_input

BASE = "a" * 32


def main():
    base_vals = run_with_input(BASE)
    print("Base:")
    for idx, (exp, val) in enumerate(base_vals):
        print(f"  block{idx}: expected={exp:#010x} computed={val:#010x}")

    print("\nPer-index impact (delta values):")
    for pos in range(32):
        test_chars = list(BASE)
        test_chars[pos] = chr(ord(test_chars[pos]) + 1)
        test = "".join(test_chars)
        vals = run_with_input(test)
        deltas = []
        for (_, base_val), (_, new_val) in zip(base_vals, vals):
            deltas.append((new_val - base_val) & 0xFFFFFFFF)
        changed = [i for i, d in enumerate(deltas) if d != 0]
        if changed:
            block = changed[0]
            delta = deltas[block]
            bytes_delta = [(delta >> (8 * i)) & 0xFF for i in range(4)]
            print(f"pos {pos:02d}: block {block} delta bytes {bytes_delta}")
        else:
            print(f"pos {pos:02d}: no change")


if __name__ == "__main__":
    main()
