import pytesseract as tss
from PIL import Image
import cv2
import sklearn




tss.pytesseract.tesseract_cmd='C:\\Users\\Junaid\\AppData\\Local\Programs\\Tesseract-OCR\\tesseract.exe'
image = Image.open('Capture.png')
text = tss.image_to_string(image)
print(text)
# Load the image
img = cv2.imread('Capture.png')

# Show the image
cv2.imshow('Image', img)

# Wait for user input
cv2.waitKey(0)

# Release resources
cv2.destroyAllWindows()
