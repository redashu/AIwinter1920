#!/usr/bin/python3

import cv2
x=cv2.imread('images.jpeg')
print(x)
print(x.shape)

cv2.rectangle(x,(0,0),(300,400),(0,0,255),2)
cv2.imshow('adhoc',x)
cv2.imshow('adhoc1',x[0:200,50:400])
cv2.waitKey(0)
