import numpy as np
import cv2
import winsound
face_cascade = cv2.CascadeClassifier('frontalface.xml')
mouth_cascade = cv2.CascadeClassifier('mouth.xml')

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("V2.mkv")
    
while 1:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    mouth = mouth_cascade.detectMultiScale(gray, 1.3, 5)
    Alarmdetect=0
    font=cv2.FONT_HERSHEY_SIMPLEX
    fontScale=1
    lineType=2


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
    if len(faces)>=1:

        if len(mouth)>=1:
            Alarmdetect=1
            pos1=(80,400)
            fontColor1=(0,0,255)
            cv2.putText(img,str("Person Detect Without Mask"),pos1,font,fontScale+0.2,fontColor1,lineType)
        else:
            pos1=(80,400)
            fontColor1=(255,0,0)
            cv2.putText(img,str("Person Detect With Mask"),pos1,font,fontScale+0.2,fontColor1,lineType)


    if Alarmdetect==1:
        frequency = 1500  # Set Frequency To 2500 Hertz
        duration = 500  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        
            
    if cv2.waitKey(100) & 0xFF == ord('q'):
                break
    cv2.imshow('img',img)

cap.release()
cv2.destroyAllWindows()
