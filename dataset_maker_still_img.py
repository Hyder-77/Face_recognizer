import cv2
import sqlite3 as sq
import os
trained_model= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)

def insert_update(id, name, age):
    connection = sq.connect("Enter your database file location here/sql4.db")
    cursor = connection.execute("SELECT * FROM STUDENTS WHERE ID=?", (id,))
    record = cursor.fetchone()
    if record:
        connection.execute("UPDATE STUDENTS SET NAME=?, AGE=? WHERE ID=?", (name, age, id))
    else:
        connection.execute("INSERT INTO STUDENTS (ID, NAME, AGE) VALUES (?, ?, ?)", (id, name, age))
    connection.commit()
    connection.close()
input_folder = "Enter your image file location here"

output_folder = "Enter your output file location here"
os.makedirs(output_folder, exist_ok=True)

trained_model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
id = input("Enter id: ")
name = input("Enter name: ")
age = input("Enter age: ")
insert_update(id,name,age)
sample_no = 0
for filename in os.listdir(input_folder):
    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path)
    if img is None:
        print(f"Could not read {img_path}, skipping.")
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = trained_model.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        sample_no += 1
        face = gray[y:y+h, x:x+w]
        save_path = os.path.join(output_folder, f"user.{id}.{sample_no}.jpg")
        cv2.imwrite(save_path, face)
        print(f"Saved {save_path}")
    if sample_no >= 40:
        break

print("Dataset creation complete.")
