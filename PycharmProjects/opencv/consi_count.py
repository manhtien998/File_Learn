import cv2 as cv
import numpy as  np

img = cv.imread(r'Count3.png',0)
img_medianBlur = cv.medianBlur(img, 5)
img_BINARY = cv.adaptiveThreshold(img_medianBlur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 129, 1)
kenel = np.ones((2,2))
a= cv.erode(img_BINARY,kenel,iterations=2)
img_dilate= cv.dilate(a,kenel,iterations=1)
cv.imshow('img_dilate',img_dilate)
ret, thresh = cv.threshold(img_dilate, 50, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
img_drawContours = cv.drawContours(img, contours, -1, (0,255,0), 2)
print(contours)
hinhtron = []
for contour in contours:
    shape = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    if len(shape) > 5:
        hinhtron.append(shape)
print(str(len(hinhtron)))
cv.waitKey(0)
cv.destroyAllWindows()