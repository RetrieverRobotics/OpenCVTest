#Switch between HSV or BGR trackbars to modify an image

import cv2 # OpenCV version 3.1.0
import numpy as np


#HSV min-max values in opencv
H_MIN, S_MIN, V_MIN = 0, 0, 0
H_MAX, S_MAX, V_MAX = 180, 255, 255

#RGB min-max values in opencv
B_MIN, G_MIN, R_MIN = 0, 0, 0
B_MAX, G_MAX, R_MAX = 255, 255, 255

#Values for cv2.waitKey()
ESCAPE_KEY = 27

#This function does nothing
def null(x):
	pass

def main():
	#Create a gray image in a window
	width, height, channels = 300, 500, 3
	image = np.zeros((width, height, channels), np.int8)
	cv2.namedWindow('image')

	#Create trackbars for HSV Changes
	cv2.createTrackbar('H', 'image', H_MIN, H_MAX, null)
	cv2.createTrackbar('S', 'image', S_MIN, S_MAX, null)
	cv2.createTrackbar('V', 'image', V_MIN, V_MAX, null)
	cv2.createTrackbar('B', 'image', B_MIN, B_MAX, null)
	cv2.createTrackbar('G', 'image', G_MIN, G_MAX, null)
	cv2.createTrackbar('R', 'image', R_MIN, R_MAX, null)

	#Switch between RGB and HSV
	switchModes = 'HSV: 0\nRGB: 1'
	cv2.createTrackbar(switch, 'image', 0, 1, null)

	while True:
		cv2.imshow('image', image)
		#'& 0xFF' required for 64-bit machines
		key = cv2.waitKey(1) & 0xFF 
		if key == ESCAPE_KEY:
			break

		#get current positions of all trackbars
		hPos = cv2.getTrackbarPos('H', 'image')
		sPos = cv2.getTrackbarPos('S', 'image')
		vPos = cv2.getTrackbarPos('V', 'image')
		rPos = cv2.getTrackbarPos('R', 'image')
		gPos = cv2.getTrackbarPos('G', 'image')
		bPos = cv2.getTrackbarPos('B', 'image')
		switchPos = cv2.getTrackbarPos(switchModes, 'image')
		
		hsv = [hPos,sPos,vPos]
		rgb = [rPos,gPos,bPos]
		
		if switchPos == 0:
			image[:] = hsv
		else:
			image[:] = rgb

	cv2.destroyAllWindows()
main()
