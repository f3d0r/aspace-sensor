# IMPORTS
import aspacefun
import i2cfun as i2c
import mag3110
import network
import usocket as _socket
import ussl as ssl
import ubinascii
import utime
from machine import I2C, Pin

# CONSTANTS
i2cDev = I2C(scl=Pin(mag3110.SCL_PIN), sda=Pin(mag3110.SDA_PIN), freq=mag3110.I2C_FREQ)

mlxAddress = 0xc

def printDivider():
    print('------------------------------------------------------------------------------------')

def reset():
    i2c.write(i2cDev, mag3110.CTRL_REG1, 0)

def setupNetwork():
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    if not nic.isconnected():
        nic.connect('bcenter')
        print("Waiting for connection...")
        while not nic.isconnected():
            utime.sleep(1)
    return nic.ifconfig()

def httpGetTest():
    s = _socket.socket()

    ai = _socket.getaddrinfo("api.trya.space", 443)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s = ssl.wrap_socket(s)
    print(s)

    # Both CPython and MicroPython SSLSocket objects support read() and
    # write() methods.
    s.write(b"GET / HTTP/1.0\r\n\r\n")
    print(s.read(4096))

    s.close()

def getByteData(hex):
    readin = bytearray(1)
    readin[0] = hex
    print("HEX:", hex)
    print("REG:", readin)
    print("REG[0]:", readin[0])
    return readin

# TESTING DEVICE
print("DEVICES PRESENT : ", hex(i2cDev.scan()[0]))
i2cDev.start()
print(i2cDev.writeto(mlxAddress, getByteData(0x60)))
utime.sleep_ms(500)
print(i2cDev.writeto(mlxAddress, getByteData(0x00)))
utime.sleep_ms(500)
print(i2cDev.writeto(mlxAddress, getByteData(0x5C)))
utime.sleep_ms(500)
print(i2cDev.writeto(mlxAddress, getByteData(0x00)))
utime.sleep_ms(500)
i2cDev.stop()

status = bytearray(1)
utime.sleep_ms(500)
i2cDev.readfrom_into(mlxAddress, status)
utime.sleep_ms(500)
print("STATUS: " + status[0])

i2cDev.start()
i2cDev.writeto(mlxAddress, getByteData(0x60))
utime.sleep_ms(500)
i2cDev.writeto(mlxAddress, getByteData(0x02))
utime.sleep_ms(500)
i2cDev.writeto(mlxAddress, getByteData(0xB4))
utime.sleep_ms(500)
i2cDev.writeto(mlxAddress, getByteData(0x08))
utime.sleep_ms(500)
i2cDev.stop()

status = bytearray(1)
utime.sleep_ms(500)
i2cDev.readfrom_into(mlxAddress, status)
utime.sleep_ms(500)
print("STATUS: " + status[0])

while (1 == 1):
    data = bytearray(7)

    i2cDev.writeto(mlxAddress, getByteData(0x3E))

    status = bytearray(1)
    i2cDev.readfrom_into(mlxAddress, status)
    print("STATUS: ", status)

    i2cDev.writeto(mlxAddress, getByteData(0x4E))
    i2cDev.readfrom_into(mlxAddress, data)

    xMag = data[1] * 256 + data[2]
    yMag = data[3] * 256 + data[4]
    zMag = data[5] * 256 + data[6]
    
    print("Magnetic Field in X-Axis:", xMag)
    print("Magnetic Field in Y-Axis:", yMag)
    print("Magnetic Field in Z-Axis:", zMag)
    utime.sleep_ms(500)

# try:
#     print("MAG PRESENT               :", i2cDev.scan()[0] == mag3110.MAG_ADDRESS)
#     print("I2C CORRECTLY IDENTIFIED  :",  i2c.read(i2cDev, mag3110.WHO_AM_I)[0] == mag3110.WHO_AM_I_RESULT)
#     print("NETWORK CONFIG            :", setupNetwork())
#     print("MAC ADDRESS               :", ubinascii.hexlify(network.WLAN().config('mac'),':').decode())
#     print("\nWIFI TEST:")
#     httpGetTest()
#     # aspacefun.continueWithDataCapture(i2cDev)
# except IndexError:
    # print("I2C DEVICE/MAG NOT FOUND, EXITING...")