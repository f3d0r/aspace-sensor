import serial
import datetime
import csv
ser = serial.Serial('/dev/cu.usbmodem1461', 9600)
while (1):
    serial_line = ser.readline()
    a = (ser.readline().decode("utf-8"))
    rup = datetime.datetime.now().strftime('%m-%d %H:%M:%S')
    a = rup + ','+ a
    print (a.split(','))
    
    myData = a  
    myFile = open('normalRoad.csv', 'a')
    with myFile:
        myFile.write(myData)
    
ser.close()


