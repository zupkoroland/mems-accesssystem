import RPi.GPIO as GPIO
import time

def ledOut2(port):
    #GPIO mód beállítása BOARD-ra.
    GPIO.setmode(GPIO.BOARD)
    
    #A port változón kapott érték OUT-ra állítása.
    GPIO.setup(port, GPIO.OUT)

    #A porton lévő LED megvilágítása.
    GPIO.output(port, GPIO.HIGH)
    
    #A futás szüneteltése egy másodpercig.
    time.sleep(1)
    
    #A porton lévő LED feszültségét elvesszi.
    GPIO.output(port, GPIO.LOW)
    
    #Felszabadítja a GPIO-t.
    GPIO.cleanup()
