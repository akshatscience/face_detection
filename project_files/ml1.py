def activate():
    import cv2
    cap = cv2.VideoCapture(0) 
    while True:
        r,frame = cap.read()
        cv2.imshow('output',frame)
        if cv2.waitKey(1)==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    
    activate()