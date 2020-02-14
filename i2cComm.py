from smbus2 import SMBus, i2c_msg

# Single transaction writing two bytes then read two at address 80
write = i2c_msg.write(16, [1, 2, 7])
read = i2c_msg.read(16, 7)
with SMBus(1) as bus:
    bus.i2c_rdwr(write, read)