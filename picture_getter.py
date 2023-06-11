import cv2
import json
from time import sleep
from datetime import datetime
from detect import detect
from self_learning_training import train


def get_pictures():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if ret:
            break

    print('Camera initialised')

    count = 0

    while count < 30:
        ret, frame = cap.read()

        print("Frame taken")

        detected_faces = detect(frame)

        if detected_faces:
            print("Face(s) detected")
        else:
            print("No faces detected")

        for face in detected_faces:
            person, confidence, face_roi = face
            print(count, person, confidence)
            with open('data.txt') as database:
                data = json.load(database)
            current_time = datetime.now().strftime("%d %m %Y _ %H %M %S")

            if confidence > 100:
                face_roi = cv2.resize(face_roi, (0, 0), fx=4, fy=4)

                cv2.putText(face_roi, "Who is this?", (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (224, 24, 37),
                            thickness=2)

                cv2.imshow('Detected Face', face_roi)

                key = cv2.waitKey(0)

                with open('data.txt') as database:
                    data = json.load(database)

                if key == ord('j'):
                    cv2.imwrite(f'images/Justin/{current_time}.jpg', frame)
                elif key == ord('s'):
                    cv2.imwrite(f'images/Sars/{current_time}.jpg', frame)
                elif key == ord('m'):
                    cv2.imwrite(f'images/Mom/{current_time}.jpg', frame)
                elif key == ord('p'):
                    cv2.imwrite(f'images/Pap/{current_time}.jpg', frame)
                else:
                    print("False input")

                cv2.destroyAllWindows()

            else:
                cv2.imwrite(f'images/{person}/{current_time}.jpg', frame)

            count += 1 / len(detected_faces)  # keeps track of how many pictures have been taken

        sleep(.05)
        
get_pictures()