import cv2 as cv


def rescale_img(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread("images/m1.jpg")
resized_img = rescale_img(img)
cv.imshow("Image", resized_img)

cv.waitKey(0)
