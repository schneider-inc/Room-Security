import cv2
import json

def detect(img):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    with open('data.txt') as people:
        people = json.load(people)['people']
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('face_trained.yml')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces_rect = face_cascade.detectMultiScale(gray, 1.6, 5)

    detected = []

    for (x, y, w, h) in faces_rect:
        face_roi = gray[y:y+h, x:x+w]
        face_roi_color = img[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(face_roi)
        detected.append([people[label], confidence, face_roi_color])

    return detected

"""
woof = detect(cv2.imread('test_justin.jpg'))

if woof:
    print(woof[0][0], woof[0][1])

else:
    print("aight")
"""