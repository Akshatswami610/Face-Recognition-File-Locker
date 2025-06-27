import cv2
import face_recognition
import numpy as np
import os
from file_encryptor import decrypt_file

def unlock_file(filename):
    known_faces = []
    known_names = []

    for file in os.listdir('faces'):
        encoding = np.load(f'faces/{file}')
        known_faces.append(encoding)
        known_names.append(file.split('.')[0])

    cam = cv2.VideoCapture(0)
    print("Show your face to unlock")
    while True:
        ret, frame = cam.read()
        if not ret:
            continue
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces, encoding)
            if True in matches:
                matched_name = known_names[matches.index(True)]
                print(f"Face recognized: {matched_name}")
                decrypt_file(f"secured_files/{filename}.enc", f"{filename}.unlocked")
                print(f"File '{filename}' unlocked!")
                cam.release()
                cv2.destroyAllWindows()
                return
        cv2.imshow("Unlock Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
