import numpy as np
import cv2

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('mainlogo.png')


add = img1 + img3
add = cv2.add(img1, img3)
weighted = cv2.addWeighted(img1, 0.6, img3, 0.4, 0)
rows, cols, channel = img3.shape
roi = img1[0:rows, 0:cols]
img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)
img1_bgd = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fgd = cv2.bitwise_and(img3, img3, mask=mask)
dst = cv2.add(img1_bgd, img3_fgd)

img1[0:rows, 0:cols] = dst

cv2.imshow('image1', img1)
cv2.imshow('image3', img3)
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('fore', img1_bgd)
cv2.imshow('back', img3_fgd)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
