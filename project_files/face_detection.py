import cv2
from os import listdir
from os.path import isfile,join
import numpy as np
import time

path='/home/akshat/img_save/'
files=[]
for i in listdir(path):
    if isfile(join(path,i)):
        files.append(i)

train_data=[]
label=[]
for i,_ in enumerate(files):
    img_path=path+files[i]
    image=cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    train_data.append(np.asarray(image,dtype=np.uint8))
    label.append(i)

label=np.asarray(label,dtype=np.int32)
model=cv2.face.LBPHFaceRecognizer_create() #face recognizer algo LBP
model.train(np.asarray(train_data),np.asarray(label)) #train dataset(model)
    
classifier=cv2.CascadeClassifier('/home/akshat/final_project/env/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
def face_detect(img,size=0.5):
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=classifier.detectMultiScale(grey,1.3,5)
    if face is():
        return img,[]
    for (x,y,h,w) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi=img[y:y+h,x:x+w]
        roi=cv2.resize(roi,(200,200))
    return img,roi

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    images,faces=face_detect(frame)
    try:
        faces=cv2.cvtColor(faces,cv2.COLOR_BGR2GRAY)
        result=model.predict(faces)
        if result[1]<500:
            conf=int(100*(1-(result[1])/300))
        
        if conf>75: #face detection start
       
            #time.sleep(3)
            cv2.putText(images,str(conf),(240,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,255),2)
            cv2.imshow('your face',images)
                #cv2.imshow('face',images)
        else:
            cv2.putText(images,str(conf),(240,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
            cv2.imshow('face',images)  
    except:
        cv2.putText(images,'face not found',(240,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imshow('face',images)
            
    if cv2.waitKey(1)==ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
