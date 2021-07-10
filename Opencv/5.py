import cv2  
import numpy as np 

cap = cv2.VideoCapture('C:/Users/NC.DESKTOP-8TG1B6T/Videos/Captures/Muck 2021-07-05 17-08-17.mp4')

while True:
	ret, frame = cap.read()
	width = int(cap.get(3))
	height = int(cap.get(4))

	# Color detection (blue)
	hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([110, 50, 50]) # chặn dưới 
	upper_blue = np.array([130, 255, 255]) # chặn trên

	# mask: phát hiện blue trong ảnh (cho biết nên giữ lại phần nào trong ảnh)
	mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

	result = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('frame', result)
	cv2.imshow('mask', mask)
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cap.destroyAllWindows()