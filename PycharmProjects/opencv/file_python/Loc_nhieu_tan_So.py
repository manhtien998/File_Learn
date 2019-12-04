import cv2 as cv
import numpy as np
import matlab
img = cv.imread(r'count2.tif')
img_medianBlur = cv.medianBlur(img, 3)
img_BINARY = cv.adaptiveThreshold(img_medianBlur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1)
kenel = np.ones((11,11))
a= cv.erode(img_BINARY,kenel,iterations=2)
img_dilate= cv.dilate(a,kenel,iterations=1)
contours = img_dilate.copy()
cv.drawContours(img_dilate, contours,(5,255,5), 3)
cv.imshow('img_medianBlur',img_medianBlur)
cv.imshow('img_BINARY',img_BINARY)
cv.imshow('ing_dilate',img_dilate)

cv.waitKey(0)
cv.destroyAllWindows


