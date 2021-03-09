from tkinter import *
import tkinter.font
import RPi.GPIO as io
from time import sleep

io.setwarnings(False)

win = Tk()
myFont = tkinter.font.Font(family = 'Hervetica', size = 12, weight = 'bold')     ##присвоюєм за замовченням стиль та розмір шрифта
smallFont = tkinter.font.Font(family = 'Hervetica', size = 8, weight = 'bold')  ##мій шрифт для малих кнопок
win.title("SERVO")   ##назва вікна
win.geometry("400x200+25+25")

DIR = 20     ##використовуєм для контакту 20 GPIO контакт. Змінна треба щоб прокручувати двіг в одну чи іншу торону. 
STEP = 21    ##використовуєм для контакту 21 GPIO контакт
CW = 1       ##зміна що обертатиме двигун по часовій стрілці
CCW = 0      ##змінна що обертатиме двигун проти часової стрілки
SPR = 200    ##Прораховано для двигуна у якого один крок 7.5 градусів 360/7.5=48!!!

io.setmode(io.BCM)
io.setup(DIR, io.OUT)     ##конфігуруємо контакт 20 для вихлопу
io.setup(STEP, io.OUT)    ##конфігуруємо контакт 21 для вихлопу
io.setup(16, io.OUT)      ##конфігуруємо контакт 16 для вихлопу
io.setup(19, io.OUT)      ##конфігуруємо контакт 19 для вихлопу
io.setup(26, io.OUT)      ##конфігуруємо контакт 21 для вихлопу

io.output(DIR, CW)        ##По іншому було б io.output(20, OUT)// на виході контакту 20 вмикаєм через змінні 1-цю (3.3В)
io.output(26, io.LOW)    ##настройка шагу драйвера(див таблицю по DRV8825)\1\
io.output(19, io.HIGH)     ##настройка шагу драйвера(див таблицю по DRV8825)\0\ зараз 1\8
io.output(16, io.HIGH)    ##настройка шагу драйвера(див таблицю по DRV8825)\1\

step_count = SPR          ##Присвоюєм кількість кроків
delay = .0005             ##Затримка між кроками

def COLLECT_HELIUM_1():
    print("ON Button pressed")
    io.output(DIR, CW)             ##зміна що обертатиме двигун по часовій стрілці
    for x in range(step_count):
        io.output(STEP, io.HIGH)
        sleep(delay)
        io.output(STEP, io.LOW)
        sleep(delay)
        
def COLLECT_HELIUM_2():
    print("ON Button pressed")
    io.output(DIR, CW)             ##зміна що обертатиме двигун по часовій стрілці
    for x in range(step_count):
        io.output(STEP, io.HIGH)
        sleep(delay)
        io.output(STEP, io.LOW)
        sleep(delay)


def OUT_HELIUM_1():
    print("OFF Button pressed")
    io.output(DIR, CCW)            ##змінна що обертатиме двигун проти часової стрілки
    for x in range(step_count):
        io.output(STEP, io.HIGH)
        sleep(delay)
        io.output(STEP, io.LOW)
        sleep(delay)
        
def OUT_HELIUM_2():
    print("OFF Button pressed")
    io.output(DIR, CCW)            ##змінна що обертатиме двигун проти часової стрілки
    for x in range(step_count):
        io.output(STEP, io.HIGH)
        sleep(delay)
        io.output(STEP, io.LOW)
        sleep(delay)
        
def exitProgram():
    print("Exit Button pressed")
    io.cleanup()
    win.destroy()
    
exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)   ##Кнопка вихід та її положення
exitButton.pack()
exitButton.place(x=250, y=140)

COLLECT_HELIUM_1_Button = Button(win, text = "COLLECT_HELIUM_1", font = smallFont, command = COLLECT_HELIUM_1, height = 2, width = 15)
COLLECT_HELIUM_1_Button.pack()
COLLECT_HELIUM_1_Button.place(x=10, y=10)

OUT_HELIUM_1_Button = Button(win, text = "OUT_HELIUM_1", font = smallFont, command = OUT_HELIUM_1, height = 2, width = 15)
OUT_HELIUM_1_Button.pack()
OUT_HELIUM_1_Button.place(x=10, y=50)
    
COLLECT_HELIUM_2_Button = Button(win, text = "COLLECT_HELIUM_2", font = smallFont, command = COLLECT_HELIUM_2, height = 2, width = 15)
COLLECT_HELIUM_2_Button.pack()
COLLECT_HELIUM_2_Button.place(x=10, y=100)

OUT_HELIUM_2_Button = Button(win, text = "OUT_HELIUM_2", font = smallFont, command = OUT_HELIUM_2, height = 2, width = 15)
OUT_HELIUM_2_Button.pack()
OUT_HELIUM_2_Button.place(x=10, y=140)    
    
mainloop()