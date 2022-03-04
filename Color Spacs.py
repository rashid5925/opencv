import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread("images/m1.jpg")
cv.imshow("Image", image)

bgr = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cv.imshow("RGB", bgr)

plt.imshow(bgr)
plt.show()

# hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
# cv.imshow("HSV", hsv)

# cv.waitKey(0)
