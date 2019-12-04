
import numpy as np
import cv2 as cv,cv2

image = cv.imread(r'C:\Users\manht\PycharmProjects\opencv\img_opencv\count3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imshow("Gray", gray)
edged = cv2.Canny(gray, 5, 250)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
im2, cnts, hierarchy = cv.findContours(closed.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
total = 0
total_cricle = 0
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.015 * peri, True)
    '''if len(approx) == 4:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 1)
        total += 1'''
    if len(approx) >15 and len(approx)< 17:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 1)
        total_cricle += 1
cv2.imshow("Edged", closed)
print ("I found {0} books in that image 4 canh".format(total))
print ("I found {0} books in that image cricle".format(total_cricle))

cv2.imshow("Output", image)
cv2.waitKey(0)