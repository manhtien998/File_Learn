
import cv2 as cv,cv2
import matplotlib
import matplotlib.pyplot as plt
import time

def convertToRGB(img):
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)

test1 = cv.imread(r'data/download.jpg',1)
cv.imshow('test1',test1)
gray_img = cv.cvtColor(test1, cv.COLOR_BGR2GRAY)
plt.imshow(gray_img, cmap='gray')

haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

faces =  cv.CascadeClassifier.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);


print('Faces found: ', len(faces))
cv.waitKey(0)
cv.destroyAllWindows()