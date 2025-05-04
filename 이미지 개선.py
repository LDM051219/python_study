# OpenCV-1.py
import cv2
import sys

# img = cv2.imread("fig/mri_brain.jpeg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("C:/tmp/fig/mri_brain.jpeg", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Image read failed")
    sys.exit()
    
print(type(img)) # class numpy
print(img.shape) # bgr (rgb x)
print(img.dtype)
cv2.imshow("mri", img)
cv2.waitKey(0) # ms
cv2.destroyAllWindows()