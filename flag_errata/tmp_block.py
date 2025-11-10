from recover_flag import run_wine
records = run_wine(b'A\n')
block = []
for ret, val in records:
    block.append((ret, val))
    if ret == 0x40311b:
        break
print('len', len(block))
vals = [val for _, val in block]
print(vals)
print('sum', sum(vals), 'last', vals[-1])
print('sum+last', sum(vals)+vals[-1])
print('sum%126', sum(vals) % 126)
print('(sum+last)%126', (sum(vals)+vals[-1]) % 126)
