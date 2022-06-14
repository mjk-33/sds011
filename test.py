from cProfile import label
from turtle import color
import serial
import struct
from datetime import datetime
import variables as v

ser = serial.Serial(port=v.port, baudrate=v.baudrate, stopbits=v.stopbits, timeout=v.timeout, parity=v.parity)

while True:
        data = ser.read(10)
        decoded = struct.unpack(v.UMPACK_PAT, data)
        measure_time = datetime.now()
        formated_time = measure_time.strftime("%Y-%m-%d %H:%M:%S")
        pm25 = decoded[2] / 10.0
        pm10 = decoded[3] / 10.0
        print(f'{formated_time}         PM2.5 = {pm25}           PM10 = {pm10}')

