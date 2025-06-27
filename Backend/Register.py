import cv2
import face_recognition
import numpy as np
import os

def register_user(name):
    cam = cv2.VideoCapture(0)
    print("Press 's' to capture your face")
    while True:
        ret, frame = cam.read()
        if not ret:
            continue
        cv2.imshow("Register Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            face_locations = face_recognition.face_locations(frame)
            if len(face_locations) != 1:
                print("Please ensure only one face is visible.")
                continue
            face_encoding = face_recognition.face_encodings(frame)[0]
            np.save(f'faces/{name}.npy', face_encoding)
            print(f"Face registered for {name}.")
            break
    cam.release()
    cv2.destroyAllWindows()
