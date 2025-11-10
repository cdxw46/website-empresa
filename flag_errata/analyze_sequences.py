from recover_flag import run_wine, ADDRESSES
prefix = bytearray()
seqs = []
for idx in range(10):
    input_bytes = bytes(prefix) + b'A\n'
    records = run_wine(input_bytes)
    block = []
    for ret, val in records:
        block.append((ret, val))
        if ret == ADDRESSES[len(prefix)]:
            break
    vals = [v for _, v in block]
    seqs.append(vals)
    remainder = sum(vals) % 126
    prefix.append(remainder)
print('prefix bytes', prefix)
print('num seqs', len(seqs))
for i, vals in enumerate(seqs):
    print(i, vals)
