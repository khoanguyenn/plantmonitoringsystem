//main
import serial #Khai bao thu vien Serial
from time import sleep #Khai bao lenh sleep tu thu vien time
ser = serial.Serial('/dev/ttyACM0',9600)
def sendAndReceive(reqData):
 while True:
 if (ser.in_waiting>0):
 resData = str(ser.readline().decode('ASCII'))
#Get & decode data received
 return resData
 else:
 reqData += "\r"
ser.write(reqData.encode())
sleep(0.5)
