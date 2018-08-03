# IMPORTS
from machine import Pin, I2C
import utime
import mag3110

# CONSTANTS
i2c = I2C(scl=Pin(mag3110.SCL_PIN), sda=Pin(mag3110.SDA_PIN), freq=mag3110.I2C_FREQ)

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

def getCurrentMode():
    return mag3110.sys_mode_descriptions[readI2cAddress(mag3110.SYSMOD)[0]]

def reset():
    writeI2cAddress(mag3110.CTRL_REG1, 0)

def setOffset(msbAddress, lsbAddress, offset):
    offset = offset << 1
    writeI2cAddress(msbAddress, int((offset >> 8) & 0xFF))
    utime.sleep_us(15)
    writeI2cAddress(lsbAddress, int(offset & 0xFF))

# TESTING DEVICE
printDivider()

devices = i2c.scan()
print("MAG PRESENT:              ", devices[0] == mag3110.MAG_ADDRESS)
data = readI2cAddress(mag3110.WHO_AM_I)[0]
print("I2C CORRECTLY IDENTIFIED: ", data == mag3110.WHO_AM_I_RESULT)

# INITIALIZATION
writeI2cAddress(mag3110.CTRL_REG1, 0)
utime.sleep(1)

print("DEFAULT MODE:", getCurrentMode())

writeI2cAddress(mag3110.CTRL_REG1, 1)
utime.sleep_us(500)
writeI2cAddress(mag3110.CTRL_REG2, 0x80)

print("NEW MODE:", getCurrentMode())

utime.sleep_us(500)
setOffset(mag3110.OFF_X_MSB, mag3110.OFF_X_LSB, 0)
utime.sleep_us(500)
setOffset(mag3110.OFF_Y_MSB, mag3110.OFF_Y_LSB, 0)
utime.sleep_us(500)
setOffset(mag3110.OFF_Z_MSB, mag3110.OFF_Z_LSB, 0)
utime.sleep_us(500)
writeI2cAddress(mag3110.CTRL_REG1, ((readI2cAddress(mag3110.CTRL_REG1)[0]) | mag3110.MAG3110_ACTIVE_MODE))
utime.sleep(1)

msb = readI2cAddress(mag3110.OUT_X_MSB)[0]
lsb = readI2cAddress(mag3110.OUT_X_LSB)[0]
msbBin = bin(msb)
lsbBin = bin(lsb)
print("X BIN", msbBin, lsbBin)
# print("MSB:\t\t", msb)
# print("MSB BIN:\t", msbBin)
utime.sleep_us(500)
# print("LSB:\t\t", lsb)
# print("LSB BIN:\t", lsbBin)
# print(bin(readI2cAddress(mag3110.CTRL_REG1)[0]))
utime.sleep_us(500)
# print(bin(readI2cAddress(mag3110.CTRL_REG2)[0]))

a  = msb << 8	# MSB
final = a | lsb # LSB
rawVal = (msb * 256) + lsb
print("NO BITWISE X", rawVal)
print("W/ BITWISE X:", int(final))