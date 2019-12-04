import cv2 as cv,cv2
import numpy as np
font = cv2.FONT_HERSHEY_COMPLEX

img = cv.imread(r'C:\Users\manht\PycharmProjects\opencv\img_opencv\count3.jpg', cv2.IMREAD_GRAYSCALE)
#img = cv2.imread("image/shapes23.png", cv2.IMREAD_GRAYSCALE)
img_medianBlur = cv.medianBlur(img, 5)
#img_GaussianBlur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
_, threshold = cv2.threshold(img_medianBlur, 200, 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

tron =[]
vuong = []
tamgiac = []
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.019*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "3canh", (x, y), font, 1,0)
        #img_drawContours = cv.drawContours(img, [approx], -1, (255, 255, 0), 2)
        tamgiac.append(cnt)
    elif len(approx) == 4:
        #cv2.putText(img, "vuong", (x, y), font, 1, (0))
        #img_drawContours = cv.drawContours(img, [approx], -1, (255, 255, 0), 2)
        vuong.append(cnt)
    elif len(approx) == 5:
        cv2.putText(img, "5C", (x, y), font, 1, (0))
    elif 6 < len(approx) < 15:
        cv2.putText(img, "elise", (x, y), font, 1, (0))
    else:
        cv2.putText(img, "tron", (x, y), font, 1, (0))
print('3 canh ',len(tamgiac))
print('tron ',len(tron))
cv2.imshow("Shapes", img)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

