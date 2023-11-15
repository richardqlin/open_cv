import cv2
import numpy as np

img = cv2.imread('C:/Users/Richard/Downloads/cats.jpg')
cv2.imshow('Cats', img) # This shows the image in a window named Image title with the img image 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow('Blank',blank)
##
##blur = cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
##cv2.imshow('Blur',blur)
canny = cv2.Canny(img,125,175)
cv2.imshow('Canny Edges',canny)

ret, thresh = cv2.threshold(canny,125, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresh',thresh)
contours, hierachies = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contour(s) found!')

cv2.drawContours(blank, contours,-1,(0,0,255),1)

cv2.imshow('Contours Drawn',blank)
    
cv2.waitKey() # This waits until a key is pressed
cv2.destroyAllWindows()
