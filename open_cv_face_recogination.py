import cv2
import time

#import HandTrackingModule as htm
##############

wCam,hCam = 640,480

###############

pTime = 0

cap = cv2.VideoCapture(0)

cap.set(3,wCam)
cap.set(4,hCam)


while 1:
    succ, img = cap.read()
    cTime= time.time()
    fps = 1/(cTime-pTime)
    
    pTime = cTime

    cv2.putText(img,f'FPS:{int(fps)}',(40,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
    cv2.imshow('img',img)
    cv2.waitKey(1)
