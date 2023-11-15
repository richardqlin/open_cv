import cv2
import numpy as np

import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/Richard/Downloads/sanfrancisco.jpg')

cv2.imshow('San Francisco', img) # This shows the image in a window named Image title with the img image


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray',gray)

# Laplacian

lap = cv2.Laplacian(gray,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian',lap)


sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0)
sobely = cv2.Sobel(gray,cv2.CV_64F,0,1)
combined_sobel = cv2.bitwise_or(sobelx, sobely)


cv2.imshow('Sobel x',sobelx)

cv2.imshow('Sobel y',sobely)
cv2.imshow('Conbined Sobel', combined_sobel)

canny = cv2.Canny(gray,150,175)
cv2.imshow('Canny',canny)

cv2.waitKey() # This waits until a key is pressed 
cv2.destroyAllWindows()
