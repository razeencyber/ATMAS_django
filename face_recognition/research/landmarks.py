#Importing packages
import dlib
import numpy as np
import cv2


cap = cv2.VideoCapture(0)
#Initialising the detector
detector = dlib.get_frontal_face_detector() 
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 

while True:
    ret, img = cap.read()
    #Grayscale Conversion
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    #Getting the face landmarks
    for face in faces:
        landmarks = predictor(gray, face)
        #Accessing the landmarks
        for point in range(0, 68):
            x = landmarks.part(point).x
            y = landmarks.part(point).y
            cv2.circle(img, (x,y), 2, (0, 0, 255))
    cv2.imshow("Face", img)
    #for breaking out of the while loop
    if (cv2.waitKey(1) == ord('q')):
        break

#Releasing capture and destroying all windows
cap.release()
cv2.destroyAllWindows()