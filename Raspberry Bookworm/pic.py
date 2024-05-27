from picamera2 import Picamera2

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration({"size": (3280, 2464)})
pic_config = picam2.create_still_configuration({"size":(1640,1232)})
picam2.start_and_capture_file("test3.jpeg",delay=5,capture_mode = pic_config,show_preview = False, preview_mode = camera_config) #png, BMP, GIF
