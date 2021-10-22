import cv2
import random
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img = cv2.imread('RDJ.jpg')
webcam = cv2.VideoCapture(0)
while True:
    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for i in face_coordinates:
        (x, y, w, h) = i
        cv2.rectangle(frame, (x, y), (x+w, y+h),  (random.randint(0,128) * 28, random.randint(0,9) * 28, random.randint(0,9) * 28), 3)
    cv2.imshow("SHUBHA'S FACE DETECTOR", frame)
    key = cv2.waitKey(1)
    if key==81 or key ==113:
        break
webcam.release()
print("Job Done")