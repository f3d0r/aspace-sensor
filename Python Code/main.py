import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)
while (1 == 1):
    pin.on()
    time.sleep(0.1)
    pin.off()
    time.sleep(0.1)
