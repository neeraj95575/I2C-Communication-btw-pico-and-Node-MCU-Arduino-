#Code for Raspberry Pi Pico
import utime
import machine
from machine import I2C,Pin

led = machine.Pin(25, machine.Pin.OUT)
led.value(0)

I2C_ADDR = 0x05 #I2C Address of NodeMCU
data = "HELLO_NODEMCU" #Data to send to I2C device

i2c = I2C(0, sda=machine.Pin(8), scl=machine.Pin(9), freq=10000)
print(i2c)
print("Initalizing I2C as Master")

while True:
    i2c.writeto(I2C_ADDR, data) #This line is responsible for sending data to nodemcu 
    a = i2c.readfrom(I2C_ADDR,10) #This line responsible for read data from Nodemcu
    led.value(1)
    print(a)
    utime.sleep(0.1)
    led.value(0)
    utime.sleep(0.1)



