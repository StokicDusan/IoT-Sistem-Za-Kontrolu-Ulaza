import RPi.GPIO as GPIO
import time

class DisplayManager(object):
    def __blink(self):
        GPIO.output(18, True)
        time.sleep(blink_interval)
        GPIO.output(18, False)
        time.sleep(blink_interval)
        GPIO.output(18, True)
        time.sleep(blink_interval)
        GPIO.output(18, False)
        time.sleep(blink_interval)

    def __init__(self):
        # Configure the PIN # 18
        self.GPIO.setmode(GPIO.BOARD)
        self.GPIO.setup(18, GPIO.OUT)
        self.GPIO.setwarnings(False)

        # Blink Interval 
        self.blink_interval = .5 #Time interval in Seconds

    def displayImage(self, strImage):
        print("Displaying " + strImage)
        if 'andjela arsovic' in strImage.lower():
            self.__displayImage(self.__blink())
        elif 'dusan stokic' in strImage.lower():
            self.__displayImage(self.__blink())
        GPIO.cleanup()

