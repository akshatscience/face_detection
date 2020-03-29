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
		faces=gray[y:y+h,x:x+w]
	
	save_img='/home/akshat/new_save1/user'+str(c)+'.jpg'
	#resize=cv2.resize(frame,(200,200))		
	cv2.imwrite(save_img,faces)
	if c==5:
		break
# face comparison
my_pic=face_recognition.load_image_file('/home/akshat/new_save1/user2.jpg')
encode1=face_recognition.face_encodings(my_pic)[0]

cmp_pic=face_recognition.load_image_file('/home/akshat/img_save/user1.jpg')
encode2=face_recognition.face_encodings(cmp_pic)[0]

result=face_recognition.compare_faces([encode1],encode2)
if result[0]==True:
	print('true')
else:
	print('false')

shutil.rmtree(r'/home/akshat/new_save1')
cam.release()
cv2.destroyAllWindows()


