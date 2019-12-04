'''import cv2 as cv
import numpy as  np

img = cv.imread(r'coin.png',0)
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
cv.destroyAllWindows()'''


import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(r'C:\Users\manht\PycharmProjects\opencv\img_opencv\count4.jpg',1)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
for r, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * r
    y0 = b * r
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
plt.imshow(img)
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv,cv2

# read the image
image = cv.imread(r'C:\Users\manht\PycharmProjects\opencv\img_opencv\count4.jpg',1)

# convert to grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# perform edge detection
edges = cv2.Canny(grayscale, 30, 100)

# detect lines in the image using hough lines technique
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)

# iterate over the output lines and draw them
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(image, (x1, y1), (x2, y2), (20, 220, 20), 3)

# show the image
plt.imshow(image)
plt.show()
'''