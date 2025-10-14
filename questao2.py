import skimage
import skimage.io
import matplotlib.pyplot as plt
import numpy as np
import skimage.morphology

def center(i, j):
    return i-2 >= 0 and i+2 < 720 and j-2 >= 0 and j + 2 < 1280

image = skimage.io.imread("./photo.jpg")
imageUsed = image.astype(np.float64)
imageMean = np.zeros_like(imageUsed)

for i in range(720):
    for j in range(1280):
        if center(i, j):

            block = imageUsed[i-2:i+3, j-2:j+3]
                      
            imageMean[i, j] = block.mean(axis=(0, 1))
        else:
            imageMean[i, j] = image[i, j]
            
imageMean = np.clip(imageMean, 0, 255).astype(np.uint8)

plt.imshow(imageMean)
plt.show()