import serial
import json

ser = serial.Serial('COM5', baudrate = 9600, timeout = 1)

if not ser.isOpen():
    ser.open()
print('com3 is open', ser.isOpen())

while True:
    try:
        arduinoData = ser.readline().decode('ascii')
        datajson = json.loads(arduinoData)
        data1 = datajson['data1']
        data2 = datajson['data2']
        print(datajson)
    except:
        continue

