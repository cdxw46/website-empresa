from compute_outputs import run_with_input


def main():
    base = [97] * 32
    # positions for block0
    indices = [0, 1, 17, 29]
    samples = {}
    for idx in indices:
        mapping = {}
        for val in range(1, 256):
            chars = base.copy()
            chars[idx] = val
            s = ''.join(chr(c) for c in chars)
            computed = run_with_input(s)[0][1]
            bytes_le = [(computed >> (8 * i)) & 0xFF for i in range(4)]
            mapping[val] = bytes_le
        samples[idx] = mapping
    for idx, mapping in samples.items():
        print(f"Index {idx}")
        for val in range(97, 97 + 5):
            print(val, mapping[val])
        print()


if __name__ == "__main__":
    main()
