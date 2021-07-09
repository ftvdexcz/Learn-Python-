import cv2
import imutils

# Load ảnh ở chế độ 1: giữ nguyên ban đầu
img = cv2.imread('image.jpg', 1)

# Resize image
# img = cv2.resize(img, dsize=(400,400)) # Chuyển ảnh về 400x400 pixel
img = cv2.resize(img, (0,0), fx=2., fy=2.) # Phóng to ảnh gấp đôi

# Rotate image (import imutils)
img = imutils.rotate(img,70) # xoay 70 độ ngược chiều kim đồng hồ

# Lưu ảnh
cv2.imwrite('img_new.jpg', img)

# Hiển thị ảnh
cv2.imshow('image', img)

# Đợi người dùng nhập để thoát
cv2.waitKey()
cv2.destroyAllWindows()

