vals = [105,7,1,31,39,111,45,53,75,105,59,49,105,27,79,56,17,79,1,79,30,56,75,79,1,98,46,98,53,105,11,1,98,11,105,7,1,56,17,113]
for key_len in range(1,5):
    for key in range(128 ** key_len):
        kbytes = [(key >> (7*i)) & 0x7f for i in range(key_len)]  # limit to 7-bit to reduce search
        trans = []
        for idx, v in enumerate(vals):
            trans.append(v ^ kbytes[idx % key_len])
        s = ''.join(chr(t) if 32 <= t < 127 else '.' for t in trans)
        if s.startswith('247CTF{' ):
            print('key_len', key_len, 'key', kbytes, s)
            raise SystemExit
