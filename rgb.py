import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

red = 12
green = 8
blue = 16

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

try:
    while (True):
        GPIO.output(green, True) 				# true sets buzzer pin high
        time.sleep(0.3) 					#delay of 0.5 sec
        GPIO.output(green, False)   			#false sets buzzer pin low
        time.sleep(0.5) 					#delay of 0.5 sec

        GPIO.output(red, True)  # true sets buzzer pin high
        time.sleep(0.3)  # delay of 0.5 sec
        GPIO.output(red, False)  # false sets buzzer pin low
        time.sleep(0.5)  # delay of 0.5 sec

        GPIO.output(blue, True)  # true sets buzzer pin high
        time.sleep(0.3)  # delay of 0.5 sec
        GPIO.output(blue, False)  # false sets buzzer pin low
        time.sleep(0.5)  # delay of 0.5 sec

except KeyboardInterrupt:
    GPIO.output(green, False)
    GPIO.output(red, False)
    GPIO.output(blue, False)
    GPIO.cleanup()