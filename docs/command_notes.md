# Sensor (MAG3110/ESP8266) Command Notes

## Setting Up

`picocom /dev/tty.SLAB_USBtoUART -b115200`
`from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
i2c.scan()`
	Should return [14]
i2c.readfrom_mem(0x0E,0x07, 1) OR i2c.readfrom_mem(14,7, 1)
Should return b'\\xc4'
i2c.readfrom_mem(0x0E,0x00, 18)
b'\\x00\\x94G\*\\x9b\\xfa\\xbd\\xc4\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x0f\\x00\\x00'

Setting the bit in the CTRL_REG1

> > > i2c.writeto_mem(0x0E,0x10, b’\\x01’) - For active mode and get data (Previous function call should return most values as x00)
> > > i2c.writeto_mem(0x0E,0x10, b’\\x02’) - For Fast Read Mode, not good loosing all data, might be helpful for gauging huge changes in vales, might be efficient in flagging car values

ampy --port /dev/tty.SLAB_USBtoUART run main.py
Method to convert bytes in hex to decimal
a = str(i2c.readfrom_mem(0x0E,0x01, 1))			a = “b’\\x94’”
b = str(a[3:6])									b = “x94”
c = “0”+b										c = “0x94”
int(c, 16)										>>> 148

Method to call and convert multiple 
import time
while (True):
	a = str(i2c.readfrom_mem(0x0E,0x01, 1))			a = “b’\\x94’”
	b = str(a[3:6])									b = “x94”
	c = “0”+b										c = “0x94”

    d = str(i2c.readfrom_mem(0x0E,0x05, 1))			a = “b’\x94’”
    e = str(a[3:6])									b = “x94”
    f = “0”+b										c = “0x94”
    print (int(f, 16))

    g = str(i2c.readfrom_mem(0x0E,0x06, 1))			a = “b’\x94’”
    h = str(a[3:6])									b = “x94”
    i = “0”+b										c = “0x94”
    print (int(c, 16), int(f, 16), int(i, 16))
    time.sleep(2) 	# sleep for 2 seconds
