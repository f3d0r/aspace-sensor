import i2cfun as i2c
import mag3110
import ustruct
import utime

def getCurrentMode(i2cDev):
    return mag3110.sys_mode_descriptions[i2c.read(i2cDev, mag3110.SYSMOD)[0]]

def setOffset(i2cDev, msbAddress, lsbAddress, offset):
    offset = offset << 1
    i2c.write(i2cDev, msbAddress, int((offset >> 8) & 0xFF))
    utime.sleep_us(15)
    i2c.write(i2cDev, lsbAddress, int(offset & 0xFF))

def readValues(i2cDev, deviceAddress = mag3110.MAG_ADDRESS):
    data = i2c.read(i2cDev, mag3110.OUT_X_MSB, 6)
    return [ustruct.unpack_from("<H", data, 0)[0], ustruct.unpack_from("<H", data, 2)[0], ustruct.unpack_from("<H", data, 4)[0]]

def continueWithDataCapture(i2cDev):
    # INITIALIZATION
    print("DEFAULT MODE:", getCurrentMode(i2cDev))
    i2c.write(i2cDev, mag3110.CTRL_REG1, 0x00)
    utime.sleep_us(500)
    i2c.write(i2cDev, mag3110.CTRL_REG2, 0x80)
    print("NEW MODE:", getCurrentMode(i2cDev))

    utime.sleep_us(500)
    setOffset(i2cDev, mag3110.OFF_X_MSB, mag3110.OFF_X_LSB, 0)
    utime.sleep_us(500)
    setOffset(i2cDev, mag3110.OFF_Y_MSB, mag3110.OFF_Y_LSB, 0)
    utime.sleep_us(500)
    setOffset(i2cDev, mag3110.OFF_Z_MSB, mag3110.OFF_Z_LSB, 0)
    utime.sleep_us(500)
    i2c.write(i2cDev, mag3110.CTRL_REG1, ((i2c.read(i2cDev, mag3110.CTRL_REG1)[0]) | mag3110.MAG3110_ACTIVE_MODE))
    utime.sleep(1)

    count = 1
    while (1 == 1):
        print(count, ":", readValues(i2cDev))
        count += 1
        utime.sleep(1)
