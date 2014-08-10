""" 
sConnection.py
Connect and interact with Serial Port
"""

import serial
import time


class SConnection:
    def __init__(self):
        self.ser = None # serial connection
        
        
    def connectToSerial(self, port):   
        # connect to the serial port 
        try:
            self.ser = serial.Serial(port, 9600)
            time.sleep(2) # extra time is needed on Windows
        except serial.SerialException:
            print 'Unable to connect to serial port'
    
    
    def writeToSerial(self, message):
        # write message to serial
        self.ser.write(message)
    
    
    def closeSerial(self):
        # close serial connection  
        self.ser.close()