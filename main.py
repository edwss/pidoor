import time

time.sleep(3.0)
import porta
import keypad
import RPi.GPIO as GPIO

Porta = porta.Porta()
Keypad = keypad.Keypad()
GPIO.setmode(GPIO.BOARD)
ROW = [12, 16, 18, 22]
COL = [7, 11, 13, 15]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(40, GPIO.OUT)
GPIO.output(40, 0)

try:
    while True:
        try:
            if (Keypad.Read_char()):
                if (Keypad.Check_pass()):
                    Porta.Open()
        except Exception as e:
            print e
except KeyboardInterrupt:
    GPIO.cleanup()
