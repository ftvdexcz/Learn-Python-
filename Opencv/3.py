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

	# chia ảnh làm 4 góc 
	image = np.zeros_like(frame, dtype=np.uint8)
	smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
	image[:height//2, :width//2] = smaller_frame
	image[height//2:, :width//2] = smaller_frame
	image[:height//2, width//2:] = smaller_frame
	image[height//2:, width//2:] = smaller_frame

	cv2.imshow('Video test', image)

	# Press 'q' to quit 
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()