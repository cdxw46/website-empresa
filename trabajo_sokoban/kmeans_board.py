from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
im = Image.open("screenshot.png")
board = im.crop((260, 200, 516, 456))
w, h = board.size
cells = 16
cell_w = w // cells
cell_h = h // cells
averages = []
for j in range(cells):
    for i in range(cells):
        cell = board.crop((i * cell_w, j * cell_h, (i + 1) * cell_w, (j + 1) * cell_h))
        avg = np.array(cell).reshape(-1, 3).mean(axis=0)
        averages.append(avg)
averages = np.array(averages)
km = KMeans(n_clusters=5, random_state=0).fit(averages)
centers = km.cluster_centers_
print("centers:")
for idx, center in enumerate(centers):
    print(idx, center)
labels = km.labels_.reshape(cells, cells)
print("labels:")
for row in labels:
    print(" ".join(map(str, row)))
