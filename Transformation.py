import cv2 as cv
import numpy as np

image = cv.imread("images/m1.jpg")
cv.imshow("Image", image)


# def translation(image, x, y):
#     transMat = np.float32([[1, 0, x], [0, 1, y]])
#     dimensions = (image.shape[1], image.shape[0])
#     return cv.warpAffine(image, transMat, dimensions)
#
#
# translated = translation(image, -100, -100)
# cv.imshow("translated", translated)


# def rotation(image, angle, rotPoint=None):
#     (height, width) = image.shape[:2]
#
#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
#
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimension = (width, height)
#
#     return cv.warpAffine(image, rotMat, dimension)
#
#
# rotated = rotation(image, -45)
# cv.imshow("rotated", rotated)


# Resize
# resized = cv.resize(image, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", resized)


# Flip
# flip = cv.flip(image, 0)
# cv.imshow("flipes", flip)
#
# flip2 = cv.flip(image, 1)
# cv.imshow("Flip", flip2)
#
# flip3 = cv.flip(image, -1)
# cv.imshow("Flip", flip3)


# Cropped
cropped = image[200:400, 300:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)
