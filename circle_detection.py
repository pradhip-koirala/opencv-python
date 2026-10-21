import cv2
import numpy as np

image = cv2.imread('lena.webp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 
                           1,
                           20,
                           param1=50,
                           param2=30,
                           minRadius=10,
                           maxRadius=100)
if circles is not None:
    # Convert the circle parameters (x, y, radius) to integers
    circles = np.uint16(np.around(circles))
    
    # FIX: Use a colon (:) to iterate through ALL detected circles in the first row
    for i in circles[0, :]:
        # Draw the outer circle boundary (Green)
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        
        # Optional: Draw a small dot at the center of the circle (Red)
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)


cv2.imshow('Detected Circles: ',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

