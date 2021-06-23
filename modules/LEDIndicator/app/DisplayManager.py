import RPi.GPIO as GPIO
import time

class DisplayManager(object):
    def __dozvoljen_pristup(self):
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, True)
        time.sleep(self.blink_interval/1000)
        GPIO.output(22, False)
        GPIO.output(16, True)
        time.sleep(self.blink_interval)
        GPIO.output(16, False)
        time.sleep(self.blink_interval/1000)
        GPIO.output(18, False)
        time.sleep(self.blink_interval)
        GPIO.cleanup(16)
        GPIO.cleanup(18)


    def __nije_dozvoljen_pristup(self):
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, False)
        GPIO.output(22, False)
        GPIO.output(16, True)
        time.sleep(self.blink_interval)
        GPIO.output(16, False)
        time.sleep(self.blink_interval)
        GPIO.cleanup(16)
        GPIO.cleanup(18)

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # Blink Interval in Seconds
        self.blink_interval = 5.0

    def displayPerson(self, strImage):
        print("Displaying " + strImage)
        if 'andjela arsovic' in strImage.lower():
            self.__dozvoljen_pristup()
        elif 'dusan stokic' in strImage.lower():
            self.__dozvoljen_pristup()
        else:
            self.__nije_dozvoljen_pristup()


