vals = [105,7,1,31,39,111,45,53,75,105,59,49,105,27,79,56,17,79,1,79,30,56,75,79,1,98,46,98,53,105,11,1,98,11,105,7,1,56,17,113]
print(len(vals))
orig = ''.join(chr(v) if 32 <= v < 127 else '.' for v in vals)
print('Original:', orig)
for k in range(1,128):
    trans_xor = [v ^ k for v in vals]
    if all(32 <= t < 127 for t in trans_xor):
        print('XOR', k, ''.join(chr(t) for t in trans_xor))
    trans_add = [(v + k) % 128 for v in vals]
    if all(32 <= t < 127 for t in trans_add):
        print('ADD', k, ''.join(chr(t) for t in trans_add))
