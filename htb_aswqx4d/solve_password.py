from itertools import product

from z3 import BitVec, BitVecVal, Solver, ZeroExt, sat

from compute_outputs import run_with_input


TARGETS = [
    0x2A239824,
    0x8A73EA61,
    0xBA3CBD99,
    0xDDBDD50D,
    0xF3444305,
    0x47272423,
    0x1517DD9C,
    0xB639B429,
]


BLOCK_POSITIONS = [
    [0, 1, 17, 29],
    [5, 10, 25, 31],
    [3, 21, 22, 30],
    [8, 16, 23, 28],
    [13, 19, 20, 26],
    [2, 6, 9, 18],
    [4, 7, 11, 12],
    [14, 15, 24, 27],
]


def compute_base_and_deltas():
    base_chars = [97] * 32
    base_str = ''.join(chr(c) for c in base_chars)
    base_vals = [comp for _, comp in run_with_input(base_str)]

    deltas = []
    for pos in range(32):
        chars = base_chars.copy()
        chars[pos] = (chars[pos] + 1) % 256
        if chars[pos] == 0:
            chars[pos] = 1  # avoid null byte
        test_str = ''.join(chr(c) for c in chars)
        comps = [comp for _, comp in run_with_input(test_str)]
        delta_vals = [((comp - base) & 0xFFFFFFFF) for comp, base in zip(comps, base_vals)]
        deltas.append(delta_vals)
    return base_chars, base_vals, deltas


def main():
    base_chars, base_vals, deltas = compute_base_and_deltas()

    s = Solver()
    vars_bytes = [BitVec(f'x_{i}', 8) for i in range(32)]

    for block_idx, positions in enumerate(BLOCK_POSITIONS):
        base_val = base_vals[block_idx]
        expr = BitVec(f'expr_{block_idx}', 32)
        expr = BitVecVal(base_val & 0xFFFFFFFF, 32)
        for pos in positions:
            diff = ZeroExt(24, vars_bytes[pos]) - BitVecVal(base_chars[pos], 32)
            delta = BitVecVal(deltas[pos][block_idx] & 0xFFFFFFFF, 32)
            expr = expr + diff * delta
        s.add(expr & BitVecVal(0xFFFFFFFF, 32) == BitVecVal(TARGETS[block_idx], 32))

    if s.check() != sat:
        print("No solution found")
        return

    model = s.model()
    result_bytes = [model.eval(vars_bytes[i]).as_long() for i in range(32)]
    print("Bytes:", result_bytes)
    print("Hex:", ''.join(f'{b:02x}' for b in result_bytes))
    try:
        print("ASCII:", ''.join(chr(b) for b in result_bytes))
    except ValueError:
        pass


if __name__ == "__main__":
    main()
