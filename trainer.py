import os
import cv2
import numpy as np
from PIL import Image as img

recognizer = cv2.face.LBPHFaceRecognizer_create() #Local Binary Patterns Histograms (LBPH) face recognizer
path="E:/mL/opencv/face_recognizer/data"
def get_img(path):
    image_paths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    ids=[]
    for paths in image_paths:
        face_img=img.open(paths).convert('L')
        face_np=np.array(face_img,'uint8')
        id= int (os.path.split(paths)[-1].split(".")[1])   #"E:/mL/opencv/face_recognizer/datadata/user.1.3.jpg",os.path.split(paths) returns ('E:/mL/opencv/face_recognizer/datadata', 'user.1.3.jpg'). os.path.split(paths)
        #[-1]Gets the last element of the tuple, which is the filename:'user.1.3.jpg'.split(".")
        # #Splits the filename by the period (.) character:'user.1.3.jpg'.split(".") gives ['user', '1', '3', 'jpg'][1]Gets the second element (index 1) from the split list:'1' (which is the ID in your filename format)
        print(id)
        faces.append(face_np)
        ids.append(id)
        cv2.imshow("training",face_np)
        cv2.waitKey(10)
    return np.array(ids),faces
ids,faces=get_img(path)
recognizer.train(faces,ids)
recognizer.save("E:/mL/opencv/face_recognizer/recognizer/training_data.yml")
cv2.destroyAllWindows()
