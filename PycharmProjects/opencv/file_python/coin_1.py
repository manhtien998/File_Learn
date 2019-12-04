import cv2 as cv
import numpy as  np

img = cv.imread(r'C:\Users\manht\PycharmProjects\opencv\img_opencv\count4.jpg',1)

img_GaussianBlur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)

#img_rgb = cv.cvtColor(img_GaussianBlur, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img_GaussianBlur, cv.COLOR_RGB2GRAY)
img_bw = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 1)
img_medianBlur = cv.medianBlur(img_bw, 5)
#blur = cv.bilateralFilter(img_medianBlur,9,5,5)
#cv.imshow('blur',img_medianBlur)
#cv.imshow('img_bw',img_bw)
kenel = np.ones((2,2),np.uint8)
img_erode= cv.erode(img_medianBlur,kenel,iterations=1)
img_dilate= cv.dilate(img_erode,kenel,iterations=1)
#cv.imshow('img_dilate',img_dilate)

ret, thresh = cv.threshold(img_erode,127, 255, 0)
im2, contours, hierarchy = cv.findContours(img_dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#img_drawContours =cv.drawContours(img, contours, -1, (255,255,0), 2)
img_drawContours = cv.drawContours(img, contours, -1, (0, 255, 0), 1)
hinhtron = []
hinhtamgiac=[]
hinhvuong=[]
for contour in contours:
    shape = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    if len(shape) >10 and len(shape) <13:
        hinhtron.append(shape)
    elif len(shape) == 3:
        img_drawContours = cv.drawContours(img, contours, -1, (255,255,0), 2)
        hinhtamgiac.append(shape)
    elif len(shape) == 4 :
        img_drawContours = cv.drawContours(img, contours, 3, (0,255,255), 3)
        hinhvuong.append(shape)
cv.imshow('img_drawContours',img_drawContours)
print('hinh tron ',str(len(hinhtron)))
print(' hinh vuong  ',str(len(hinhvuong)))
print(' hinh tam giac  ', str(len(hinhtamgiac)))
cv.imshow('img_drawContours',img_drawContours)
cv.waitKey(0)
cv.destroyAllWindows()
