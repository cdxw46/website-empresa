from compute_outputs import run_with_input


def main():
    base = [97] * 32
    base[0] = 0xD5
    base[1] = 0xDB
    base[17] = 0xC9
    base[29] = 0xD4
    s = ''.join(chr(c) for c in base)
    vals = run_with_input(s)
    print(vals[0])


if __name__ == "__main__":
    main()
