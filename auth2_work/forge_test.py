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


def build_blocks(ct):
    pad_len = (BLOCK_LEN - len(ct) % BLOCK_LEN) % BLOCK_LEN
    buf = ct + b"\x00" * pad_len + (0).to_bytes(8, "big") + (len(ct) * 8).to_bytes(8, "big")
    return [int.from_bytes(buf[i:i+BLOCK_LEN], "big") for i in range(0, len(buf), BLOCK_LEN)]


def solve_H(blocks, S):
    rows = [0] * 128
    for col in range(128):
        basis = 1 << col
        result = ghash_with_H(blocks, basis)
        for row in range(128):
            if (result >> row) & 1:
                rows[row] |= (1 << col)
    rhs = [(S >> row) & 1 for row in range(128)]
    pivot_cols = [-1] * 128
    row = 0
    for col in range(128):
        pivot = None
        for r in range(row, 128):
            if (rows[r] >> col) & 1:
                pivot = r
                break
        if pivot is None:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        rhs[row], rhs[pivot] = rhs[pivot], rhs[row]
        pivot_cols[row] = col
        for r in range(128):
            if r != row and ((rows[r] >> col) & 1):
                rows[r] ^= rows[row]
                rhs[r] ^= rhs[row]
        row += 1
    if row < 128:
        return None
    H = 0
    for r in range(128):
        col = pivot_cols[r]
        if col == -1:
            continue
        if rhs[r] & 1:
            H |= (1 << col)
    return H


def forge_once():
    key = random.randbytes(16)
    username = .join(random.choice(string.ascii_lowercase) for _ in range(40))
    G = GCM(key, IV)
    guest_plain = json.dumps({username: username, role: guest}).encode()
    ct_bytes, tag_bytes = G.encrypt(guest_plain)
    keystream = bytes(c ^ p for c, p in zip(ct_bytes, guest_plain))
    ks_block = keystream[:BLOCK_LEN]
    S = int.from_bytes(tag_bytes, big) ^ int.from_bytes(ks_block, big)
    blocks = build_blocks(ct_bytes)
    H = solve_H(blocks, S)
    if H is None:
        return False
    target_username = username[:-6]
    admin_plain = json.dumps({username: target_username, role: super_admin}).encode()
    if len(admin_plain) != len(guest_plain):
        return False
    ct_new = bytes(k ^ p for k, p in zip(keystream, admin_plain))
    blocks_new = build_blocks(ct_new)
    S_new = ghash_with_H(blocks_new, H)
    tag_new = (S_new ^ int.from_bytes(ks_block, big)).to_bytes(BLOCK_LEN, big)
    pt_check, auth = G.decrypt(ct_new, tag_new)
    if not auth:
        return False
    data = json.loads(pt_check.decode())
    return data.get(role) == super_admin

success = 0
trials = 20
for _ in range(trials):
    if forge_once():
        success += 1
print(fsuccess
