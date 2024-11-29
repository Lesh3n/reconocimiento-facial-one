import numpy as np
import cv2 as cv
import face_recognition as fr 
import os 
import time

# Se toma la ruta del directorio (de forma relativa) en donde se tienen las imagenes a detectar. 
image_source_path = os.path.relpath('static/images/face-recognition-files/')

# Nombres de los archivos para concatenarlos en la funcion os.path.join
# TODO: PAPITO cachate alguna forma de agarrar el nombre de las imagenes sin la necesidad de estar hardcodeandolas
# va a ser un dolor de pija tener que escribir 200 variables en el caso hipotetico de tener 200 clientas.
dre_file_name = 'dre-pic.jpg'
danielle_file_name = 'danielle-marsh-pic.jpg'

# Prende la camara
camera_capture = cv.VideoCapture(0)

#Encodings 
# First encoding of the pics (which is my face)
dre_image = fr.load_image_file(f'{os.path.join(image_source_path, dre_file_name)}')
dre_face_encoding = fr.face_encodings(dre_image)[0]

# Second encoding of the pics (Danielle marsh)
danielle_image = fr.load_image_file(f'{os.path.join(image_source_path, danielle_file_name)}')
danielle_face_encoding = fr.face_encodings(danielle_image)[0]

known_face_encodings = [
    dre_face_encoding,
    danielle_face_encoding
]

known_face_names = [
    "Andres",
    "Danielle"
]

face_locations: list = []
face_encodings: list = []
face_names: list = []
process_this_frame = True

if not camera_capture.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = camera_capture.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    if process_this_frame:
        small_frame = cv.resize(frame, (0,0), fx=0.25, fy=0.25)
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

        face_locations = fr.face_locations(rgb_small_frame)
        face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

        face_names: list = []
        for face_encoding in face_encodings:
            matches = fr.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = fr.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
            time.sleep(5)


    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv.FILLED)
        font = cv.FONT_HERSHEY_DUPLEX
        cv.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        

    cv.imshow('Video', frame)

    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
camera_capture.release()
cv.destroyAllWindows()