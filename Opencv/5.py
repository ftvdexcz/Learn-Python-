import cv2  
import numpy as np 

cap = cv2.VideoCapture('C:/Users/NC.DESKTOP-8TG1B6T/Videos/Captures/Muck 2021-07-05 17-08-17.mp4')

while True:
	ret, frame = cap.read()
	width = int(cap.get(3))
	height = int(cap.get(4))

	hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	cv2.imshow('frame', hsv_img)

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cap.destroyAllWindows()
