import json
from pathlib import Path

from z3 import BitVec, BitVecVal, Solver, ZeroExt, simplify, sat, UDiv, URem, is_bv_value


OPS_PATH = Path("ops_full.json")


def load_ops():
    return json.loads(OPS_PATH.read_text())


def build_solver():
    ops = load_ops()
    solver = Solver()

    inputs8 = [BitVec(f"x_{i}", 8) for i in range(32)]
    inputs64 = [ZeroExt(56, v) for v in inputs8]

    stack = []
    constraints = []

    ptr_sym = BitVec("PTR", 64)

    for idx, op in enumerate(ops):
        op_id = op["id"]
        imm = op["imm"]
        after = op.get("after") or []
        after_top = after[0][1] if after else None

        if op_id == 8:
            stack.append(ptr_sym)
        elif op_id == 12:
            stack.append(stack[-1])
        elif op_id == 9:
            stack[-1] = BitVecVal(32, 64)
        elif op_id == 22:
            stack[-1] = (stack[-1] * BitVecVal(6, 64) - BitVecVal(12, 64)) & BitVecVal(0xFFFFFFFFFFFFFFFF, 64)
        elif op_id == 15:
            stack.append(BitVecVal(imm & 0xFFFFFFFFFFFFFFFF, 64))
        elif op_id == 21:
            b = stack.pop()
            stack[-1] = (stack[-1] + b) & BitVecVal(0xFFFFFFFFFFFFFFFF, 64)
        elif op_id == 17:
            b = stack.pop()
            a = stack.pop()
            stack.append(UDiv(a, b))
        elif op_id == 0:
            stack[-1] = (stack[-1] * BitVecVal(8, 64) + BitVecVal(0x18, 64)) & BitVecVal(0xFFFFFFFFFFFFFFFF, 64)
        elif op_id == 23:
            b = stack.pop()
            stack[-1] = (stack[-1] * b) & BitVecVal(0xFFFFFFFFFFFFFFFF, 64)
        elif op_id == 20:
            b = stack.pop()
            a = stack.pop()
            stack.append(URem(a, b))
        elif op_id == 2:
            b = stack.pop()
            a = stack.pop()
            result = (a - b) & BitVecVal(0xFFFFFFFFFFFFFFFF, 64)
            stack.append(result)
            if is_bv_value(b) and b.as_long() < (1 << 32):
                constraints.append(a == b)
        elif op_id == 1:
            idx_input = imm
            stack[-1] = inputs64[idx_input]
        elif op_id == 10:
            stack.append(stack[-1 - imm])
        elif op_id == 13:
            shift = stack.pop()
            stack[-1] = (stack[-1] << (shift & BitVecVal(0x3F, 64))) & BitVecVal(0xFFFFFFFFFFFFFFFF, 64)
        elif op_id == 11:
            b = stack.pop()
            stack[-1] = stack[-1] | b
        elif op_id == 7:
            stack.pop()
        elif op_id == 4:
            stack[-1] = URem(stack[-1] + BitVecVal(0x11, 64), BitVecVal(3, 64))
        elif op_id == 16:
            b = stack.pop()
            a = stack.pop()
            eq_val = after_top if after_top is not None else 1
            eq = BitVec(f"eq_{idx}", 64)
            solver.add(eq == BitVecVal(eq_val & 0xFFFFFFFFFFFFFFFF, 64))
            solver.add((a == b) == (eq == BitVecVal(1, 64)))
            stack.append(eq)
        elif op_id == 14:
            stack.pop()
        elif op_id == 3:
            pass
        elif op_id == 19:
            shift = stack.pop()
            stack[-1] = stack[-1] >> (shift & BitVecVal(0x3F, 64))
        elif op_id == 18:
            pass
        else:
            raise ValueError(f"Unhandled op {op_id}")

    for c in constraints:
        solver.add(simplify(c))

    return solver, inputs8


def main():
    solver, inputs = build_solver()
    if solver.check() != sat:
        print("No solution")
        return
    model = solver.model()
    result = [model.eval(v).as_long() for v in inputs]
    print("Bytes:", result)
    try:
        print("ASCII:", ''.join(chr(b) for b in result))
    except ValueError:
        pass
    print("Hex:", ''.join(f"{b:02x}" for b in result))


if __name__ == "__main__":
    main()
