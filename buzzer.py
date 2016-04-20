#import time
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT)

#p = GPIO.PWM(11, 50)  # channel=12 frequency=50Hz

#try:
#    while 1:
#      p.ChangeFrequency(400)
#      p.start(50)
#      time.sleep(0.5)
#      p.stop()
#      time.sleep(5)
#except KeyboardInterrupt:
#    pass
import RPi.GPIO as GPIO                 # imports Raspberry Pi's GPIO module
import time                             # imports time module
GPIO.setmode(GPIO.BOARD)                  # sets GPIO pins naming same as BCM SoC
GPIO.setup(11, GPIO.OUT) 				# sets 18 pin as output
try:
    while (True):
        GPIO.output(11, True) 				# true sets buzzer pin high
        time.sleep(0.3) 					#delay of 0.5 sec
        GPIO.output(11, False)   			#false sets buzzer pin low
        time.sleep(0.5) 					#delay of 0.5 sec
except KeyboardInterrupt:
    GPIO.output(11, False)
    GPIO.cleanup()