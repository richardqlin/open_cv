import cv2
import numpy as np

import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/Richard/Downloads/cat1.jpg')

cv2.imshow('Cats', img) # This shows the image in a window named Image title with the img image 


blank = np.zeros(img.shape[:2], dtype = 'uint8')

##gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##
##cv2.imshow('Gray',gray)
##
mask = cv2.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow('Mask',masked)
##
##gray_hist = cv2.calcHist([gray],[0],mask,[256],[0,256])
##
##plt.figure()
##plt.title('Grayscale Historgram')
##plt.xlabel('Bins')
##plt.ylabel('# of pixels')
##plt.plot(gray_hist)
##plt.xlim([0,256])
##plt.show()

# Color Historgram

plt.figure()
plt.title('Grayscale Historgram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')


colors = ('b','g','r')

for i, col in enumerate(colors):
    hist = cv2.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()
    

cv2.waitKey() # This waits until a key is pressed 
cv2.destroyAllWindows()
