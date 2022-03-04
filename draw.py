import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("blank", blank)

# blank[200:300, 200:300] = 0, 255, 0
# cv.imshow("green", blank)

# cv.rectangle(blank, (0, 0), (200, 200), (0, 255, 0), thickness=5)
# cv.imshow("rect", blank)
# cv.rectangle(blank, (0, 0), (200, 200), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow("rect", blank)
# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow("rect", blank)

# cv.circle(blank, (250, 250), 40, (0, 0,255), thickness=-1)
# cv.imshow("Circle", blank)
#
# cv.line(blank, (0, 0), (250, 250), (255, 0, 0), thickness=2)
# cv.imshow("line", blank)

cv.putText(blank, "Hello", (50, 255), cv.FONT_HERSHEY_TRIPLEX, 5, (0, 255, 0), thickness=2)
cv.imshow("text", blank)

cv.waitKey(0)
