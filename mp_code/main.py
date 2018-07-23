# IMPORTS
from machine import Pin, I2C
from time import sleep
import mag3110
import ubinascii

# CONSTANTS
i2c = I2C(scl=Pin(mag3110.SCL_PIN), sda=Pin(mag3110.SDA_PIN), freq=mag3110.I2C_FREQ)

def printDividers():
    print('------------------------------------------------------------------------------------')

def isHex(rawHex):
    return "\\x" in str(rawHex)

def formatHex(rawHex, onlyDecimal = True):
    xIndex = str(rawHex).index("x")
    decimal = (str(rawHex)[xIndex + 1:len(str(rawHex)) - 1]).upper()
    return ("0" + str(rawHex)[3:len(str(rawHex)) - 1]).upper() if not onlyDecimal else decimal

def hexToBinary(rawHex):
    return bin(int(rawHex, 16))[2:]

def hexToInt(rawHex):
    return int(rawHex, 16)

def readI2cAddress(registerAddress, getRaw = True, onlyDecimal = False, deviceAddress = mag3110.MAG_ADDRESS, numBytes = 1):
    data = i2c.readfrom_mem(deviceAddress, registerAddress, numBytes)
    if (getRaw):
        return data
    else:
        return formatHex(data, onlyDecimal)

def writeI2cAddress(registerAddress, writeContents, deviceAddress = mag3110.MAG_ADDRESS):
    i2c.writeto_mem(deviceAddress, registerAddress, writeContents)

def getCurrentMode():
    currentModeBinary = str(hexToBinary(readI2cAddress(mag3110.SYSMOD, False)))
    currentModeIndex = mag3110.sys_mode_binary.index(currentModeBinary)
    return mag3110.sys_mode_descriptions[currentModeIndex]

def mergeHex(hexA, hexB):
    return hexToInt(hexA) * 256 + hexToInt(hexB)

# INITIALIZATION
printDividers()

# TESTING
# data = readI2cAddress(mag3110.WHO_AM_I)

# print("I2C RAW OUTPUT:", data)

# print("CONVERT HEX TO DECIMAL:", hexToInt(data))

# print("CONVERT HEX TO BINARY:", hexToBinary(data))

# print("CURRENT MODE:", getCurrentMode())

writeI2cAddress(mag3110.CTRL_REG1, b'1')
sleep(1)
print(getCurrentMode())

while(1 == 1):
    msb = readI2cAddress(mag3110.OUT_X_MSB)
    lsb = readI2cAddress(mag3110.OUT_X_LSB)
    print("MSB:", msb)
    print("LSB:", lsb)
    printDividers()
    sleep(1.5)

printDividers()