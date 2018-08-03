# IMPORTS
import network
import usocket as _socket
import ussl as ssl
import ubinascii
import utime
import ujson
import urequests

ASPACE_AUTH_KEY = '***REMOVED***'

def printDivider():
    print('------------------------------------------------------------------------------------')

def setupNetwork():
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    if not nic.isconnected():
        nic.connect('bcenter')
        print("Waiting for connection...")
        while not nic.isconnected():
            utime.sleep(1)
    return nic.ifconfig()

def requestTest():
    response = urequests.get('https://api.trya.space/v1')
    return response.json()

def updateSensorStatus(spotID, newOccupancyStatus, authKey = ASPACE_AUTH_KEY):
    response = urequests.post('https://api.trya.space/v1/parking/update_status?spot_id=' + str(spotID) + '&occupied=' + str(newOccupancyStatus) + '&auth_key=' + str(authKey))
    return response.json()

def updateSpotStatusTest():
    updateSensorStatus(841, 'T')
    utime.sleep(2)
    updateSensorStatus(841, 'N')

# TESTING DEVICE
print("NETWORK CONFIG            :", setupNetwork())
setupNetwork()
print("MAC ADDRESS               :", ubinascii.hexlify(network.WLAN().config('mac'),':').decode())
responseData = requestTest()

if (responseData['res_info']['code'] == 30):
    updateSpotStatusTest()
else:
    print("SERVER DIDN'T RESPOND NORMALLY, EXITING...")
# aspacefun.continueWithDataCapture(i2cDev)