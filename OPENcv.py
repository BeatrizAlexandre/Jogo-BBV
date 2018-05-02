# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 11:31:52 2018

@author: vitor
"""

#import cv2
#import numpy as np
#
#device = cv2.VideoCapture(0)
#while True:
#    
#    ret, frame = device.read()
#    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#    lower_range = np.array([110, 50, 50])
#    upper_range = np.array([130, 255, 255])
#    
#    mask = cv2.inRange(hsv, lower_range, upper_range )
#    cv2.imshow('Maked', mask)
#    
#    result = cv2.bitwise_and(frame, frame, mask=mask )
#    cv2.imshow('Maked', mask)
#    
#    if cv2.waitKey(0)==27:
#        break
#device.release()
#cv2.destroyAllWindows()

import cv2
import numpy as np

lowerBound = np.array([20,100,100])
upperBound = np.array([80,255,255])

cam = cv2.VideoCapture(0)

teste = True
while teste:
    ret, img = cam.read()
    print(img)
    img = cv2.resize(img, (340, 220))    
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV,lowerBound,upperBound)
    x,y,w,h=cv2.boundingRect(mask)
    print(x, y)
    cv2.imshow('mask',mask)
    cv2.imshow('cam',img)
    cv2.waitKey(10)
