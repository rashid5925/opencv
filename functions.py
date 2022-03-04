import cv2 as cv

img = cv.imread("images/m1.jpg")

cv.imshow("Image", img)

# 1. Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# 2. Blur
# blur =  cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# 3. edge cascade
# canny = cv.Canny(img, 125, 175)
# cv.imshow("canny", canny)

# 4. dilation
# dilated = cv.dilate(canny, (3, 3), iterations=1)
# cv.imshow("dilated", dilated)

# 5. eroding
# eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow("eroded", eroded)

# 6. Resize
# resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", resize)

# 7. Cropping
croped = img[50:200, 200:400]
cv.imshow("cropped", croped)

cv.waitKey(0)
