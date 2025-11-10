from recover_flag import run_wine, ADDRESSES
err_pw = bytes([105,7,1,31,39,111,45,53,75,105,59,49,105,27,79,56,17,79,1,79,30,56,75,79,1,98,46,98,53,105,11,1,98,11,105,7,1,56,17,113])
records = run_wine(err_pw + b'\n')
seqs = []
current = []
addr_idx = 0
for ret, val in records:
    current.append(val)
    if addr_idx < len(ADDRESSES) and ret == ADDRESSES[addr_idx]:
        seqs.append(current)
        current = []
        addr_idx += 1
        if addr_idx >= len(ADDRESSES):
            break
for idx, seq in enumerate(seqs):
    s = sum(seq)
    r = s % 126
    print(idx, len(seq), s, r)
    print(seq)
