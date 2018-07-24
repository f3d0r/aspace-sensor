import serial
import datetime
import csv
from time import sleep
import keyboard
import sys
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

current_state = "0"
f = open('human.csv','a')
f.write("\n")
f.write("\n")
f.write("\n")
f.write("\n")

while (not keyboard.is_pressed('c')):
    serial_line = ser.readline()

    a = (ser.readline().decode("utf-8")).strip()

    a = a.replace(' ', ',')    

    try: #used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):
            current_state = "1"
        elif keyboard.is_pressed('w'):
            current_state = "0"
    except:
        pass
    a = a + ("," + current_state)
    print(a)
    f.write(a + "\n")
    sleep(0.1)
    
ser.close()
f.close()