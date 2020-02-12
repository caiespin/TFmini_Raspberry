import RPi.GPIO as GPIO
import time

relayPin = 32     # define the relayPin

def setup():    
    GPIO.setmode(GPIO.BOARD)       
    GPIO.setup(relayPin, GPIO.OUT)   # set relayPin to OUTPUT mode

def loop():
    GPIO.output(relayPin,True)
    print ("Relay on")
    time.sleep(5)
    GPIO.output(relayPin,False)
    print ("Relay off")
    
def destroy():
    GPIO.cleanup()                      

if __name__ == '__main__':     # Program entrance
    print ('Reseting TFmini at pin '+str(relayPin)+'...')
    setup()
    try:
        loop()
    finally:
        destroy()