from tkinter import *
import tkinter.font
import random
import time
import RPi.GPIO as io

io.setwarnings(False) ##Ігнор помилки GPIO порт зайнятий після попереднього запуску.

io.setmode(io.BOARD)  ##Змуушуєм працювати GPIO по номеру Піну, а не по назві виходу.
io.setup(40, io.OUT)  ##Пін 40 працює тільки на вихід
io.setup(38, io.OUT)  ##Пін 38 працює тільки на вихід
io.output(40, io.LOW) ##Пін 40 в любому випадку при запуску програми вимкнути клапан.
io.output(38, io.LOW) ##Пін 38 в любому випадку при запуску програми вимкнути клапан.

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

            
def get_value():
    print(v.get())
     
def clean_value():
    v.set("")
    


def validate(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if text in '0123456789':
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return False



##class Pump:
    def __init__(self, master1):
        vcmd = (master1.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.pump_steps_field = Entry(win, validate = 'key', validatecommand = vcmd)
        self.pump_steps_field.pack()
        
    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789':
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
        
##helium_pump_1 = Pump()
##helium.

first_helium_pump_steps_entry_window = Entry(win,textvariable = v, validate = 'key', validatecommand = validate('%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')) #textvariable = firstpumpvalue)       ##поле введення кількості кроків першого двігла
first_helium_pump_steps_entry_window.pack()
first_helium_pump_steps_entry_window.place(x=600, y=45)

second_helium_pump_steps_entry_window = Entry()#(win, textvariable = secondpumpvalue)      ##поле введення кількості кроків другого двігла
second_helium_pump_steps_entry_window.pack()
second_helium_pump_steps_entry_window.place(x=600, y=154)

exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)   ##Кнопка вихід та її оложення
exitButton.pack()
exitButton.place(x=800, y=600)

first_helium_pump_IN = Button(win, text = "pump 1 IN", font = smallFont, command = get_value, height = 2, width = 12) ##
first_helium_pump_IN.pack()
first_helium_pump_IN.place(x=800, y=10)

first_helium_pump_OUT = Button(win, text = "pump 1 OUT", font = smallFont, command = clean_value, height = 2, width = 12) ##
first_helium_pump_OUT.pack()
first_helium_pump_OUT.place(x=800, y=60)

second_helium_pump_IN = Button(win, text = "pump 2 IN", font = smallFont, command = exitProgram, height = 2, width = 12)
second_helium_pump_IN.pack()
second_helium_pump_IN.place(x=800, y=120)

second_helium_pump_OUT = Button(win, text = "pump 2 OUT ", font = smallFont, command = exitProgram, height = 2, width = 12)
second_helium_pump_OUT.pack()
second_helium_pump_OUT.place(x=800, y=170)

Valve_01_Button = Button(win, text = "Valve 1", font = smallFont, command = Valve_01, height = 2, width = 10)
Valve_01_Button.pack()
Valve_01_Button.place(x=10, y=10)

Valve_02_Button = Button(win, text = "Valve 2", font = smallFont, command = Valve_02, height = 2, width = 10)
Valve_02_Button.pack()
Valve_02_Button.place(x=10, y=50)

Valve_03_Button = Button(win, text = "Valve 3", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_03_Button.pack()
Valve_03_Button.place(x=10, y=90)

Valve_04_Button = Button(win, text = "Valve 4", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_04_Button.pack()
Valve_04_Button.place(x=10, y=130)

Valve_05_Button = Button(win, text = "Valve 5", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_05_Button.pack()
Valve_05_Button.place(x=10, y=170)

Valve_06_Button = Button(win, text = "Valve 6", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_06_Button.pack()
Valve_06_Button.place(x=10, y=210)

Valve_07_Button = Button(win, text = "Valve 7", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_07_Button.pack()
Valve_07_Button.place(x=10, y=250)

Valve_08_Button = Button(win, text = "Valve 8", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_08_Button.pack()
Valve_08_Button.place(x=10, y=290)

Valve_09_Button = Button(win, text = "Valve 9", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_09_Button.pack()
Valve_09_Button.place(x=10, y=330)

Valve_10_Button = Button(win, text = "Valve 10", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_10_Button.pack()
Valve_10_Button.place(x=10, y=370)

Valve_11_Button = Button(win, text = "Valve 11", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_11_Button.pack()
Valve_11_Button.place(x=10, y=410)

Valve_12_Button = Button(win, text = "Valve 12", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_12_Button.pack()
Valve_12_Button.place(x=10, y=450)

Valve_13_Button = Button(win, text = "Valve 13", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_13_Button.pack()
Valve_13_Button.place(x=10, y=490)

Valve_14_Button = Button(win, text = "Valve 14", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_14_Button.pack()
Valve_14_Button.place(x=10, y=530)

Valve_15_Button = Button(win, text = "Valve 15", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_15_Button.pack()
Valve_15_Button.place(x=10, y=570)

Valve_16_Button = Button(win, text = "Valve 16", font = smallFont, command = exitProgram, height = 2, width = 10)
Valve_16_Button.pack()
Valve_16_Button.place(x=10, y=610)

win.mainloop()
