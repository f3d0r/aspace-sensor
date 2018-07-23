# IMPORTS
from machine import Pin, I2C
import ustruct
import ubinascii
import mag3110

# CONSTANTS
i2c = I2C(scl=Pin(mag3110.SCL_PIN), sda=Pin(mag3110.SDA_PIN), freq=mag3110.I2C_FREQ)

def printDividers():
    for x in range(1):
        print('------------------------------------------------------------------------------------')

# RETURNS FULL HEX, FORMATTED
def formatHex(rawHex, onlyDecimal = True):
    xIndex = str(rawHex).index("x")
    decimal = (str(rawHex)[xIndex + 1:len(str(rawHex)) - 1]).upper()
    return ("0" + str(rawHex)[3:len(str(rawHex)) - 1]).upper() if not onlyDecimal else decimal

def hexToBinary(rawHex):
    return bin(int(rawHex, 16))[2:]

def hexToInt(rawHex):
    return int(data, 16)

def readI2cAddress(registerAddress, onlyDecimal = False, magAddress = mag3110.MAG_ADDRESS, numBytes = 1):
    return formatHex(i2c.readfrom_mem(magAddress, registerAddress, numBytes), onlyDecimal)

def getCurrentMode():
    currentModeBinary = str(hexToBinary(readI2cAddress(mag3110.SYSMOD)))
    currentModeIndex = mag3110.sys_mode_binary.index(currentModeBinary)
    return mag3110.sys_mode_descriptions[currentModeIndex]

# INITIALIZATION
printDividers()

# TESTING
data = readI2cAddress(mag3110.WHO_AM_I)

print("I2C RAW OUTPUT: ", data)

print("CONVERT HEX TO DECIMAL: ", hexToInt(data))

print("CONVERT HEX TO BINARY: ", hexToBinary(data))

print("CURRENT MODE: ", getCurrentMode())

printDividers()