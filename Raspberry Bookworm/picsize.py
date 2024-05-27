from picamera2 import Picamera2

picam2 = Picamera2()
pic_config = picam2.create_still_configuration({"size":(980,720)})
picam2.start_and_capture_file("test2.jpeg",capture_mode = pic_config)
