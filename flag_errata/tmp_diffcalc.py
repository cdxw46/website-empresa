from recover_flag import run_wine
records = run_wine(b'A\n')
block = []
for ret, val in records:
    block.append(val)
    if ret == 0x40311b:
        break
seq = block
print('seq', seq)
print('len', len(seq))
print('sum', sum(seq))
print('even sum', sum(seq[::2]))
print('odd sum', sum(seq[1::2]))
print('diff even', sum(seq[::2]) % 126)
print('diff odd', sum(seq[1::2]) % 126)
