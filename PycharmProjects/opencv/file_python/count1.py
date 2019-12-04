import  cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\manht\PycharmProjects\opencv\img_opencv\count4.jpg',0)
img_medianBlur = cv.medianBlur(img, 5)
img_GaussianBlur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
img_BINARY = cv.adaptiveThreshold(img_GaussianBlur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, 1)
kenel = np.ones((2,2),np.uint8)
img_erode= cv.erode(img_BINARY,kenel,iterations=1)
img_dilate= cv.dilate(img_erode,kenel,iterations=1)
for i in range (0,img_dilate.shape[0]):
    for j in range (0,img_dilate.shape[1]):
        img_dilate[i,j] =255- img_dilate[i,j]
ret, thresh = cv.threshold(img_dilate,127, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
img_drawContours =cv.drawContours(img_dilate, contours, -1, (255,255,0), 1)
cv.imshow('img_drawContours',img_drawContours)
hinhtron = []
hinhvuong=[]
for contour in contours:
    shape = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    if len(shape) > 10 :
        hinhtron.append(shape)
    elif len(shape) == 4:
        hinhvuong.append(shape)
print('hinh tron ',str(len(hinhtron)))
print(' hinh vuong  ',str(len(hinhvuong)))
cv.waitKey(0)
cv.destroyAllWindows()


