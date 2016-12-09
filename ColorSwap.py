#Switch between detecting yellow and blue

import cv2 # OpenCV version 3.1.0
import numpy as np

#Values for cv2.waitKey()
SPACE_BAR = 32
ESCAPE_KEY = 27

def main():
	#Capture video from camera
	videoCapture = cv2.VideoCapture(0)

	#Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	videoOutput = cv2.VideoWriter('OpenCV.avi', fourcc, 20.0, (640,480))

	#Detect Yellow
	lower_yellow = np.array([20,100,100])
	upper_yellow = np.array([30,255,255])

	#Detect Blue
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])

	#Current color
	lower = lower_yellow
	upper = upper_yellow
	isDetectingYellow = True

	while (videoCapture.isOpened()):
		#Capture frame-by-frame
		ret, frame = videoCapture.read()

		#Convert BGR to HSV
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
		if (ret == True):
			#Threshold the HSV image to only get the desired color within the boundries (lower - upper)
			mask = cv2.inRange(hsv, lower, upper)

			#Bitwise-AND mask and original image
			res = cv2.bitwise_and(frame,frame, mask = mask)

			#flip the frame
			frame = cv2.flip(res, 0)

			#write the flipped frame
			videoOutput.write(frame)
			cv2.imshow('frame', frame)

			#Detect key press to exit application or switch the color being detected
			key = cv2.waitKey(5)
			if key == ESCAPE_KEY:
				break
			elif key == SPACE_BAR:
				if(isDetectingYellow):
					lower = lower_blue
					upper = upper_blue
					isDetectingYellow = False
				else: #detecting blue
					lower = lower_yellow
					upper = upper_yellow
					isDetectingYellow = True
		else:
			break

	#When everything done, release the capture
	videoCapture.release()
	videoOutput.release()
	cv2.destroyAllWindows()
main()
