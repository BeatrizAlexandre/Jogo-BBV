# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 11:19:54 2018

Programa para testar open cv.

@author: biaku
"""

import cv2
import numpy as np

lowerBound = np.array([20,100,20])
upperBound = np.array([80,255,255])

cam = cv2.VideoCapture(0)

teste = True
while teste:
    ret, img = cam.read()
    img = cv2.resize(img, (340, 220))    
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV,lowerBound,upperBound)
    x,y,w,h=cv2.boundingRect(mask)
    print(x, y)
    cv2.imshow('mask',mask)
    cv2.imshow('cam',img)
    cv2.waitKey(10)
    
    