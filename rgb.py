from PIL import Image
import numpy as np
import cv2

im = np.array(Image.open('singa.jpg'))

im_R =im.copy()
im_R[:,:,(1,2)] = 0
im_G =im.copy()
im_G[:,:,(0,2)] = 0
im_B =im.copy()
im_B[:,:,(0,1)] = 0

im_RGB = np.concatenate((im_R, im_G, im_B), axis =1)

pil_img = Image.fromarray(im_RGB)

cv2.imshow('hasil',pil_img)

cv2.waitKey(0)