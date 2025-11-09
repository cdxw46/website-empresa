import os
import subprocess

ADDRESSES = [
    0x40311b, 0x4032c6, 0x403a7c, 0x403f74, 0x404122, 0x4044bf,
    0x40501f, 0x4056ed, 0x4060e1, 0x4064c6, 0x406581, 0x406e98,
    0x40727d, 0x407b0d, 0x4082b3, 0x408cd4, 0x408d7d, 0x40951c,
    0x409cd4, 0x40a47a, 0x40af12, 0x40b92e, 0x40c324, 0x40caca,
    0x40d287, 0x40d303, 0x40d469, 0x40d4e5, 0x40dbac, 0x40df91,
    0x40e031, 0x40e7e9, 0x40e865, 0x40e905, 0x40ecea, 0x40ee8f,
    0x40f647, 0x410063, 0x41010c, 0x410257,
]

ENV = os.environ.copy()
ENV["WINEDEBUG"] = "+relay,+relay=KERNEL32"


def run_wine(input_bytes: bytes):
    proc = subprocess.run(
        ["wine", "flag_errata.exe"],
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=ENV,
        timeout=8,
    )
    data = (proc.stdout + proc.stderr).decode(errors="ignore")
    records = []
    for line in data.splitlines():
        if "GetLastError" not in line or "Ret" not in line:
            continue
        ret_idx = line.find("ret=")
        val_idx = line.find("retval=")
        if ret_idx == -1 or val_idx == -1:
            continue
        try:
            ret = int(line[ret_idx + 4: ret_idx + 12], 16)
            val = int(line[val_idx + 7: val_idx + 15], 16)
        except ValueError:
            continue
        records.append((ret, val))
    return records


def extract_char(prefix: bytes):
    input_bytes = prefix + b"A\n"
    records = run_wine(input_bytes)
    addr_index = 0
    groups = []
    current = []
    for ret, val in records:
        current.append(val)
        if addr_index >= len(ADDRESSES):
            break
        if ret == ADDRESSES[addr_index]:
            groups.append(current)
            current = []
            addr_index += 1
            if addr_index >= len(prefix) + 1:
                break
    target_index = len(prefix)
    if target_index >= len(groups):
        raise RuntimeError(f"Failed to recover character at index {target_index}")
    seq = groups[target_index]
    seq_sum = sum(seq)
    total = seq_sum % 126
    return total, seq_sum


def main():
    prefix = bytearray()
    recovered = []
    for _ in range(len(ADDRESSES)):
        code, seq_sum = extract_char(bytes(prefix))
        prefix.append(code)
        recovered.append((code, seq_sum))
        disp = chr(code) if 32 <= code < 127 else f"\\x{code:02x}"
        print(len(prefix), code, disp, seq_sum)
    print("Final bytes:", prefix)
    try:
        print("As string:", prefix.decode())
    except UnicodeDecodeError:
        print("Non-printable characters present")
    print("Sums:", [seq_sum for _, seq_sum in recovered])


if __name__ == "__main__":
    main()
