import cv2 as cv,cv2
import numpy as np


image = cv.imread(r'C:\Users\manht\PycharmProjects\opencv\img_opencv\count3.jpg',1)

hsv = cv2.cvtColor(image ,cv2.COLOR_BGR2HSV)

lower = np.uint8([83, 0, 0])
upper = np.uint8([180, 255, 255])

white_mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=white_mask)
# cv2.imshow('inrange', result)
print(result.shape)
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)
im2, cnts, hierarchy = cv.findContours(gray, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
count = []
for contour in cnts:
    shape = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    cv2.drawContours(image, contour, -1, (0, 255, 0), 3)
    if len(shape) > 5:
        count.append(contour)

a = cv2.drawContours(image, contour, -1, (0, 255, 0), 3)
print(count)
cv.imshow('a',a)
cv2.waitKey(0)
cv.destroyAllWindows()

