import RPi.GPIO as GPIO

relayPin = 32     # define the relayPin

def setup():    
    GPIO.setmode(GPIO.BOARD)       
    GPIO.setup(relayPin, GPIO.OUT)   # set relayPin to OUTPUT mode

def loop(state):
    if state == 'off':
        relayState = True
    else:
        relayState = False
    GPIO.output(relayPin,relayState)

    
def destroy():
    GPIO.cleanup()                      

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()