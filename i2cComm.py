from smbus2 import SMBus, i2c_msg
import RPi.GPIO as GPIO
import time

def setup():  
    GPIO.setmode(GPIO.BOARD)  

def loop():
    # Single transaction writing two bytes then read two at address 80
    write = i2c_msg.write(16, [1, 2, 7])
    read = i2c_msg.read(16, 7)
    while True:
        with SMBus(1) as bus:
            bus.i2c_rdwr(write, read)
        data = list(read)
        dist = data[2]|(data[3] << 8)
        print(dist)
        time.sleep(0.5)
    
def destroy():
    GPIO.cleanup()                      

if __name__ == '__main__':     # Program entrance
    print ('Reading TFMini')
    setup()
    try:
        loop()
    finally:
        destroy()



