# IMPORTS
from machine import Pin, I2C
import ustruct
import utime
import mag3110

# CONSTANTS
i2c = I2C(scl=Pin(mag3110.SCL_PIN), sda=Pin(mag3110.SDA_PIN), freq=mag3110.I2C_FREQ)
multiplexer = 0x70

def printDivider():
    print('------------------------------------------------------------------------------------')

def readI2cAddress(registerAddress, bytes = 1, deviceAddress = mag3110.MAG_ADDRESS):
    data = bytearray(bytes)
    i2c.readfrom_mem_into(deviceAddress, registerAddress, data)
    return data

def writeI2cAddress(registerAddress, writeContents, deviceAddress = mag3110.MAG_ADDRESS):
    writeData = bytearray(1)
    writeData[0] = writeContents
    i2c.writeto_mem(deviceAddress, registerAddress, writeData)

# def writeI2cAddressBuffer(registerAddress, buffer, deviceAddress = mag3110.MAG_ADDRESS):
#     i2c.writeto_mem(deviceAddress, registerAddress, buffer)

def getCurrentMode():
    return mag3110.sys_mode_descriptions[readI2cAddress(mag3110.SYSMOD)[0]]

def reset():
    writeI2cAddress(mag3110.CTRL_REG1, 0)

def setOffset(msbAddress, lsbAddress, offset):
    offset = offset << 1
    writeI2cAddress(msbAddress, int((offset >> 8) & 0xFF))
    utime.sleep_us(15)
    writeI2cAddress(lsbAddress, int(offset & 0xFF))

def readValues(deviceAddress = mag3110.MAG_ADDRESS):
    data = readI2cAddress(mag3110.OUT_X_MSB, 6)
    return [ustruct.unpack_from("<h", data, 0)[0], ustruct.unpack_from("<h", data, 2)[0], ustruct.unpack_from("<h", data, 4)[0]]

def tcaSelect(i):
    data = bytearray(1)
    ustruct.pack_into('<B', data, 0, 1 << i)
    i2c.writeto(multiplexer, data)
    print("SELECTED ADDRESS #", hex(data[0]))

# for addr in range(0, 8):
#     utime.sleep_us(500)
#     tcaSelect(addr)

tcaSelect(0)
utime.sleep_ms(500)
data = readI2cAddress(mag3110.WHO_AM_I, 1, mag3110.MAG_ADDRESS)
utime.sleep_ms(500)
print(data)
tcaSelect(1)
utime.sleep_ms(500)
data = readI2cAddress(mag3110.WHO_AM_I, 1, mag3110.MAG_ADDRESS)
print(data)
tcaSelect(1)
utime.sleep_ms(500)
data = readI2cAddress(mag3110.WHO_AM_I, 1, mag3110.MAG_ADDRESS)
print(data)