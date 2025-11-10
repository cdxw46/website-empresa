vals = [105,7,1,31,39,111,45,53,75,105,59,49,105,27,79,56,17,79,1,79,30,56,75,79,1,98,46,98,53,105,11,1,98,11,105,7,1,56,17,113]
diff_xor = [vals[0]] + [vals[i] ^ vals[i-1] for i in range(1, len(vals))]
diff_sub = [vals[0]] + [(vals[i] - vals[i-1]) % 128 for i in range(1, len(vals))]
print('XOR diff:', ''.join(chr(v) if 32 <= v < 127 else '.' for v in diff_xor))
print('SUB diff:', ''.join(chr(v) if 32 <= v < 127 else '.' for v in diff_sub))
