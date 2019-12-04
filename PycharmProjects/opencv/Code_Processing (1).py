'''
import numpy as np
import cv2 as cv

img = cv.imread('image/count4.jpg')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 255, 0)
_, contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

print("First -> Number of contours = " + str(len(contours)))
# print(contours[0])

cv.drawContours(img, contours, -1, (0, 255, 0), 3)
cv.imshow('Image_1', img)

list_contours = []
for contour in contours:
    shape = cv.approxPolyDP(contour, 0.15 * cv.arcLength(contour, True), True)
    # cv.drawContours(img, [shape], 0, (0), 5)
    if len(shape) == 3:
        list_contours.append(shape)

print("Second -> Number of Contours found = " + str(len(list_contours)))
cv.drawContours(img, list_contours, -1, (0, 255, 0), 3)
cv.drawContours(imgray, list_contours, -1, (0, 255, 0), 3)

cv.imshow('Image_2', img)
cv.imshow('Image GRAY', imgray)
cv.waitKey(0)
cv.destroyAllWindows()
'''

import cv2 as cv,cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX

img = cv.imread(r'C:\Users\manht\PycharmProjects\opencv\img_opencv\count3.jpg', cv2.IMREAD_GRAYSCALE)
img_copy = img.copy()

# img_bw = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 129, 1)
# edged = cv2.Canny(img_bw, 30, 200)
# _, contours, _ = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 3)
cv2.imshow("Shapes_First", img_copy)

dict_shape = {"Triangle": [], "Rectangle": [], "Pentagon": [], "Ellipse": [], "Circle": []}

# Triangle = 110 and 0.009
# Rectangle = 127 and 0.01
# Pentagon =

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.015 * cv2.arcLength(cnt, True), True)
    # x = approx.ravel()[0]
    # y = approx.ravel()[1]
    if len(approx) == 3:
        dict_shape["Triangle"].append(approx)
    elif len(approx) == 4:
        dict_shape["Rectangle"].append(approx)
    elif len(approx) == 5:
        dict_shape["Pentagon"].append(approx)
    elif 6 < len(approx) < 15:
        dict_shape["Ellipse"].append(approx)
    else:
        dict_shape["Circle"].append(approx)

print("-> Number of Contours found = " + str(len(dict_shape["Ellipse"])))
cv2.drawContours(img, dict_shape["Ellipse"], -1, (0, 255, 0), 3)

cv2.imshow("Threshold", threshold)
cv2.imshow("Shapes_Second", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
