import cv2
import numpy as np

img = cv2.imread('C:/Users/Richard/Downloads/cats.jpg')

cv2.imshow('Cats', img) # This shows the image in a window named Image title with the img image 

blank = np.zeros(img.shape[:2],dtype='uint8')

cv2.imshow('Blank Image',blank)

mask = cv2.rectangle(blank,(img.shape[1]//4,img.shape[0]//4),(img.shape[1]//4+200,img.shape[0]//4+200),100,255,-1)

cv2.imshow('Mask',mask)

masked = cv2.bitwise_and(img,img,mask= mask)

cv2.imshow('Mask Image',masked)


cv2.waitKey() # This waits until a key is pressed 
cv2.destroyAllWindows()
