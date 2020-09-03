import numpy as np 
import cv2

#Video Capture a collection of images
cap = cv2.VideoCapture(0)

while True:
    
    #Capture frame-by-frame
    ret, frame = cap.read()
    
    #Basic GrayScale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Frames
    cv2.imshow('Face-Detector', frame)
    cv2.imshow('Basic Grayscale', gray)
    if cv2.waitKey(20) & 0xFF == ord('x'):
        break

#Release the capture at the end
cap.release()
cv2.destroyAllWindows()