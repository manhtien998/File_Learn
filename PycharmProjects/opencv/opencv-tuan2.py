import cv2 as cv
import numpy as np

def Cong_MaTran():
    img1 = np.array(cv.imread(r'eight_pepper.tif',0))
    img2 = np.array(cv.imread(r'eight_salt.tif',0))
    img_final = img1 + img2
    cv.imshow('img_final',img_final)
    img_final_1_2= img_final - img1 -img2
    cv.imshow('img_final-1-2',img_final_1_2)
    img_final_2 = img_final - img2+ img1
    cv.imshow('img_final-2-1',img_final_2)
    cv.waitKey(0)
    cv.destroyAllWindows()

def Nhan_MaTran():
    cv.imshow('Nhan ma tran', cv.imread(r'car-left.tif',0)*2)
    cv.waitKey(0)
    cv.destroyAllWindows()

def Tang_Sang():
    img_baby=cv.imread(r'baby.png')
    img_baby_HSV=cv.cvtColor(img_baby,cv.COLOR_BGR2HSV)
    cv.imshow('goc',img_baby)
    cv.imshow('baby_HSV',img_baby_HSV[:,:,2]+150)
    cv.waitKey(0)
    cv.destroyAllWindows()

def Ngich_Dao():
    img_boy = np.array(cv.imread(r'boy.tif',0))
    print(img_boy)
    Nghichdao=B = np.linalg.inv(img_boy)
    cv.imshow('nghich dao ma tran ',Nghichdao)
    cv.waitKey(0)
    cv.destroyAllWindows()
def ZOOM(scale_percent):
    img = cv.imread(r'baby.png')
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    cv.imshow("Resized image", resized)
    cv.waitKey(0)
    cv.destroyAllWindows()

def tuongphan_sang():
    cv.imshow('Nhan ma tran', cv.imread(r'car-left.tif',0)*2+100)
    cv.waitKey(0)
    cv.destroyAllWindows()


def xoayanh_Tam(angle):
    image = cv.imread(r'boy.tif')
    center=tuple(np.array(image.shape[0:2])/2)
    rot_mat = cv.getRotationMatrix2D(center,angle,1.0)
    cv.imshow("xoayanh()",cv.warpAffine(image, rot_mat, image.shape[0:2],flags=cv.INTER_LINEAR) )
    cv.waitKey(0)
    cv.destroyAllWindows()


def Tuong_Phan():
    beta = 20
    alpha=1,5
    img = cv.imread(r"salzburg.png", 1)
    dst = cv.imread(r"salzburg.png", 1)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            for k in range(0, 3):
                dst[i, j, k] = alpha * img[i, j, k] + beta
    cv.imshow('after', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


def Tuongphan1():
    img = cv.imread(r"salzburg.png", 0)
    img_full = img.copy()
    maxlest = img.max()
    minlest = img.min()
    for i in range (0,img.shape[0]):
        for j in range (0,img.shape[1]):
            img_full[i,j]= 255*(img[i,j]-minlest)/(maxlest-minlest)
    cv.imshow('1',img_full)
    cv.waitKey(0)
    cv.destroyAllWindows()

def Histogram():
    img = cv.imread(r"pollen_image.tif", 0)
    dst = img.copy()
    cv.equalizeHist(img,dst)
    cv.imshow('dst',dst)
    cv.waitKey()
    cv.destroyAllWindows()

def Loc_nhieu():
    img = cv.imread(r'eight_pepper.tif')
    img1 = cv.imread(r'eight_salt.tif')
    out_1 = cv.add(img,img1)
    blur = cv.GaussianBlur(out_1,(5,5),0)
    pepper_salt=cv.subtract(blur,out_1)
    new = cv.resize()
    cv.imshow('goc',out_1)
    cv.imshow('salt',pepper_salt)
    cv.waitKey(0)
    cv.destroyAllWindows()

def Imcomlement(Img):
    for img_X in range(0, len(Img)):
        for img_Y in range(0, len(Img[0])):
            Img[img_X, img_Y] = 255 - Img[img_X, img_Y]
    return Img


def Loc_pepper():
    img2 = cv.imread(r'eight_pepper.tif', 0)
    img3 = cv.imread(r'eight_salt.tif', 0)
    img = cv.add(img2, img3)
    img1 = cv.medianBlur(img, 5)
    cv.imshow('median', img1)
    cv.waitKey(0)
    cv.destroyAllWindows

