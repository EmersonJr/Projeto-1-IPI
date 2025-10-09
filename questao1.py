import skimage
import skimage.io
import matplotlib.pyplot as plt
import numpy as np

image = skimage.io.imread('./photo.jpg')

x=0

for i in range(1280):
    for j in range(720):
        if j % 2 == 1:
            image[j, i] = 0

for j in range(720):
    for i in range(1280):
        if i % 2 == 1:
            image[j, i] = 0

plt.imshow(image)
plt.show()

