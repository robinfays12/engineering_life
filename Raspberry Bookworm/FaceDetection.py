import cv2
from picamera2 import Picamera2

face_cascade = cv2.CascadeClassifier('./opencv-4.x/data/haarcascades/haarcascade_frontalface_default.xml')

def detect_face(img):
	coord = face_cascade.detectMultiScale(img)
	for(x,y,w,h) in coord:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),5)
	return img

picam2 = Picamera2()
picam2.preview_configuration.main.size=(1280,720) #full screen : 3280 2464
picam2.preview_configuration.main.format = "RGB888" #8 bits
picam2.start()

while True:
        im = picam2.capture_array()
        im = detect_face(im)
        cv2.imshow("preview",im)
        if cv2.waitKey(1)==ord('q'):
                break

picam2.stop()
cv2.destroyAllWindows()
