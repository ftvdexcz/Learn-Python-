import numpy as np 
import cv2 
import random

img = cv2.imread('E:/Long/AI/fruit.jpg')

# Image representation (Opencv use BGR)
print(img) 

# Access pixel value (H,W,C)
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

# Copy parts of image (slicing window)
new_img = np.array(img[50:350,50:400,:img.shape[2]])

# Paste parts of image 
img[70:370,70:420,:img.shape[2]] = new_img

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()