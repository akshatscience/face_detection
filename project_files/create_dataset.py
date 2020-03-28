import cv2
import shutil
import os
import time
path=os.path.join('/home/akshat/','new_save1')
os.mkdir(path)
cam=cv2.VideoCapture(0)
c=0
while True:
	ret,frame=cam.read()
	c+=1
	#cv2.imshow('fame',frame)
	cv2.imwrite('/home/akshat/new_save1/user'+str(c)+'.jpg',frame)
	if c==10:
		break
	
#for _ in time.sleep(5):
 #   cv2.imshow('faces',frame)
shutil.rmtree(r'/home/akshat/new_save1')
cam.release()
cv2.destroyAllWindows()


