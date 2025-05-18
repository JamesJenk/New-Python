#!/bin/python3 

# Python program to Scan and Read a QR code
from qrtools import QR

my_QR = QR(filename = "MyQRCode1.png")
  
# decodes the QR code and returns True if successful
my_QR.decode()
  
# prints the data
print (my_QR.data)