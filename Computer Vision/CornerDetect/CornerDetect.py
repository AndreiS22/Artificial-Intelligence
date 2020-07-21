import numpy as np
import cv2

img = cv2.imread('opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

while True:
	corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 4)
	corners = np.int0(corners)

	for corner in corners:
	    x,y = corner.ravel()
	    cv2.circle(img,(x,y),5 ,255,-1)
	    
	cv2.imshow('Corner',img)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
cv2.destroyAllWindows()
