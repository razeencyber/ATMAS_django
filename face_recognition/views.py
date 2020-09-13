from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from ATMAS_django.settings import BASE_DIR
import numpy as np
import cv2
import dlib
from math import hypot
from card_login.otp import send_warn
from card_login.models import Record


def warn_face(request):
    return render(request, 'warn.html')


def detectFace(request):
    face_detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(str(BASE_DIR) + "/face_recognition/research/shape_predictor_68_face_landmarks.dat") #

    cap = cv2.VideoCapture(0)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(
        str(BASE_DIR) +
        "/face_recognition/research/trainer.yml")  #Learning the trained data
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
    card_number = request.session[
        'CARD_NUMBER']  #we will use request.session to store the card number
    record = Record.objects.filter(id=card_number).first()
    phone_number = record.mobile_number
    print(f"CARD_NUMBER is {card_number}")
    userId = 0
    get_frame = 0
    while (True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector(gray)
        for face in faces:
            x, y = face.left(), face.top()
            x1,y1 = face.right(), face.bottom()
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 2)

            #Implementing Blink Detection to prevent spoofing
            landmarks = predictor(gray, face)
            left_eye_ratio = get_blink_ratio([36, 37, 38, 39, 40, 41], landmarks)
            right_eye_ratio = get_blink_ratio([42, 43, 44, 45, 46, 47], landmarks)

            avg_blink_ratio = (left_eye_ratio + right_eye_ratio)/2

            #Implementing Real time facial recognition
            getId, conf = recognizer.predict(gray[y:y1, x:x1])
            print(f"getId {getId} card_number {card_number} conf {conf}")
            
            
            if conf < 47 and getId == int(card_number):
                if avg_blink_ratio > 8.0:
                    userId = getId
                    cv2.putText(img, "Detected", (x, y1), font, 2, (0, 255, 0),
                                2)
                else:
                    get_frame += 1
                    cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
                    cv2.putText(img, "Spoof", (x, y1), font, 2, (0, 255, 255),
                            2)
                    cv2.putText(img, "Please Blink",(50,150), font, 2, (255,0,0),3)
                
            else:
                get_frame += 1
                cv2.putText(img, "Unknown", (x, y1), font, 2, (0, 0, 255),
                            2)
        cv2.imshow("Face", img)
        if (cv2.waitKey(1) == ord('q')):
            break
        elif (userId != 0):
            cv2.waitKey(5000)
            break
        elif get_frame > 520:
            send_warn(card_number, phone_number)
            break
    print(userId)
    print(request.session.get('CARD_NUMBER'))
    cap.release()
    cv2.destroyAllWindows()
    if userId != 0:
        return redirect('/demo')
    else:
        return redirect('/')
