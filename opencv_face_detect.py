import cv2
import numpy as np

import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/Richard/Downloads/people-1.png')

cv2.imshow('Laies', img) # This shows the image in a window named Image title with the img image 


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray People',gray)

haar_cascade = cv2.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), thickness=2)

cv2.imshow('Detected Faces',img)

cv2.waitKey() # This waits until a key is pressed 
cv2.destroyAllWindows()
