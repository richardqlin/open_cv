import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/Richard/Downloads/sanfrancisco.jpg')

cv2.imshow('Cats', img) # This shows the image in a window named Image title with the img image 

##plt.imshow(img)
##plt.show()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

#BGR to HSV

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('Hsv',hsv)

# HSV to BGR

hsv_bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

cv2.imshow('hsv --> bgr',hsv_bgr)

hsv_lab = cv2.cvtColor(hsv,cv2.COLOR_LAB2BGR)

cv2.imshow('lab --> bgr',hsv_lab)


lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)

cv2.imshow('Label', lab)

# BGR TO RGB

rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(rgb)
plt.show()

##
##canny = cv2.Canny(img,125,175)
##cv2.imshow('Canny Edges',canny)
##
##
##ret, thresh = cv2.threshold(canny,125, 255, cv2.THRESH_BINARY)
##cv2.imshow('Thresh',thresh)
##_,contours, hierachies = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
##
##print(f'{len(contours)} contour(s) found!')
##
##cv2.drawContours(blank, contours,-1,(0,0,255),1)
##
##cv2.imshow('Contours Drawn',blank)
##    
cv2.waitKey() # This waits until a key is pressed 
cv2.destroyAllWindows()
