#Use trackbars to adjust the threshold of the video camera input

import cv2 #OpenCV 3.1.0
import numpy as np

#BGR min-max values in opencv
B_MIN, G_MIN, R_MIN = 0, 0, 0
B_MAX, G_MAX, R_MAX = 255, 255, 255

#Keyboard keys for cv2.waitKey()
ESCAPE_KEY = 27
SPACE_BAR = 32

#This function does nothing
def null(x):
	pass

#Create a gray image in a window
width, height, channels = 300, 300, 3
image = np.zeros((width, height, channels), np.int8)
cv2.namedWindow('image')

#Create trackbars for lower BGR values
cv2.createTrackbar('bMin', 'image', B_MIN, B_MAX, null)
cv2.createTrackbar('gMin', 'image', G_MIN, G_MAX, null)
cv2.createTrackbar('rMin', 'image', R_MIN, R_MAX, null)

#Create trackbars for upper BGR values
cv2.createTrackbar('bMax', 'image', B_MIN, B_MAX, null)
cv2.createTrackbar('gMax', 'image', G_MIN, G_MAX, null)
cv2.createTrackbar('rMax', 'image', R_MIN, R_MAX, null)

#Get video from camera
videoCapture = cv2.VideoCapture(0)

while True:
	#'& 0xFF' required for 64-bit machines
	key = cv2.waitKey(1) & 0xFF
	if key == ESCAPE_KEY:
		break

	#get current positions of all trackbars
	bMinPos = cv2.getTrackbarPos('bMin', 'image')
	gMinPos = cv2.getTrackbarPos('gMin', 'image')
	rMinPos = cv2.getTrackbarPos('rMin', 'image')
	bgrMinimum = np.array([bMinPos, gMinPos, rMinPos])
	lower = np.array(bgrMinimum, np.uint8)

	bMaxPos = cv2.getTrackbarPos('bMax', 'image')
	gMaxPos = cv2.getTrackbarPos('gMax', 'image')
	rMaxPos = cv2.getTrackbarPos('rMax', 'image')
	bgrMaximum = np.array([bMaxPos, gMaxPos, rMaxPos])
	upper = np.array(bgrMaximum, np.uint8)

	#Take frame
	ret, frame = videoCapture.read()
	image = frame
	
	#Convert from BGR to HSV
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	#Threshhold the HSV image
	mask = cv2.inRange(hsv, lower, upper)
	res = cv2.bitwise_and(image, image, mask = mask)
	
	#Denoise image
	gaussianBlur = cv2.GaussianBlur(res, (5,5), 0)
	
	#Show both images horizontally
	cv2.imshow('image', np.hstack([image, gaussianBlur]))

cv2.destroyAllWindows
