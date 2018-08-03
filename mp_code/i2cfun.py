import mag3110

def read(i2c, registerAddress, bytes = 1, deviceAddress = mag3110.MAG_ADDRESS):
    data = bytearray(bytes)
    i2c.readfrom_mem_into(deviceAddress, registerAddress, data)
    return data

def write(i2c, registerAddress, writeContents, deviceAddress = mag3110.MAG_ADDRESS):
    writeData = bytearray(1)
    writeData[0] = writeContents
    i2c.writeto_mem(deviceAddress, registerAddress, writeData)