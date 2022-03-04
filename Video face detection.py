import cv2 as cv

capture = cv.VideoCapture(0)


while True:
    isTrue, image = capture.read()

    cv.imshow("Video", image)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", gray)

    haar_cascade = cv.CascadeClassifier("haar_face.xml")
    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    print(len(face_rect))

    for (x, y, w, h) in face_rect:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    cv.imshow("Detected", image)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
