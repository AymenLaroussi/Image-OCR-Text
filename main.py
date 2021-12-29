import cv2
import io
import requests
import json

# Import image
img = cv2.imread("images/1.jpg")

# Get image propriety
height, width, _ = img.shape
# Use api ocr from link below
url_api="https://api.ocr.space/parse/image"
# Compress image
_, image_compress = cv2.imencode(".jpg", img, [1, 90])
file_bytes = io.BytesIO(image_compress)
# Upload image
result = requests.post(url_api,
        files = {"2.jpg": file_bytes},
        data = {"apikey": "helloworld"})

# Extract Data
result = result.content.decode()
result = json.loads(result)
parsed_results = result.get("ParsedResults")[0]
text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)

# Display Image
cv2.imshow("img", img)
cv2.waitKey(0)