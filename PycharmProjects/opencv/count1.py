
import  cv2 as cv,cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread(r'C:\Users\manht\PycharmProjects\opencv\img_opencv\count3.jpg',0)
img_medianBlur = cv.medianBlur(img, 5)
img_GaussianBlur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
img_BINARY = cv.adaptiveThreshold(img_GaussianBlur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, 1)
kenel = np.ones((2,2),np.uint8)
img_erode= cv.erode(img_BINARY,kenel,iterations=1)
img_dilate= cv.dilate(img_erode,kenel,iterations=1)
for i in range (0,img_dilate.shape[0]):
    for j in range (0,img_dilate.shape[1]):
        img_dilate[i,j] =255- img_dilate[i,j]
#img_cany = cv.Canny(img_dilate,1,2)
#cv2.imshow('img_cany',img_cany)
'''ret, thresh = cv.threshold(img_dilate,127, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

hinhtron = []
hinhvuong=[]
hinhtamgiac = []
for contour in contours:
    shape = cv.approxPolyDP(contour, 0.012*cv.arcLength(contour, True), True)
    if len(shape) > 11 and len(shape) <14 :
        hinhtron.append(shape)
        img_drawContours = cv.drawContours(img_dilate, contour, -1, (255, 255, 0), 1)
    elif len(shape) ==5:
        hinhvuong.append(shape)
    elif len(shape) == 3:
        hinhtamgiac.append(shape)
 '''
font = cv2.FONT_HERSHEY_COMPLEX
_, threshold = cv2.threshold(img_dilate, 155, 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

tron =[]
vuong = []
tamgiac = []
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "tam giac", (x, y), font, 1,0)
        img_drawContours = cv.drawContours(img, [approx], -1, (255, 255, 0), 2)
        tamgiac.append(cnt)
'''    elif len(approx) == 4:
        cv2.putText(img, "vuong", (x, y), font, 1, (0))
        img_drawContours = cv.drawContours(img, [approx], -1, (255, 255, 0), 2)
        vuong.append(cnt)
    elif len(approx) == 5:
        cv2.putText(img, "5 canh", (x, y), font, 1, (0))
    elif 6 < len(approx) < 15:
        cv2.putText(img, "elise", (x, y), font, 1, (0))
    else:
        cv2.putText(img, "tron", (x, y), font, 1, (0))'''


print('hinh tron ',str(len(tron)))
print(' hinh vuong  ',str(len(vuong)))
print('hinh tam giac ',str(len(tamgiac)))
cv.imshow('img_drawContours',img_drawContours)
cv2.waitKey(0)
cv2.destroyAllWindows()
