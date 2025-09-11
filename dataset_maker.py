import cv2
import numpy as np
import sqlite3 as sq

trained_model= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)

def insert_update(id,name,age):
    connection= sq.connect("E:/mL/opencv/sql4.db")
    cmd ="SELECT * FROM  STUDENTS WHERE ID="+str(id)+";"
    cursor= connection.execute(cmd)
    record_bool=0
    for row in cursor:
        record_bool=1
        if record_bool==1:
          connection.execute("UPDATE STUDENTS SET NAME=?,AGE=? WHERE ID=?",(name,age,id))
        else:
           connection.execute("INSERT INTO STUDENTS (ID,NAME,AGE) VALUES(?,?,?)",(id,name,age))
    connection.commit()
    connection.close()
#user input
id=input("enter id:")
name=input("enter name:")
age=input("enter age:")

insert_update(id,name,age)
sample_no=0
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
        sample_no+=1
        face= gray[y:y+h,x:x+w]
        cv2.imwrite("E:/mL/opencv/face_recognizer/data/user."+str(id)+"."+str(sample_no)+".jpg",face)
        cv2.waitKey(150)
    cv2.imshow("sampling",frame)
    cv2.waitKey(1)
    if sample_no>=20:
        break
capture.release()
cv2.destroyAllWindows()

