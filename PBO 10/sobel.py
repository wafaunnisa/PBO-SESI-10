import imageio as img
import numpy as np
import matplotlib.pyplot as plt

image = img.imread("C:/Users/ACER/Downloads/cartoon.jpg",mode='F')

sobelX = np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
])

sobelY = np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]
])

imgPad = np.pad(image,pad_width=1,mode='constant', constant_values=0)

Gx = np.zeros_like(image)
Gy = np.zeros_like(image)

for y in range(1,imgPad.shape[0]-1):
    for x in range(1,imgPad.shape[1]-1):
        region = imgPad[y-1:y+2,x-1:x+2]
        Gx[y-1,x-1] = (region * sobelX).sum()
        Gy[y-1,x-1] = (region * sobelY).sum()

G = np.sqrt(Gx**2 + Gy**2)
G = (G/G.max()) * 255
G = np.clip(G,0,255)
G = G.astype(np.uint8)

plt.figure(figsize=(6,6))
plt.subplot(1,3,1)
plt.imshow(Gx, cmap='gray')

plt.subplot(1,3,2)
plt.imshow(Gy, cmap='gray')

plt.subplot(1,3,3)
plt.imshow(G, cmap='gray')

plt.tight_layout()
plt.show()