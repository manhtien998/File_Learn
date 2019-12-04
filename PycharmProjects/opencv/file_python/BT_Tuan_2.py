import cv2 as cv


img1 = cv.imread(r'eight_pepper.tif',0)
img2 = cv.imread(r'eight_salt.tif',0)
baby = cv.imread("baby.png",0)
blend_add = cv.imread("blend_add.tif", 0)
eight_tract = img1 +img2
#cv.imshow('eight_saft',eight_tract)
sub_tract = img1- img2
#cv.imshow("sub_tract",sub_tract)
for i in range (0,sub_tract.shape[0]):
    for j in range (0,sub_tract.shape[1]):
        sub_tract[i,j] =255- sub_tract[i,j]
baby_blend = cv.add(cv.resize(baby,(200, 200)), cv.resize(blend_add,(200, 200)))
#cv.imshow('baby_blend',baby_blend)
resized_pepper_saft = cv.resize(sub_tract,(200, 200))
Final_image = resized_pepper_saft + baby_blend
cv.imshow('FULL_sub_tract', sub_tract)
#cv.imshow('full1_Final_image',Final_image)
cv.waitKey(0)
cv.destroyAllWindows()


