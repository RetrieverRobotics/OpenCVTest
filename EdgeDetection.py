#Detect Edges of an object

import cv2 # OpenCV version 3.1.0
import numpy as np

ESCAPE_KEY = 27
SPACE_BAR = 32

videoCapture = cv2.VideoCapture(0)

while(True):
	#Get each frame
	ret, frame = videoCapture.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	#Edge Detection
	edges = cv2.Canny(frame, 100, 200)

	#Denoise 
	blur = cv2.GaussianBlur(edges , (5,5), 0)

	#Show blur and no blur
	cv2.imshow('Edges', edges)
	cv2.imshow('Blur', blur)

	#Escape to quit
	k = cv2.waitKey(5) & 0xFF
	if k == ESCAPE_KEY:
		break

cv2.destroyAllWindows()
videoCapture.release()

