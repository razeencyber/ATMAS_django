import numpy as np 
import cv2
import pickle
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade  = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml") #Learning the trained data


getId = 0
font = cv2.FONT_HERSHEY_SIMPLEX
#card_number = 1 #we will use request.session to store the card number
userId = 0
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0), 2)

        getId,conf = recognizer.predict(gray[y:y+h, x:x+w])
        print(getId)
        print(conf)
        if conf <  42:
            userId = getId
            cv2.putText(img, "Detected",(x,y+h), font, 2, (0,255,0),2)
        else:
            cv2.putText(img, "Unknown",(x,y+h), font, 2, (0,0,255),2)
    cv2.imshow("Face", img)
    if(cv2.waitKey(1) == ord('q')):
        break
    elif(userId!=0):
        cv2.waitKey(5000)
        break
print(userId)
cap.release()
cv2.destroyAllWindows()
