import cv2

cap = cv2.VideoCapture(0)

people = ['Justin', 'Mom', 'Pap', 'Sars']

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

while True:
    ret, frame = cap.read()

    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_rect = face_cascade.detectMultiScale(gray, 1.6, 7)

    for(x, y, w, h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {confidence}')

        cv2.putText(frame, people[label], (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (224, 24, 37), thickness=2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (224, 24, 37), thickness=2)

    cv2.imshow('Detected Face', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()