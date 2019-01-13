import RPi.GPIO as GPIO
import time

def ledOut2(port):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(port, GPIO.OUT)

    GPIO.output(port, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(port, GPIO.LOW)
    GPIO.cleanup()