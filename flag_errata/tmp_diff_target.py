sums = [609,1897,9955,6331,1929,4521,14787,8747,12801,4893,689,11767,4893,10989,9781,13286,647,9781,9955,9781,13890,13286,12801,9781,9955,602,1810,602,8747,4893,641,9955,602,641,4893,1897,9955,13286,647,1499]
target = '247CTF{'
for i, ch in enumerate(target):
    desired = ord(ch)
    current = sums[i] % 126
    diff = (current - desired) % 126
    print(i, ch, current, desired, diff)
