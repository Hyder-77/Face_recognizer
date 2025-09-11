import cv2
import sqlite3 as sq

trained_model= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Enter your trained data file location here/training_data.yml")
def get_profile(id):
    connection= sq.connect("Enter your database file location here/sql4.db")
    cmd ="SELECT * FROM  STUDENTS WHERE ID="+str(id)+";"
    cursor= connection.execute(cmd)
    profile =None
    for row in cursor:
        profile =row
    connection.close()
    return profile
while True :
    ret,frame = capture .read()
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= trained_model.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50,50),
        flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,200,0),2)
        id,conf = recognizer.predict(gray[y:y+h,x:x+w])
        print(conf)
        profile=get_profile(id)
        if profile != None and conf<85:
            cv2.putText(frame, "ID:"+str(profile[0]), (x, y+h+10), cv2.FONT_HERSHEY_COMPLEX, 0.9, (250, 0, 0), 2)
            cv2.putText(frame, "Name:"+str(profile[1]), (x, y+h+35), cv2.FONT_HERSHEY_COMPLEX, 0.9, (250, 0, 0), 2)
            cv2.putText(frame, "Age:"+str(profile[2]), (x, y+h+60), cv2.FONT_HERSHEY_COMPLEX, 0.9, (250, 0, 0), 2)
        else:
            cv2.putText(frame, "Loading......", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.9, (250, 0, 0), 2)        
    cv2.imshow("Face_detector",frame)
    if cv2.waitKey(10)== ord('q') or cv2.getWindowProperty("Face_detector",cv2.WND_PROP_VISIBLE)<1:
        break
capture.release()
cv2.destroyAllWindows()
