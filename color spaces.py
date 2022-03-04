import cv2 as cv
import numpy as np

image = cv.imread("images/m1.jpg")
cv.imshow("image", image)

blank = np.zeros(image.shape[:2], dtype="uint8")

b, g, r = cv.split(image)

# cv.imshow("b", b)
# cv.imshow("g", g)
# cv.imshow("r", r)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("b", blue)
cv.imshow("g", green)
cv.imshow("r", red)


# merged = cv.merge([b, g, r])
# cv.imshow("Merged", merged)

cv.waitKey(0)
