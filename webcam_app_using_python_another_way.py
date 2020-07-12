# -*- coding: utf-8 -*-
"""Webcam_App-using_python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16BtBD64GuNER4HAEbjARKWu8RDxK9AI4
"""

import cv2

imgcapture =  cv2.VideoCapture(0)
result = True
while (result):
  ret, frame = imgcapture.read()
  cv2.imwrite("test.jpg", frame)
  result = False
  print("Image Captured!.......")


imgcapture.release()