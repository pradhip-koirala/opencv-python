import cv2
import numpy as np

image = cv2.imread('lena.webp')

blur = cv2.GaussianBlur(image, (7,7),0)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()