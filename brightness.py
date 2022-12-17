import numpy as np
import cv2

img = cv2.imread('singa.jpg',0)
cv2.imshow('Gambar Asli',img)

img2 = np.ones((183,275,1),np.uint8)*255
img3 = np.ones((183,275,1),np.uint8)*255

ukuran = img.shape
for i in range(ukuran[0]):
    for j in range(ukuran[1]):
        pix = img[i,j] + 60
        if(pix<=255):
            pix=255
        img2[i,j] = pix
        img3[i,j]=img[i,j]-img2[i,j]

cv2.imshow('Gambar Hasil Brightness',img2)
cv2.imshow('Asli dikurangi Hasil Brightness',img3)

cv2.waitKey()