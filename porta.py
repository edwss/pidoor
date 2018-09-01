import RPi.GPIO as GPIO
import time
import keypad
class Porta():
    def __init__(self):
        self.check_password = ''
        self.Keypad = keypad.Keypad()
    def Open(self):
        try:
            GPIO.output(40, 1)
            time.sleep(2)
            GPIO.output(40, 0)
            self.Keypad.Clean_buffer()
        except:
            self.Keypad.Clean_buffer()
            pass
