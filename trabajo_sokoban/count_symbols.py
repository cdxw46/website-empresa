from collections import Counter
with open("board_ascii.txt") as f:
    grid = "".join(line.strip() for line in f if line.strip())
print(Counter(grid))
