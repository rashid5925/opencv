import cv2 as cv

image = cv.imread("images/m1.jpg")
cv.imshow("Image", image)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(len(face_rect))

for (x, y, w, h) in face_rect:
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Detected", image)

cv.waitKey(0)
