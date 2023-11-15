# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:42:49 2021

@author: richardlin
"""

import cv2

img = cv2.imread('C:/Users/Richard/Downloads/testing_img.jpg')

image = cv2.resize(img,(500,300))

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(image_gray,(5,5),0)

ret, im_th = cv2.threshold(image_gray,90,255,cv2.THRESH_BINARY)

rt, im_th_inv = cv2.threshold(image_gray,90,255,cv2.THRESH_BINARY_INV)

ctrs, hier = cv2.findContours(im_th.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image,ctrs,-1,(0,255,255),2)

for c in ctrs:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),1)
    #print(image[122])
    row,col,c = image.shape
    #print(row,col)
    roi = image[y:y++h,x:x+w]
    #print(roi)
    roi = cv2.resize(roi,(28,28))
    roi=cv2.dilate(roi,(3,3))
    print(roi)


cv2.imshow('contours',image)

cv2.imshow('original image',image)

cv2.imshow('grascale image', image_gray)

cv2.imshow('blurred image', img_blur)

cv2.imshow('threshold image',im_th)

cv2.imshow('threshold invert image',im_th_inv)

cv2.waitKey(0)

cv2.destroyAllWindows()
