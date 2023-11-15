import cv2

img = cv2.imread('C:/Users/Richard/Downloads/sanfrancisco.jpg')

cv2.imshow('Image title', img) # This shows the image in a window named Image title with the img image 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)


blur= cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow('blur',blur)



canny = cv2.Canny(blur,125,175)
cv2.imshow('Canny Edge',canny)

dilated = cv2.dilate(canny,(7,7), iterations=3)

cv2.imshow('dilated',dilated)


eroded = cv2.erode(dilated,(3,3),iterations=1)

cv2.imshow('erode',eroded)

resized = cv2.resize(img,(500,400))

cv2.imshow('Resized',resized)

cropped = img[50:200,200:400]

cv2.imshow('Cropped',cropped)
cv2.waitKey() # This waits until a key is pressed 
cv2.destroyAllWindows()
