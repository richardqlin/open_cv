import cv2
import numpy as np

img = cv2.imread('C:/Users/Richard/Downloads/cats.jpg')

cv2.imshow('Cats', img) # This shows the image in a window named Image title with the img image 

average = cv2.blur(img,(3,3))

cv2.imshow('Average Blue',average)

gauss = cv2.GaussianBlur(img,(3,3),0)
cv2.imshow("Gaussian Blur",gauss)

# median blue

median = cv2.medianBlur(img,3)

cv2.imshow('Median Blue',median)

bilateral = cv2.bilateralFilter(img,10,35,25)
cv2.imshow('Bilateral Blue',bilateral)
 
cv2.waitKey() # This waits until a key is pressed 
cv2.destroyAllWindows()
