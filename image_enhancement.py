import cv2
import numpy as np

image = cv2.imread('lena.webp')

bright = cv2.convertScaleAbs(image, alpha=1.2, beta=50)


cv2.imshow("Original image: ", image)
cv2.imshow("Enhanced Image: ", bright)

cv2.waitKey(0)
cv2.destroyAllWindows()