import cv2
import os
import json
from datetime import datetime
from time import sleep
from detect import detect
from speech_recognizer import recognize_speech
from play_voice import voice


def get_person():
    with open('data.txt') as database:
        people = json.load(database)['people']

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("lol")
            continue

        detected = detect(frame)

        if not detected:
            print("not detected")
            continue

        if len(detected) > 1:
            for face1 in range(len(detected)):
                print(face1)
                for face2 in range(face1+1, len(detected)):
                    print(face2)
                    print()
                    if detected[face1][0] == detected[face2][0]:
                        detected.remove(detected[face2])

        print("detected", len(detected))

        for det_face in detected:
            name, confidence, face = det_face

            if confidence > 100:
                face = cv2.resize(face, (0, 0), fx=4, fy=4)
                face1 = face.copy()
                face2 = face.copy()
                cv2.putText(face1, f"{name}? y/n?", (20, 20),
                            cv2.FONT_HERSHEY_COMPLEX, 1.0, (224, 24, 37), thickness=2)

                while True:
                    cv2.imshow(f"{name}?", face)
                    cv2.waitKey(1)
                    current_time = datetime.now().strftime("%d%m%Y_%H%M%S")
                    response = recognize_speech(f"is this {name}")

                    if response.startswith('y'):
                        cv2.imwrite(f'images/{name}/{current_time}.jpg', frame)
                        cv2.imwrite(
                            f'images/attempted_entry/{current_time}.jpg', frame)
                        break
                    elif response.startswith('n'):
                        cv2.destroyAllWindows()

                        cv2.putText(face2, f"Then who?", (20, 20),
                                    cv2.FONT_HERSHEY_COMPLEX, 1.0, (224, 24, 37), thickness=2)
                        cv2.imshow("Then who?", face2)
                        cv2.waitKey(1)

                        while True:
                            response = recognize_speech("then who")
                            for person in people:
                                if person.startswith(response[0]):
                                    break
                            else:
                                sleep(1)
                                continue
                            cv2.imwrite(
                                f'images/{response.capitalize()}/{current_time}.jpg', frame)
                            cv2.imwrite(
                                f'images/attempted_entry/{current_time}.jpg', frame)
                            name = response.capitalize()
                            break
                        break
                    else:
                        continue

            if len(detected) == 1:
                voice(f"{name} would like to enter")
                print(name, confidence)
            elif len(detected) > 1:
                voice(name)
                if(det_face == detected[-1]):
                    voice(f"and {name} would like to enter")

        break

    cap.release()


get_person()
