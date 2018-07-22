# This is your main script.

from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
print('initialized')