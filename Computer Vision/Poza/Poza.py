import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread("Abstract.jpg", cv2.IMREAD_COLOR);
cv2.namedWindow("picture",cv2.WINDOW_NORMAL)
cv2.imshow("picture", img)
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])
plt.show()
k = cv2.waitKey(0)
if k == 10:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite("painting.png", img)
	cv2.destroyAllWindows()