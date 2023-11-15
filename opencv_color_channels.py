import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/Richard/Downloads/sanfrancisco.jpg')

cv2.imshow('SF', img) # This shows the image in a window named Image title with the img image 

blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv2.split(img)

blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])

cv2.imshow('Blue',blue)
cv2.imshow('Green',green)
cv2.imshow('Red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


merged = cv2.merge((b,g,r))

cv2.imshow('Merge',merged)

cv2.waitKey() # This waits until a key is pressed 
cv2.destroyAllWindows()
