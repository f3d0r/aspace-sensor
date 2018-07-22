import serial
import datetime
import csv
ser = serial.Serial('/dev/cu.usbmodem1461', 9600)



while (1):
    serial_line = ser.readline()
    #print(serial_line) # If using Python 2.x use: print serial_line
    # Do some other work on the data

    # sleep 5 minutes

    # Loop restarts once the sleep is finished
##    f = open('example.csv','wl')
##    f.write()
##    f.close()
    a = (ser.readline().decode("utf-8"))
    rup = datetime.datetime.now().strftime('%m-%d %H:%M:%S')
    #print (rup)
    a = rup + ','+ a
    #print (a)
    print (a.split(','))
    
    myData = a  
    #with myFile:  
        #writer = csv.writer(myFile)
        #writer.writerows(myData)
    myFile = open('hoolibeb2.csv', 'a')
    with myFile:
        myFile.write(myData)
    
ser.close()

# code delay function.
# code timer !

