from PIL import Image
import numpy as np
board = Image.open("board.png")
rows, cols = 16, 16
cell_w = board.width // cols
cell_h = board.height // rows
for j in range(rows):
    for i in range(cols):
        cell = board.crop((i*cell_w, j*cell_h, (i+1)*cell_w, (j+1)*cell_h))
        avg = np.array(cell).reshape(-1,3).mean(axis=0)
        print(f"({j},{i}) {avg}")
