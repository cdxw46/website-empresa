sums = [609,1897,9955,6331,1929,4521,14787]
target = '247CTF{'
for sum_val, ch in zip(sums, target):
    desired = ord(ch)
    remainder = sum_val % 126
    diff_mod = (remainder - desired) % 126
    correction = sum_val - diff_mod
    print(ch, 'sum', sum_val, 'rem', remainder, 'desired', desired, 'diff', diff_mod)
