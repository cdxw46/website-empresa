from PIL import Image
import numpy as np
import subprocess
import os
WINDOW_ID = os.environ.get("WINDOW_ID", "0x1400003")
subprocess.run(["bash","-lc",f"DISPLAY=:99 import -window {WINDOW_ID} window_tmp.png"],check=True)
im = Image.open("window_tmp.png").convert("RGB")
arr = np.array(im)
mask = (arr[:,:,1]>200) & (arr[:,:,0]<50)
rows = np.where(mask.any(axis=1))[0]
cols = np.where(mask.any(axis=0))[0]
row_start,row_end = rows[0],rows[-1]
col_start,col_end = cols[0],cols[-1]
board = im.crop((col_start,row_start,col_end+1,row_end+1))
board.save("board_current.png")
rows_count, cols_count = 16, 16
cell_w = board.width // cols_count
cell_h = board.height // rows_count
mapping_chars = []
for j in range(rows_count):
    row_chars = []
    for i in range(cols_count):
        cell = board.crop((i*cell_w,j*cell_h,(i+1)*cell_w,(j+1)*cell_h))
        avg = np.array(cell).reshape(-1,3).mean(axis=0)
        r,g,b = avg
        if g>220:
            ch = "#"
        elif b>40 and r>20:
            ch = "B"
        elif g>60 and b<20:
            ch = "P"
        elif g>120:
            ch = "x"
        else:
            ch = "."
        row_chars.append(ch)
    mapping_chars.append("".join(row_chars))
for row in mapping_chars:
    print(row)
