from compute_outputs import run_with_input


def main():
    base = list("a" * 32)
    for ch in ["a", "b", "c", "d"]:
        base[29] = ch
        computed = run_with_input("".join(base))[0][1]
        bytes_le = [(computed >> (8 * i)) & 0xFF for i in range(4)]
        print(ch, hex(computed), bytes_le)


if __name__ == "__main__":
    main()
