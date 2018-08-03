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

def httpGetTest():
    s = _socket.socket()

    ai = _socket.getaddrinfo("api.trya.space", 443)
    # print("Address infos:", ai)
    addr = ai[0][-1]

    # print("Connect address:", addr)
    s.connect(addr)

    s = ssl.wrap_socket(s)
    print(s)

    s.write(b"GET /v1 HTTP/1.0\r\n\r\n")
    res = s.read(4096)
    jsonRes = ujson.loads(res)
    print(jsonRes)
    s.close()

def requestTest():
    response = urequests.get('https://api.trya.space/v1')
    return response.json()

def updateSensorStatus(spotID, newOccupancyStatus, authKey = ASPACE_AUTH_KEY):
    response = urequests.post('https://api.trya.space/v1/parking/update_status?spot_id=' + str(spotID) + '&occupied=' + str(newOccupancyStatus) + '&auth_key=' + str(authKey))
    return response.json()

# TESTING DEVICE
# print("NETWORK CONFIG            :", setupNetwork())
setupNetwork()
# print("MAC ADDRESS               :", ubinascii.hexlify(network.WLAN().config('mac'),':').decode())
# print("\nWIFI TEST:")
responseData = requestTest()
print("RESPONSE_INFO:",responseData['res_info']['code_info'])
print("RESPONSE_CODE:",responseData['res_info']['code'])
updateSpotResponse = updateSensorStatus(841, 'T')
utime.sleep(5)
updateSpotResponse = updateSensorStatus(841, 'F')
utime.sleep(5)
updateSpotResponse = updateSensorStatus(841, 'N')
# httpGetTest()
# aspacefun.continueWithDataCapture(i2cDev)