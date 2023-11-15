import cv2,random,numpy

import numpy as np
img = cv2.imread('test_1.jpg')

cv2.putText(img, "Hello World", (100, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 3)

cv2.imshow("Hello World image", img)


img=cv2.rectangle(img,(random.randint(10,100),random.randint(10,100)),(random.randint(0,100),random.randint(0,100)),(0,0,255),-1)
img=cv2.circle(img, (random.randint(100,900),random.randint(100,800)), random.randint(10,100), (0, 255, 0), thickness=-1)

pts = [

  numpy.array([

    numpy.array([[300,  290]]),

    numpy.array([[200, 390]]),

    numpy.array([[430,  400]])

  ])

]

img=cv2.fillPoly(img, pts, (0,255,255))


img = np.zeros((500, 500, 3), dtype=np.uint8) # This code creates a black BGR image

WIDTH = 500

HEIGHT = 100

X = 250

Y = 250

CENTER = X, Y

AXES = WIDTH/2, HEIGHT/2

ANGLE = 90

STARTANGLE = 0

ENDANGLE = 90

COLOR = (0, 255, 0)

THICKNESS = -1

##img = cv2.ellipse(img, CENTER, AXES, ANGLE,
##
##                          STARTANGLE,ENDANGLE, COLOR, THICKNESS)

cv2.imshow('Image title', img) # This shows the image in a window named Image title with the img image 


cv2.waitKey() # This waits until a key is pressed 
cv2.destroyAllWindows()
