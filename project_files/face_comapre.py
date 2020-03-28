import cv2
import shutil
import os
import time
import face_recognition
import numpy as np

detect=cv2.CascadeClassifier('/home/akshat/final_project/env/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
path=os.path.join('/home/akshat/','new_save1')
os.mkdir(path)
cam=cv2.VideoCapture(0)
c=0

while True:
	ret,frame=cam.read()
	c+=1
	#cv2.imshow('fame',frame)
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	face_size=detect.detectMultiScale(gray,1.3,5)
	for (x,y,h,w) in face_size:
		faces=frame[y:y+h,x:x+w]
	save_img='/home/akshat/new_save1/user'+str(c)+'.jpg'
	#resize=cv2.resize(frame,(200,200))		
	cv2.imwrite(save_img,faces)
	if c==5:
		break

shutil.rmtree(r'/home/akshat/new_save1')
cam.release()
cv2.destroyAllWindows()


