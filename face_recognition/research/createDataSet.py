import numpy as np
import os
import cv2
face_cascade = cv2.CascadeClassifier(
    'cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cam = cv2.VideoCapture(0)

id = 1

sampleNum = 0
while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleNum += 1
        cv2.imwrite(
            BASE_DIR + '/images/user.' + str(id) + '.' + str(sampleNum) +
            '.jpg', gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.waitKey(250)
    cv2.imshow("Face", img)
    cv2.waitKey(1)

    if (sampleNum > 30):
        break
cam.release()
cv2.destroyAllWindows()
