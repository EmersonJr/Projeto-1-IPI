import skimage
import skimage.io
import matplotlib.pyplot as plt
import numpy as np

image = skimage.io.imread('./photo.jpg')
plt.imshow(image)
plt.axis('off')
plt.show()
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def outbound(i, j):
    return (i >= 720 or i < 0 or j >= 1280 or j < 0)
def meanPixels(pixels):
    # pixToCalc = np.array(pixels, dtype=np.uint16)
    return np.mean(np.array(pixels), dtype=int, axis=0)

newImg = []

for j in range(720):
    newLin = []
    for i in range(1280):
        if i % 2 == 0:
            newLin.append(image[j, i])
    newImg.append(newLin)

newImg1 = []
# print(len(newImg[0]))

for i in range(len(newImg[0])):
    newCol = []
    for j in range(720):
        if j % 2 == 0:
            newCol.append(newImg[j][i])
    newImg1.append(np.array(newCol))

newImg1 = np.array(newImg1)
newImg1 = newImg1.transpose((1, 0, 2))
plt.imshow(newImg1)
plt.axis('off')
plt.show()

imgOr = skimage.io.imread('./photo.jpg')

imageMid = []
newImg1.tolist()
for i in range(len(newImg1)):
    newCol = []
    for j in range(len(newImg1[i])):
        newCol.append(newImg1[i][j])
        if j + 1 < len(newImg1[i]):

            toCalc = np.array([newImg1[i][j], newImg1[i][j+1]], dtype=np.uint16) 
            avg = (toCalc.sum(axis=0) // 2).astype(np.uint8)
            newCol.append(avg)
        else:
            newCol.append(newImg1[i][-1])
    
    imageMid.append(np.array(newCol, dtype=np.uint8))

imageMid = np.array(imageMid)
image = []

for i in range(len(imageMid)):

    image.append(imageMid[i].astype(np.uint8))
    if i + 1 < len(imageMid):

        avg = ((imageMid[i].astype(np.uint16) + imageMid[i + 1].astype(np.uint16)) // 2).astype(np.uint8)
        image.append(avg)
    else:
        image.append(imageMid[i])
    
image = np.array(image, dtype=np.uint8)
# print(len(imageMid[0]))
plt.imshow(image)
plt.axis('off')
plt.show()

errQuadMed = ((image.astype(np.float64) - imgOr.astype(np.float64)) ** 2).mean()

print(errQuadMed)