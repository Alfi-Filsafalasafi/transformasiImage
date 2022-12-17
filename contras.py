import cv2

img = cv2.imread('singa.jpg', 1)
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l_channel, a, b = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl = clahe.apply(l_channel)
limg = cv2.merge((cl,a,b))

enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

cv2.imshow('Original',img)
cv2.imshow('Hasil', enhanced_img)
cv2.waitKey(0)