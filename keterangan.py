import numpy as np
import cv2
img = cv2.imread('fotoku.jpg',0)
cv2.imshow('Original',img)

print(img)
print("jml pixel citra :")
print(img.size)
print("ukuran shape :")
print(img.shape)
print("tinggi citra :")
print(len(img))
print("lebar citra :")
print(len(img[1]))
print("Nilai pixel pada koordinat(11,21) ")
print(img[11,21])

cv2.waitKey(0)