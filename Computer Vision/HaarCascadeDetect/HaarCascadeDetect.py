import cv2
import numpy as np 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x ,y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x + w, y + h), (255, 200, 40), 2)
		roi_gray = gray[y:y + h, x:x + w]
		roi_color = img[y:y + h, x:x + w]
		eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
		for(x, y, w, h) in eyes:
			cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 255, 0), 3)
	cv2.imshow("GOTCHA", img)
	k = cv2.waitKey(20) & 0xFF
	if k == 27:
		break
cap.release()
cv2.destrotAllWindows()