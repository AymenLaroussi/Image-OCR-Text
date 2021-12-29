import cv2
import io

# Import image
img = cv2.imread("images/1.jpg")

# Get image propriety
height, width, _ = img.shape
# Use api ocr from link below
url_api="https://api.ocr.space/parse/image"
# Compress image
_, image_compress = cv2.imencode(".jpg", img, [1, 90])
file_bytes = io.BytesIO(image_compress)


# Display Image
cv2.imshow("img", img)
cv2.waitKey(0)