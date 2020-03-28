import cv2

detect=cv2.CascadeClassifier('/home/akshat/final_project/env/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
def extract(img):
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_classifier=detect.detectMultiScale(grey,1.3,5)
    if face_classifier is():
        return None
    for (x,y,h,w) in face_classifier:
        faces=img[y:y+h,x:x+w]
    
    return faces

cap=cv2.VideoCapture(0)
c=0
while True:
    ret,frame=cap.read()
    #cv2.imshow('face',frame)
    if extract(frame) is not None:
        c+=1
        face=cv2.resize(extract(frame),(200,200))
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        save='/home/akshat/img_save/user'+str(c)+'.jpg'
        cv2.imwrite(save,face)
        #cv2.imshow('frame',frame)
    if cv2.waitKey(0)==ord('q') or c==50:
        break

    
cap.release()
cv2.destroyAllWindows()