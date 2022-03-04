import cv2 as cv
import numpy as np

image = cv.imread("images/m1.jpg")
# cv.imshow("image", image)

black = np.zeros(image.shape, dtype="uint8")
# cv.imshow("black", black)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

# canny = cv.Canny(gray, 125, 175)
# cv.imshow("Canny", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)


contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print("Total contours are: ", len(contours))

cv.drawContours(black, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours Drawn", black)

cv.waitKey(0)
