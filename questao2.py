import skimage
import skimage.io
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft2, ifft2, fftshift, ifftshift

def center(i, j):
    return i-2 >= 0 and i+2 < 720 and j-2 >= 0 and j + 2 < 1280

def gaussianPassaBaixa(img, freqCorte):

    r = 720
    c = 1280

    centrR, centrC = r // 2, c // 2

    y, x = np.ogrid[:r, :c]

    dist = np.sqrt((y-centrR)**2 + (x-centrC)**2)

    mask = np.exp(-(dist**2) / (2*(freqCorte**2)))

    filterApply = np.zeros_like(img)

    for i in range(3):
        fftApply = fft2(img[...,i])
        fftSApply = fftshift(fftApply)
        maskApply = fftSApply * mask
        
        filterApply[..., i] = np.abs(ifft2(ifftshift(maskApply)))

    return filterApply

def errQuadMed(imgBase, imgTest):
    return np.mean((imgBase.astype(np.float64) - imgTest.astype(np.float64)) ** 2)
 
image = skimage.io.imread("./photo.jpg")
image = image.astype(np.float64)
imageMean = np.zeros_like(image)

for i in range(720):
    for j in range(1280):
        if center(i, j):

            block = image[i-2:i+3, j-2:j+3]
                      
            imageMean[i, j] = block.mean(axis=(0, 1))
        else:
            imageMean[i, j] = image[i, j]
            
imageMean = np.clip(imageMean, 0, 255).astype(np.uint8)

plt.imshow(imageMean)
plt.show()

ans, ansAux = 0, (int)(1e9+1)

for fc in range(1, 500):

    imgTest = gaussianPassaBaixa(image, fc)
    imgTest = np.clip(imgTest, 0, 255).astype(np.uint8)
    eqmHip = errQuadMed(imageMean, imgTest)

    if eqmHip < ansAux:
        ans = fc
        ansAux = eqmHip

print(ans, end=" - > ")
imgAns = gaussianPassaBaixa(image, ans)
imgAns = np.clip(imgAns, 0, 255).astype(np.uint8)
print(errQuadMed(imageMean, imgAns))
plt.imshow(imgAns)
plt.show()