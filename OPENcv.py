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

lowerBound = np.array([50,150,0])
upperBound = np.array([150,255,255])

cam = cv2.VideoCapture(0)

teste = True
while teste:
    ret, img = cam.read()
    img = cv2.resize(img, (800, 600))    
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV,lowerBound,upperBound)

    # Find the largest contour and extract it
    # https://stackoverflow.com/questions/39044886/finding-largest-blob-in-image
    _, contours, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE )

    maxContour = 0
    maxContourData = None
    for contour in contours:
        contourSize = cv2.contourArea(contour)
        if contourSize > maxContour:
            maxContour = contourSize
            maxContourData = contour

    if maxContourData is not None:
        x,y,w,h=cv2.boundingRect(maxContourData)
        x = 800 - x
        print(x, y)
    else:
        print('sem contorno')
        
    cv2.imshow('mask',mask)
    cv2.imshow('cam',img)
    cv2.waitKey(10)
