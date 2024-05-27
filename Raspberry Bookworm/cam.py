import cv2
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.preview_configuration.main.size=(980,540) #full screen : 3280 2464
picam2.preview_configuration.main.format = "RGB888" #8 bits
picam2.start()

while True:
	im = picam2.capture_array()
	cv2.imshow("preview",im)
	if cv2.waitKey(1)==ord('q'):
		break

picam2.stop()
cv2.destroyAllWindows()
