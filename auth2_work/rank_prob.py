import sys, json, random, string
sys.path.append("/workspace/auth2_work/authentification-2")
from gcm.gcm import GCM
from gcm import BLOCK_LEN
from crypto import IV

R = 0xe1000000000000000000000000000000
MASK = (1 << 128) - 1

def gf_mul(x, y):
    z = 0
    v = x
    w = y
    for _ in range(128):
        if (w >> 127) & 1:
            z ^= v
        w = ((w << 1) & MASK)
        if v & 1:
            v = (v >> 1) ^ R
        else:
            v >>= 1
    return z

def ghash_with_H(blocks, H):
    Y = 0
    for Xi in blocks:
        Y ^= Xi
        Y = gf_mul(Y, H)
    return Y

def rank_for(username, key):
    G = GCM(key, IV)
    plaintext = json.dumps({"username": username, "role": "guest"}).encode()
    ct, tag = G.encrypt(plaintext)
    pad_len = (BLOCK_LEN - len(ct) % BLOCK_LEN) % BLOCK_LEN
    buf = ct + b"\x00" * pad_len + (0).to_bytes(8, "big") + (len(ct) * 8).to_bytes(8, "big")
    blocks = [int.from_bytes(buf[i:i+BLOCK_LEN], "big") for i in range(0, len(buf), BLOCK_LEN)]
    rows = [0] * 128
    for col in range(128):
        result = ghash_with_H(blocks, 1 << col)
        for row in range(128):
            if (result >> row) & 1:
                rows[row] |= (1 << col)
    row_idx = 0
    for col in range(128):
        pivot = None
        for r in range(row_idx, 128):
            if (rows[r] >> col) & 1:
                pivot = r
                break
        if pivot is None:
            continue
        rows[row_idx], rows[pivot] = rows[pivot], rows[row_idx]
        for r in range(128):
            if r != row_idx and ((rows[r] >> col) & 1):
                rows[r] ^= rows[row_idx]
        row_idx += 1
    return row_idx

for length in [8, 16, 24, 32, 40, 48, 56]:
    trials = 100
    count = 0
    for _ in range(trials):
        username = "".join(random.choice(string.ascii_letters + string.digits + "_-") for _ in range(length))
        key = random.randbytes(16)
        if rank_for(username, key) == 128:
            count += 1
    print(f"length {length}: rank128 {count}/{trials}")
