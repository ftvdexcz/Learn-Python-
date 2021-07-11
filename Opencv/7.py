import cv2  
import numpy as np 

# Nếu Object và ảnh có kích thước quá chênh lệch thì cần resize

img = cv2.imread('E:/Long/AI/soccer_practice.jpg',0)
template = cv2.imread('E:/Long/AI/ball.png',0)
height, width = template.shape

# Template Matching (Object Detection)
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
			cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# Try each method 
for method in methods:
	img2 = img.copy() 

	result = cv2.matchTemplate(img2, template, method)
	# Displaying matches
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		location = min_loc
	else:
		location = max_loc

	bottom_right = (location[0]+height,location[1]+width) 
	cv2.rectangle(img2, location, bottom_right, 255, 5)
	cv2.imshow('Match',img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()