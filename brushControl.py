#Code that connects to Arduino and tells it which mode to run on
import serial as piss
import time

ArduinoSerial = piss.Serial('/dev/cu.usbmodem14101',9600)
time.sleep(2)

bot_mode = str(raw_input())
ArduinoSerial.write(bot_mode)