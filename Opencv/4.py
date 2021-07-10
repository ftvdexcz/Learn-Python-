import cv2  
import numpy as np 

# Video Capture 
cap = cv2.VideoCapture('C:/Users/NC.DESKTOP-8TG1B6T/Videos/Captures/Muck 2021-07-05 17-08-17.mp4')

# get width, height of capture 
width = int(cap.get(3))
height = int(cap.get(4))

while True: 
	# frame represent an image, 
	ret, frame = cap.read()

	# Draw line: cv2.line(source, startpoint, endpoint, color, thickness)
	# frame = cv2.line(frame, (0,0), (width,height), (255,0,0), 10)

	# Draw rectangle: cv2.rectangle(source, centerpoint, radius, color, thickness (-1 to fill))
	# frame = cv2.rectangle(frame, (100,100), (200,200), (128,128,128), 5)

	# Draw circle: cv2.circle(source, centerpoint, radius, color, thickness (-1 to fill))
	# frame = cv2.circle(frame, (200,200), 60, (128, 125,215), 5)

	# Draw text: cv2.putText(source, text, center position, font, fontscale, color, linethickness, linetype)
	font = cv2.FONT_HERSHEY_SIMPLEX
	frame = cv2.putText(frame, 'Text', (200, height-10), font, 4, (0,0,0), 5, cv2.LINE_AA)

	cv2.imshow('Video test', frame)

	# Press 'q' to quit 
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()