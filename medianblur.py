import cv2 as cv
img = cv.imread('singa.jpg')
blur = cv.medianBlur(img,5)
blurlebih = cv.medianBlur(img,9)
cv.imshow('original', img)
cv.imshow('blur',blur)
cv.imshow('blurlebih',blurlebih)
cv.waitKey(0)