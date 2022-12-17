import cv2 as cv
img = cv.imread('singa.jpg')
blur = cv.blur(img,(6,5))
blurlebih = cv.blur(img,(9,9))
cv.imshow('original', img)
cv.imshow('blur',blur)
cv.imshow('blurlebih',blurlebih)
cv.waitKey(0)