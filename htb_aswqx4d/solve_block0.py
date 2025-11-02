ASCII_RANGE = range(32, 127)


def solve_block0():
    solutions = []
    for x3 in ASCII_RANGE:
        p3 = x3 & 1
        x2 = (152 - 207 - 128 * p3) % 256
        if x2 not in ASCII_RANGE:
            continue
        p2 = x2 & 1
        x0 = (36 - 207 - 128 * p2) % 256
        if x0 not in ASCII_RANGE:
            continue
        p0 = x0 & 1
        x1 = (42 - 207 - 128 * p0) % 256
        if x1 not in ASCII_RANGE:
            continue
        p1 = x1 & 1
        lhs = (207 + x3 + 128 * p1) % 256
        if lhs != 35:
            continue
        solutions.append((x0, x1, x2, x3))
    return solutions


def main():
    sols = solve_block0()
    print("solutions", len(sols))
    for sol in sols:
        chars = ''.join(chr(c) for c in sol)
        print(chars, sol)


if __name__ == "__main__":
    main()
