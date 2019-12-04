import cv2 as cv,cv2
import numpy as  np

img = cv.imread(r'C:\Users\manht\PycharmProjects\opencv\img_opencv\count4.jpg',1)


img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY)
img_bw = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 1)
img_medianBlur = cv.medianBlur(img_bw, 5)
img_GaussianBlur = cv.GaussianBlur(img_medianBlur,(5,5),cv.BORDER_DEFAULT)
kenel = np.ones((2,2),np.uint8)
img_erode= cv.erode(img_GaussianBlur,kenel,iterations=1)
img_dilate= cv.dilate(img_erode,kenel,iterations=1)
for i in range (0,img_dilate.shape[0]):
    for j in range (0,img_dilate.shape[1]):
        img_dilate[i,j] =255- img_dilate[i,j]
img_cany = cv.Canny(img_dilate,200,300)
cv2.imshow('img_cany',img_cany)
ret, thresh = cv.threshold(img_cany,127, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
hinhtron = []
hinhvuong=[]
hinhtamgiac = []
for contour in contours:
    shape = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    if len(shape) > 12 and len(shape) <16 :
        hinhtron.append(shape)
        img_drawContours = cv.drawContours(img_cany, contour, -1, (255, 255, 0), 1)
    elif len(shape) ==5:
        hinhvuong.append(shape)
    elif len(shape) == 3:
        hinhtamgiac.append(shape)
print('hinh tron ',str(len(hinhtron)))
print(' hinh vuong  ',str(len(hinhvuong)))
print('hinh tam giac ',str(len(hinhtamgiac)))
cv.imshow('img_drawContours',img_drawContours)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''
img_GaussianBlur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
img_rgb = cv.cvtColor(img_GaussianBlur, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY)
img_bw = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 1)
img_medianBlur = cv.medianBlur(img_bw, 5)
kenel = np.ones((2,2),np.uint8)
img_erode= cv.erode(img_medianBlur,kenel,iterations=1)
img_dilate= cv.dilate(img_erode,kenel,iterations=1)
img_canny = cv.Canny(img_dilate,200,300)
ret, thresh = cv.threshold(img_canny,127, 255, 0)
im2, contours, hierarchy = cv.findContours(img_canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
img_drawContours =cv.drawContours(img, contours, -1, (255,255,0), 2)
hinhtron = []
hinhtamgiac=[]
hinhvuong=[]
for contour in contours:
    shape = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    if len(shape) >12 and len(shape) <15 :
        hinhtron.append(shape)
        print(contour,'hinhtron')
#        img_drawContours = cv.drawContours(img, contour, -1, (0, 255, 0), 3)
    elif len(shape) == 3:
        #img_drawContours = cv.drawContours(img, contour, -1, (255,255,0), 3)
        hinhtamgiac.append(shape)
    elif len(shape) == 4 :
        #img_drawContours = cv.drawContours(img, contour, -1, (255,0,255), 3)
        hinhvuong.append(shape)
cv.imshow('img_drawContours',img_drawContours)
print('hinh tron ',str(len(hinhtron)))
print(' hinh vuong  ',str(len(hinhvuong)))
print(' hinh tam giac  ', str(len(hinhtamgiac)))
cv.waitKey(0)
cv.destroyAllWindows()
'''