from picamera2 import Picamera2
from picamera2.encoders import Quality


picam2 = Picamera2()

video_config = picam2.create_video_configuration(main={"size":(1920,1080)})

picam2.start_and_record_video("test.mp4",quality=Quality.HIGH,config=video_config, duration=5,show_preview=True,audio=False)

