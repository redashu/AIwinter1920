#!/usr/bin/python3

import cv2
#  loading  camera driver
cap=cv2.VideoCapture(0)
f=cv2.CascadeClassifier('humanface.xml')
g=cv2.CascadeClassifier('eye.xml')
print(dir(f))
while True:
    y,x=cap.read()  #take one shot
    face=f.detectMultiScale(x)
    #print(x)
    print(face)
    #print(x.shape)
    for (fx,fy,fw,fh)  in  face:
        cv2.rectangle(x,(fx,fy),(fx+fw,fy+fh),(0,0,255),4)
        onlyface=x[fy:fy+fh,fx:fx+fw]
        eye=g.detectMultiScale(onlyface)
        for  (ex,ey,ew,eh) in eye:
            cv2.rectangle(onlyface,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('adhoc',x/1257)
    cv2.imshow('adhoc1',x)
    #cv2.imshow('adhoc1',onlyface)
    #cv2.imshow('adhoc1',x[0:200,50:400])
    if  cv2.waitKey(10)  &  0xff ==  ord('q'):
        break

