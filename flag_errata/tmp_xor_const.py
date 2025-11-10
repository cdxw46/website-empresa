vals = [105,7,1,31,39,111,45,53,75,105,59,49,105,27,79,56,17,79,1,79,30,56,75,79,1,98,46,98,53,105,11,1,98,11,105,7,1,56,17,113]
for k in range(128):
    trans = [v ^ k for v in vals]
    s = ''.join(chr(t) if 32 <= t < 127 else '.' for t in trans)
    if 'CTF' in s:
        print(k, s)
