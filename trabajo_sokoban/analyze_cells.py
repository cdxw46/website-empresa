from PIL import Image
import numpy as np
im = Image.open("screenshot.png")
board = im.crop((260, 200, 516, 456))
w, h = board.size
cells = 16
cell_w = w // cells
cell_h = h // cells
for j in range(cells):
    for i in range(cells):
        cell = board.crop((i * cell_w, j * cell_h, (i + 1) * cell_w, (j + 1) * cell_h))
        arr = np.array(cell)
        avg = arr.reshape(-1, 3).mean(axis=0)
        print(f"({j},{i}) {avg}")
    print("-" * 20)
