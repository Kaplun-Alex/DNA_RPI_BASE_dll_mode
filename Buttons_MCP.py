from tkinter import *
import tkinter.font
import smbus          ##Бібліотека керування I2C шиною
import sys            ##Бібліотека керування I2C шиною
import getopt
from time import sleep
import RPi.GPIO as io ##Бібліотека керування GPIO портами

io.setwarnings(False) ##Ігнор помилки GPIO порт зайнятий після попереднього запуску.

bus = smbus.SMBus(1)  ##РОбоча шина в РІ 3  - 1("sudo i2cdetect -y 1" пошук по шині!!!)
DEVICE_1 = 0x20
bus.write_byte_data(0x20,0x00,0x00)     ##Сетап всіх виводів банку А на МСР в output
bus.write_byte_data(0x20,0x01,0x00)     ##Сетап всіх виводів банку B на МСР в output

win = Tk()

myFont = tkinter.font.Font(family = 'Hervetica', size = 12, weight = 'bold')     ##присвоюєм за замовченням стиль та розмір шрифта
smallFont = tkinter.font.Font(family = 'Hervetica', size = 8, weight = 'bold')  ##мій шрифт для малих кнопок
win.title("DNA Switcher")   ##назва вікна
win.geometry("450x220+25+25")     ##розмір вікна// ('"800x600"+50+50) зміщення по координатах Х та У//


def exitProgram():
    print("Exit Button pressed")
    io.cleanup()
    win.destroy()

def Valve_01(new):
    print("Valve_01 button pressed")               
    old = int(bus.read_byte_data(0x20,0x12))       
    z = old | new
    y = old ^ new
    if old != z:
        bus.write_byte_data(0x20,0x12,z)
        Valve_01_Button["text"] = "Valve 1 ON"
    else:
        bus.write_byte_data(0x20,0x12,y)
        Valve_01_Button["text"] = "Valve 1 OFF"
    
   
   # bus.write_byte_data(0x20,0x12,z)


exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)   ##Кнопка вихід та її положення
exitButton.pack()
exitButton.place(x=300, y=150)

Valve_01_Button = Button(win, text = "Valve 1", font = smallFont, command = lambda:Valve_01(2), height = 2, width = 10)  ##command = lambda:Valve_01(64)
Valve_01_Button.pack()
Valve_01_Button.place(x=10, y=50)


mainloop() 