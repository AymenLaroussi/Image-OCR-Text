import cv2

# Import image
img = cv2.imread("images/1.jpg")

# Display Image
cv2.imshow("img", img)
cv2.waitKey(0)