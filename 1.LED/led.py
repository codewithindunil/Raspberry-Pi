import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.output(18,GPIO.HIGH)

time.sleep(1)

GPIO.output(18,GPIO.LOW)

