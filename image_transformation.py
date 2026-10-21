import cv2
import numpy as np

image = cv2.imread('lena.webp')

rows, cols = image.shape[:2]

matrix   = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)

rotated = cv2.warpAffine(image, matrix, (cols, rows))

cv2.imshow("Original Image: ", image)
cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
