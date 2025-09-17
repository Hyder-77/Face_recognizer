import os
import cv2
import numpy as np
from PIL import Image as img

recognizer = cv2.face.LBPHFaceRecognizer_create()
path="Enter your images file location here"
def get_img(path):
    image_paths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    ids=[]
    for paths in image_paths:
        face_img=img.open(paths).convert('L')
        face_np=np.array(face_img,'uint8')
        id= int (os.path.split(paths)[-1].split(".")[1])  
        print(id)
        faces.append(face_np)
        ids.append(id)
        cv2.imshow("training",face_np)
        cv2.waitKey(10)
    return np.array(ids),faces
ids,faces=get_img(path)
recognizer.train(faces,ids)
recognizer.save("Enter your destination file where you want to saved the trained output file, location here")
cv2.destroyAllWindows()
