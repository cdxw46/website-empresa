import json
from pathlib import Path
from typing import List, Tuple, Dict

OPS = json.loads(Path("ops_full.json").read_text())

PTR = object()
MASK = (1 << 64) - 1
CHECK_OPS = [300, 303, 306, 309, 312, 315, 318, 321]


def run_vm(input_bytes: List[int]) -> Dict[int, Tuple[int, int, int]]:
    stack = [PTR]
    log: Dict[int, Tuple[int, int, int]] = {}

    for idx, op in enumerate(OPS):
        op_id = op["id"]
        imm = op["imm"]

        if op_id == 8:
            continue
        elif op_id == 12:
            stack.append(stack[-1])
        elif op_id == 9:
            stack[-1] = len(input_bytes)
        elif op_id == 22:
            stack[-1] = (stack[-1] * 6 - 12) & MASK
        elif op_id == 15:
            stack.append(imm)
        elif op_id == 21:
            b = stack.pop()
            stack[-1] = (stack[-1] + b) & MASK
        elif op_id == 17:
            b = stack.pop()
            a = stack.pop()
            stack.append(a // b)
        elif op_id == 0:
            stack[-1] = (stack[-1] * 8 + 0x18) & MASK
        elif op_id == 23:
            b = stack.pop()
            stack[-1] = (stack[-1] * b) & MASK
        elif op_id == 20:
            b = stack.pop()
            a = stack.pop()
            stack.append(a % b)
        elif op_id == 2:
            b = stack.pop()
            a = stack.pop()
            result = (a - b) & MASK
            stack.append(result)
            if idx in CHECK_OPS:
                log[idx] = (a & 0xFFFFFFFF, b & 0xFFFFFFFF, result & 0xFFFFFFFF)
        elif op_id == 1:
            stack[-1] = input_bytes[imm]
        elif op_id == 10:
            stack.append(stack[-1 - imm])
        elif op_id == 13:
            shift = stack.pop() & 0xFF
            stack[-1] = (stack[-1] << shift) & MASK
        elif op_id == 11:
            b = stack.pop()
            stack[-1] = (stack[-1] | b) & MASK
        elif op_id == 7:
            stack.pop()
        elif op_id == 4:
            stack[-1] = ((stack[-1] + 0x11) % 3)
        elif op_id == 16:
            b = stack.pop()
            a = stack.pop()
            stack.append(1 if a == b else 0)
        elif op_id == 14:
            stack.pop()
        elif op_id == 3:
            continue
        elif op_id == 19:
            shift = stack.pop() & 0xFF
            stack[-1] = (stack[-1] >> shift)
        elif op_id == 18:
            continue
        else:
            raise ValueError(f"Unhandled op {op_id}")

    return log


def main():
    vals = run_vm([ord('a')] * 32)
    for idx in CHECK_OPS:
        a, b, res = vals[idx]
        print(idx, hex(a), hex(b), hex(res))


if __name__ == "__main__":
    main()
