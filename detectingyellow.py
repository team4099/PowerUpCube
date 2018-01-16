import numpy as np
import cv2
from time import sleep

cap = cv2.VideoCapture(1)

while(True):
    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #blur = cv2.blur(hsv,(5,5))
    
    #lower_range = np.array([59, 45, 45], dtype=np.uint8)
    #upper_range = np.array([80, 100, 100], dtype=np.uint8)
    lower_range = np.array([20, 100, 100], dtype=np.uint8)
    upper_range = np.array([30, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_range, upper_range)
 
    cv2.imshow('mask',mask)
    cv2.imshow('image', img)
    cv2.waitKey(1)
# When everything done, release the capture
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
