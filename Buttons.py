from tkinter import *
import tkinter.font
import smbus          ##Бібліотека керування I2C шиною
import sys            ##Бібліотека керування I2C шиною
import getopt
import time
import RPi.GPIO as io ##Бібліотека керування GPIO портами

io.setwarnings(False) ##Ігнор помилки GPIO порт зайнятий після попереднього запуску.

bus = smbus.SMBus(1)  ##РОбоча шина в РІ 3  - 1("sudo i2cdetect -y 1" пошук по шині!!!)
DEVICE_1 = 0x20
bus.write_byte_data(0x20,0x00,0x00)     ##Сетап всіх виводів банку А на МСР в output
bus.write_byte_data(0x20,0x01,0x00)     ##Сетап всіх виводів банку B на МСР в output
##bus.write_byte_data(0x20,0x06,0x01)
 

io.setmode(io.BOARD)  ##Змуушуєм працювати GPIO по номеру Піну, а не по назві виходу.
io.setup(40, io.OUT)  ##Пін 40 працює тільки на вихід
io.setup(38, io.OUT)  ##Пін 38 працює тільки на вихід
io.output(40, io.LOW) ##Пін 40 в любому випадку при запуску програми вимкнути клапан.
io.output(38, io.LOW) ##Пін 38 в любому випадку при запуску програми вимкнути клапан.

bus = smbus.SMBus(1)  ##РОбоча шина в РІ 3  - 1("sudo i2cdetect -y 1" пошук по шині!!!)
bus.write_byte_data(0x20,0x00,0x00)     ##Сетап всіх виводів банку А на МСР в output
bus.write_byte_data(0x20,0x01,0x00)     ##Сетап всіх виводів банку B на МСР в output

win = Tk()

myFont = tkinter.font.Font(family = 'Hervetica', size = 12, weight = 'bold')     ##присвоюєм за замовченням стиль та розмір шрифта
smallFont = tkinter.font.Font(family = 'Hervetica', size = 8, weight = 'bold')  ##мій шрифт для малих кнопок
win.title("DNA Switcher")   ##назва вікна
win.geometry("1000x660+25+25")     ##розмір вікна// ('"800x600"+50+50) зміщення по координатах Х та У//

v = StringVar()
#secondpumpvalue = IntVar()

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

def Valve_02(new):
    print("Valve_01 button pressed")               
    old = int(bus.read_byte_data(0x20,0x13))       
    z = old | new
    y = old ^ new
    if old != z:
        bus.write_byte_data(0x20,0x13,z)
        Valve_01_Button["text"] = "Valve 1 ON"
    else:
        bus.write_byte_data(0x20,0x13,y)
        Valve_01_Button["text"] = "Valve 1 OFF"
'''


def Valve_01():
    print("Valve_01 button pressed")
    if io.input(40) :
            io.output(40, io.LOW)
            Valve_01_Button["text"] = "Valve 1 OFF"
           
    else:
            io.output(40, io.HIGH)
            Valve_01_Button["text"] = "Valve 1 ON"
            
            
def Valve_02():
    print("Valve_02 button pressed")
    if io.input(38) :
            io.output(38, io.LOW)
            Valve_02_Button["text"] = "Valve 2 OFF"
                       
    else:
            io.output(38, io.HIGH)
            Valve_02_Button["text"] = "Valve 2 ON"

'''
    
    
    
first_helium_pump_steps_entry_window = Entry(win,textvariable = v) #textvariable = firstpumpvalue)       ##поле введення кількості кроків першого двігла
first_helium_pump_steps_entry_window.pack()
first_helium_pump_steps_entry_window.place(x=600, y=45)

second_helium_pump_steps_entry_window = Entry()#(win, textvariable = secondpumpvalue)      ##поле введення кількості кроків другого двігла
second_helium_pump_steps_entry_window.pack()
second_helium_pump_steps_entry_window.place(x=600, y=154)

exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)   ##Кнопка вихід та її положення
exitButton.pack()
exitButton.place(x=800, y=600)

first_helium_pump_IN = Button(win, text = "pump 1 IN", font = smallFont, command = exitProgram, height = 2, width = 12) ##
first_helium_pump_IN.pack()
first_helium_pump_IN.place(x=800, y=10)

first_helium_pump_OUT = Button(win, text = "pump 1 OUT", font = smallFont, command = exitProgram, height = 2, width = 12) ##
first_helium_pump_OUT.pack()
first_helium_pump_OUT.place(x=800, y=60)

second_helium_pump_IN = Button(win, text = "pump 2 IN", font = smallFont, command = exitProgram, height = 2, width = 12)
second_helium_pump_IN.pack()
second_helium_pump_IN.place(x=800, y=120)

second_helium_pump_OUT = Button(win, text = "pump 2 OUT ", font = smallFont, command = exitProgram, height = 2, width = 12)
second_helium_pump_OUT.pack()
second_helium_pump_OUT.place(x=800, y=170)

################################################ - Розширювач №1

Valve_01_Button = Button(win, text = "Valve 1", font = smallFont, command = lambda:Valve_01(1), height = 2, width = 10)
Valve_01_Button.pack()
Valve_01_Button.place(x=10, y=10)

Valve_02_Button = Button(win, text = "Valve 2", font = smallFont, command = lambda:Valve_01(2), height = 2, width = 10)
Valve_02_Button.pack()
Valve_02_Button.place(x=10, y=50)

Valve_03_Button = Button(win, text = "Valve 3", font = smallFont, command = lambda:Valve_01(4), height = 2, width = 10)
Valve_03_Button.pack()
Valve_03_Button.place(x=10, y=90)

Valve_04_Button = Button(win, text = "Valve 4", font = smallFont, command = lambda:Valve_01(8), height = 2, width = 10)
Valve_04_Button.pack()
Valve_04_Button.place(x=10, y=130)

Valve_05_Button = Button(win, text = "Valve 5", font = smallFont, command = lambda:Valve_01(16), height = 2, width = 10)
Valve_05_Button.pack()
Valve_05_Button.place(x=10, y=170)

Valve_06_Button = Button(win, text = "Valve 6", font = smallFont, command = lambda:Valve_01(32), height = 2, width = 10)
Valve_06_Button.pack()
Valve_06_Button.place(x=10, y=210)

Valve_07_Button = Button(win, text = "Valve 7", font = smallFont, command = lambda:Valve_01(64), height = 2, width = 10)
Valve_07_Button.pack()
Valve_07_Button.place(x=10, y=250)

Valve_08_Button = Button(win, text = "Valve 8", font = smallFont, command = lambda:Valve_01(128), height = 2, width = 10)
Valve_08_Button.pack()
Valve_08_Button.place(x=10, y=290)

Valve_09_Button = Button(win, text = "Valve 9", font = smallFont, command = lambda:Valve_02(1), height = 2, width = 10)
Valve_09_Button.pack()
Valve_09_Button.place(x=10, y=330)

Valve_10_Button = Button(win, text = "Valve 10", font = smallFont, command = lambda:Valve_02(2), height = 2, width = 10)
Valve_10_Button.pack()
Valve_10_Button.place(x=10, y=370)

Valve_11_Button = Button(win, text = "Valve 11", font = smallFont, command = lambda:Valve_02(4), height = 2, width = 10)
Valve_11_Button.pack()
Valve_11_Button.place(x=10, y=410)

Valve_12_Button = Button(win, text = "Valve 12", font = smallFont, command = lambda:Valve_02(8), height = 2, width = 10)
Valve_12_Button.pack()
Valve_12_Button.place(x=10, y=450)

Valve_13_Button = Button(win, text = "Valve 13", font = smallFont, command = lambda:Valve_02(16), height = 2, width = 10)
Valve_13_Button.pack()
Valve_13_Button.place(x=10, y=490)

Valve_14_Button = Button(win, text = "Valve 14", font = smallFont, command = lambda:Valve_02(32), height = 2, width = 10)
Valve_14_Button.pack()
Valve_14_Button.place(x=10, y=530)

Valve_15_Button = Button(win, text = "Valve 15", font = smallFont, command = lambda:Valve_02(64), height = 2, width = 10)
Valve_15_Button.pack()
Valve_15_Button.place(x=10, y=570)

Valve_16_Button = Button(win, text = "Valve 16", font = smallFont, command = lambda:Valve_02(128), height = 2, width = 10)
Valve_16_Button.pack()
Valve_16_Button.place(x=10, y=610)


################################################ - Розширювач №2


Valve_17_Button = Button(win, text = "Valve 17", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_17_Button.pack()
Valve_17_Button.place(x=125, y=10)

Valve_18_Button = Button(win, text = "Valve 18", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_18_Button.pack()
Valve_18_Button.place(x=125, y=50)

Valve_19_Button = Button(win, text = "Valve 19", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_19_Button.pack()
Valve_19_Button.place(x=125, y=90)

Valve_20_Button = Button(win, text = "Valve 20", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_20_Button.pack()
Valve_20_Button.place(x=125, y=130)

Valve_21_Button = Button(win, text = "Valve 21", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_21_Button.pack()
Valve_21_Button.place(x=125, y=170)

Valve_22_Button = Button(win, text = "Valve 22", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_22_Button.pack()
Valve_22_Button.place(x=125, y=210)

Valve_23_Button = Button(win, text = "Valve 23", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_23_Button.pack()
Valve_23_Button.place(x=125, y=250)

Valve_24_Button = Button(win, text = "Valve 24", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_24_Button.pack()
Valve_24_Button.place(x=125, y=290)

Valve_25_Button = Button(win, text = "Valve 25", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_25_Button.pack()
Valve_25_Button.place(x=125, y=330)

Valve_26_Button = Button(win, text = "Valve 26", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_26_Button.pack()
Valve_26_Button.place(x=125, y=370)

Valve_27_Button = Button(win, text = "Valve 27", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_27_Button.pack()
Valve_27_Button.place(x=125, y=410)

Valve_28_Button = Button(win, text = "Valve 28", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_28_Button.pack()
Valve_28_Button.place(x=125, y=450)

Valve_29_Button = Button(win, text = "Valve 29", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_29_Button.pack()
Valve_29_Button.place(x=125, y=490)

Valve_30_Button = Button(win, text = "Valve 30", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_30_Button.pack()
Valve_30_Button.place(x=125, y=530)

Valve_31_Button = Button(win, text = "Valve 31", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_31_Button.pack()
Valve_31_Button.place(x=125, y=570)

Valve_32_Button = Button(win, text = "Valve 32", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_32_Button.pack()
Valve_32_Button.place(x=125, y=610)

################################################ - Розширювач №3

################################################ - Розширювач №4
mainloop()
