import skimage
import skimage.io
import matplotlib.pyplot as plt
import numpy as np

image = skimage.io.imread('./photo.jpg')
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def outbound(i, j):
    return (i >= 720 or i < 0 or j >= 1280 or j < 0) 
for j in range(720):
    for i in range(1280):
        if i % 2:
            image[j, i] = 0

for i in range(1280):
    for j in range(720):
        if j % 2:
            image[j, i] = 0


plt.imshow(image)
plt.show()

imgOr = skimage.io.imread('./photo.jpg')

for i in range(720):
    for j in range(1280):
        if j % 2:
            accum = 0
            for z in range(2):
                addi = dirs[z][0]
                addj = dirs[z][1]

                newi = i + addi
                newj = addj + j

                if outbound(newi, newj):

                    if not addi:
                        newj = j - addj
                    else:
                        newi = i - addi

                accum += imgOr[newi, newj]
            
            image[i, j] = accum // 4

for j in range(1280):
    for i in range(720):
        if i % 2:
            accum = 0
            for z in range(2, 4):
                addi = dirs[z][0]
                addj = dirs[z][1]
                newi = i + addi
                newj = addj + j

                if outbound(newi, newj):

                    if not addi:
                        newj = j - addj
                    else:
                        newi = i - addi
                
                accum += imgOr[newi, newj]
            
            image[i, j] = accum // 4

plt.imshow(image)
plt.show()

errQuadMed = 0

for i in range(720):
    for j in range(1280):

        errQuadMed += (image[i, j] - imgOr[i, j]) * (image[i, j] - imgOr[i, j])

errQuadMed = errQuadMed / (720.0*1280.0)

print(errQuadMed)