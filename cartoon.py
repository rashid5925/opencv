import cv2 as cv
import numpy as np

image = cv.imread("images/m1.jpg")

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)
color = cv.bilateralFilter(image, 9, 250, 250)
cartoon = cv.bitwise_and(color, color, mask=edges)

cv.imshow("Image", image)
cv.imshow("Edges", edges)
cv.imshow("Cartoon", cartoon)
cv.waitKey(0)
cv.destroyAllWindows()