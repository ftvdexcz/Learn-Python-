import cv2 
import numpy as np 

img = cv2.imread('E:/Long/AI/chessboard.jpg ')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# Corner detection 


cv2.imshow('frame', img)
cv2.waitKey()
cv2.destroyAllWindows()