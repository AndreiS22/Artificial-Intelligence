import numpy as np
import cv2

#initializare
img = cv2.imread("Abstract.jpg", cv2.IMREAD_COLOR)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#desenat
cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)
cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)
cv2.circle(img, (100, 63), 55, (0, 0, 255), -1)
#facem un poligon. Mai intai avem nevoie de pcte
pct = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
#pct = pct.reshape((-1, 1, 2))
cv2.polylines(img, [pct], True, (0, 255, 255), 3)
#scriem
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "CV says Hello!", (0, 130), font, 1, (200, 255, 255), 2, cv2.LINE_AA)
#afisat si distrus file
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()