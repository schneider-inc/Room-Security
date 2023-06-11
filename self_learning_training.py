import os
import numpy as np
import cv2
import json


def train():
    with open('data.txt') as database:
        people = json.load(database)['people']

    dir = os.getcwd() + "\\images" # gets current working directory

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    features = []
    labels = []

    def create_train():
        count = 0

        for person in people:
            print()
            print(person)
            path = os.path.join(dir, person)
            label = people.index(person)

            for img in os.listdir(path):
                print(count, img)
                img_path = os.path.join(path, img)

                img_array = cv2.imread(img_path)
                gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

                faces_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5)

                for (x, y, w, h) in faces_rect:
                    faces_roi = gray[y:y+h, x:x+w]
                    features.append(faces_roi)
                    labels.append(label)
                
                count += 1

    create_train()
    print('Training completed --------------------')

    features = np.array(features, dtype=object)
    labels = np.array(labels)

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    face_recognizer.train(features, labels)

    face_recognizer.save('face_trained.yml')
    np.save('features.npy', features)
    np.save('labels.npy', labels)

    print('DONE TRAINING')

train()