#Communication

import serial

def Connect(COM,Baud):
    ser=serial.Serial("COM%d" % COM,Baud)
    return(ser)

def Send(s,ser):
    s_bytes=bytes(s,encoding='utf-8')
    State=ser.write(s_bytes)
    if State:
        print("Success")
    else:
        print("Failed")
    return

def Catch(ser):
    s=ser.read().decode('utf-8')
    message=s.split()
    string=''
    for letter in message:
        string+=chr(int(letter))
    return letter


ser=Connect(12,9600)
