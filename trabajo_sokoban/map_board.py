from PIL import Image
import numpy as np
im = Image.open("screenshot.png")
board = im.crop((260, 200, 516, 456))
w, h = board.size
cells = 16
cell_w = w // cells
cell_h = h // cells
prototypes = {
    "#": np.array([0, 255, 255], dtype=float),
    "#": np.array([0, 128, 128], dtype=float),
    " ": np.array([0, 0, 0], dtype=float),
    "B": np.array([80, 40, 90], dtype=float),
    "P": np.array([50, 80, 0], dtype=float),
    "X": np.array([200, 150, 0], dtype=float)
}
# since dict keys must be unique, handle prototypes separately
labels = [("#", np.array([0,255,255])),
          ("#", np.array([0,128,128])),
          (" ", np.array([0,0,0])),
          ("B", np.array([80,40,90])),
          ("P", np.array([50,80,0])),
          ("X", np.array([200,150,0]))]
for j in range(cells):
    row = ""
    for i in range(cells):
        cell = board.crop((i*cell_w, j*cell_h, (i+1)*cell_w, (j+1)*cell_h))
        avg = np.array(cell).reshape(-1,3).mean(axis=0)
        best_label = None
        best_dist = float("inf")
        for label, ref in labels:
            dist = np.linalg.norm(avg - ref)
            if dist < best_dist:
                best_dist = dist
                best_label = label
        row += best_label
    print(row)
