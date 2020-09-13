import numpy as np 
import cv2
import dlib
from math import hypot
import pickle
face_detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml") #Learning the trained data

def mid_point(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)
def get_blink_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    mid_top = mid_point(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    mid_bottom = mid_point(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))
    
    hor_dist = cv2.line(img, left_point, right_point, (255,0,0), 2)
    ver_dist = cv2.line(img, mid_top, mid_bottom, (255,0,0), 2)
    
    hor_dist_length = hypot((left_point[0]-right_point[0]),(left_point[1]-right_point[1]))
    ver_dist_length = hypot((mid_top[0] - mid_bottom[0]),(mid_top[1] - mid_bottom[1]))

    ratio = hor_dist_length/ver_dist_length
    return ratio

getId = 0
font = cv2.FONT_HERSHEY_SIMPLEX
#card_number = 1 #we will use request.session to store the card number
userId = 0
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)
    for face in faces:
        x, y = face.left(), face.top()
        x1,y1 = face.right(), face.bottom()
        
        cv2.rectangle(img,(x,y), (x1,y1), (0,255,0), 2)
        
        landmarks = predictor(gray, face)
        left_eye_ratio = get_blink_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blink_ratio([42, 43, 44, 45, 46, 47], landmarks)

        avg_blink_ratio = (left_eye_ratio + right_eye_ratio)/2

        #ID and confidence value
        getId,conf = recognizer.predict(gray[y:y1, x:x1])
        print(f"The ID predicted: {getId}  The confidence: {conf}",getId, conf)
                
        print(f"The blink ratio: {avg_blink_ratio}",avg_blink_ratio)
        if conf <  45:
            if avg_blink_ratio > 8.0:
                #userId = getId
                cv2.putText(img, "Detected",(x,y1), font, 2, (0,255,0),2)
            else:
                cv2.putText(img, "Please Blink",(50,150), font, 2, (255,0,0),3)
        else:
            cv2.putText(img, "Unknown",(x,y1), font, 2, (0,0,255),2)
    cv2.imshow("Face", img)
    if(cv2.waitKey(1) == ord('q')):
        break
    elif(userId!=0):
        cv2.waitKey(5000)
        break
print(userId)
cap.release()
cv2.destroyAllWindows()
