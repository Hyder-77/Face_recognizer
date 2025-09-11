# 🎯 Face Recognition System using OpenCV and SQLite

This project is a complete pipeline for face recognition using OpenCV's Haar Cascade and LBPH (Local Binary Patterns Histograms) algorithm. It includes dataset creation (from webcam and still images), training, and real-time face recognition with profile display from an SQLite database.

---

## 📁 Project Structure

face_recognizer/ 
├── data/ # Stores cropped face images 
├── source_images/ # Folder for still image dataset input 
├── recognizer/ # Stores trained model (.yml) 
├── sql4.db # SQLite database for storing user profiles
├── dataset_maker.py # Capture face samples via webcam
├── dataset_from_images.py # Create dataset from still images 
├── train_model.py # Train LBPH model 
└── face_recognizer.py # Real-time face recognition


---

## 🧠 Features

- Face detection using Haar Cascade
- Dataset creation via webcam or static images
- SQLite integration for storing user profiles (ID, Name, Age)
- LBPH-based face recognition
- Real-time face identification with profile overlay

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install opencv-python numpy pillow

 2. Create Dataset via Webcam
python dataset_maker.py

 3. Create Dataset from Still Images
Place images in source_images/<user_id>/ and run:
python dataset_from_images.py

4. Train the Model

python train_model.py

5. Run Face Recognition
Press q to exit the recognition window.

## 🗃️ Database Schema
SQLite table: STUDENTS

Column  	Type	  Description
ID	       INTEGER	  Unique user ID
NAME	    TEXT	   User's name
AGE	      INTEGER	   User's age

##🛠️ Technologies Used
Python

OpenCV

SQLite

NumPy

PIL (Pillow)

##📌 Notes
Minimum 20 samples are captured per user via webcam.

Still image dataset captures up to 40 samples.

Recognition confidence threshold is set to < 85.

##👨‍💻 Author
Tanveer Hyder Aspiring AI Engineer | Electrical Engineering Student Focused on ethical AI and real-world applications.