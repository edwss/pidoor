import banco
import time
import RPi.GPIO as GPIO
import time

MATRIX = [[1, 2, 3, 'A'],
          [4, 5, 6, 'B'],
          [7, 8, 9, 'C'],
          ['*', 0, '#', 'D']]
ROW = [12, 16, 18, 22]
COL = [7, 11, 13, 15]


class Keypad():
    def __init__(self):
        self.check_password = ''
        try:
            self.database = banco.Connection()
        except Exception as e:
            time.sleep(5)
            self.database = banco.Connection()
            print e

    def Read_char(self):
        for j in range(4):
            GPIO.output(COL[j], 0)
            for i in range(4):
                if (GPIO.input(ROW[i]) == 0):
                    if (MATRIX[j][i] == 'D'):
                        GPIO.output(COL[j], 1)
                        return True
                    time.sleep(0.2)
                    self.check_password += str(MATRIX[j][i])
                    print MATRIX[j][i]
                    while (GPIO.input(ROW[i]) == 0):
                        pass
            GPIO.output(COL[j], 1)

    def Check_pass(self):
        try:
            print self.check_password
            if (self.database.check_pass(self.check_password)):
                self.Clean_buffer()
                return 1
            else:
                self.Clean_buffer()
                return 0
        except:
            self.Clean_buffer()
            pass

    def Clean_buffer(self):
        self.check_password = ''
