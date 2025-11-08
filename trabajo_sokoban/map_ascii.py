from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
im = Image.open('screenshot.png')
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
labels = km.labels_.reshape(cells, cells)
centers = km.cluster_centers_
# decide mapping based on center colors
mapping = {}
for idx, (r, g, b) in enumerate(centers):
    if g > 200 and b > 200:
        mapping[idx] = '#'
    elif g > 100 and b > 100:
        mapping[idx] = 'x'
    elif g > 40 and b < 10:
        mapping[idx] = 'P'
    elif r > 40 and b > 40:
        mapping[idx] = 'B'
    else:
        mapping[idx] = ' '
for row in labels:
    print(''.join(mapping[idx] for idx in row))
