from tkinter import *
import tkinter.font
import RPi.GPIO as io
from time import sleep

io.setwarnings(False)

#color = '#FFFFFF'
win = Tk()
#win.configure(bg=color)
myFont = tkinter.font.Font(family = 'Hervetica', size = 12, weight = 'bold')     ##присвоюєм за замовченням стиль та розмір шрифта
smallFont = tkinter.font.Font(family = 'Hervetica', size = 8, weight = 'bold')  ##мій шрифт для малих кнопок
win.title("SERVO")   ##назва вікна
win.geometry("560x360+25+25")

DIR = 20     ##використовуєм для контакту 20 GPIO контакт. Змінна треба щоб прокручувати двіг в одну чи іншу торону. 
STEP = 21    ##використовуєм для контакту 21 GPIO контакт
CW = 1       ##зміна що обертатиме двигун по часовій стрілці
CCW = 0      ##змінна що обертатиме двигун проти часової стрілки
SPR = 200    ##Прораховано для двигуна у якого один крок 7.5 градусів 360/7.5=48!!!
AUTO = 10



io.setmode(io.BCM)
io.setup(DIR, io.OUT)     ##конфігуруємо контакт 20 для вихлопу
io.setup(STEP, io.OUT)    ##конфігуруємо контакт 21 для вихлопу
io.setup(16, io.OUT)      ##конфігуруємо контакт 16 для вихлопу
io.setup(19, io.OUT)      ##конфігуруємо контакт 19 для вихлопу
io.setup(26, io.OUT)      ##конфігуруємо контакт 21 для вихлопу

io.output(DIR, CW)        ##По іншому було б io.output(20, OUT)// на виході контакту 20 вмикаєм через змінні 1-цю (3.3В)
io.output(26, io.LOW)     ##настройка шагу драйвера(див таблицю по DRV8825)\1\
io.output(19, io.HIGH)    ##настройка шагу драйвера(див таблицю по DRV8825)\0\ зараз 1\8
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
def AUTOMATICAL():
    print('Automatical mode ON')
    for x in range(AUTO):         ##цикл що автоматично виконує вище описані функції одна за одною з перервою в 1с
        COLLECT_HELIUM_1()
        sleep(.05)
        OUT_HELIUM_1()
        sleep(.05)
def exitProgram():
    print("Exit Button pressed")
    io.cleanup()
    win.destroy()

def step_input_1():                 ##Функція змінює глобальну змінну та змінює кількість кроків на введене значення
    global step_count
    step_count = int(step_entry_1.get())
    print("STEP COUNT = ")
    print(step_count)
def step_input_2():                 ##Функція змінює глобальну змінну та змінює кількість кроків на введене значення
    global step_count
    step_count = int(step_entry_2.get())
    print("STEP COUNT = ")
    print(step_count)

    
SetButton_1 = Button(win, text = "SET", font = smallFont, command = step_input_1, height = 1, width = 3)   ##Кнопка вихід та її положення
SetButton_1.pack()
SetButton_1.place(x=320, y=35)

SetButton_2 = Button(win, text = "SET", font = smallFont, command = step_input_2, height = 1, width = 3)   ##Кнопка вихід та її положення
SetButton_2.pack()
SetButton_2.place(x=320, y=125)

step_entry_1 = Entry()
step_entry_1.pack()
step_entry_1.place(x=250, y=39, height = 20, width = 50)

step_entry_2 = Entry()
step_entry_2.pack()
step_entry_2.place(x=250, y=129, height = 20, width = 50)


exitButton = Button(win, text = "EXIT", font = smallFont, command = exitProgram, height = 2, width = 15)
exitButton.pack()
exitButton.place(x=400, y=300)

COLLECT_HELIUM_1_Button = Button(win, text = "COLLECT_HELIUM_1", font = smallFont, command = COLLECT_HELIUM_1, height = 2, width = 15)
COLLECT_HELIUM_1_Button.pack()
COLLECT_HELIUM_1_Button.place(x=400, y=10)

OUT_HELIUM_1_Button = Button(win, text = "OUT_HELIUM_1", font = smallFont, command = OUT_HELIUM_1, height = 2, width = 15)
OUT_HELIUM_1_Button.pack()
OUT_HELIUM_1_Button.place(x=400, y=50)
    
COLLECT_HELIUM_2_Button = Button(win, text = "COLLECT_HELIUM_2", font = smallFont, command = COLLECT_HELIUM_2, height = 2, width = 15)
COLLECT_HELIUM_2_Button.pack()
COLLECT_HELIUM_2_Button.place(x=400, y=100)

OUT_HELIUM_2_Button = Button(win, text = "OUT_HELIUM_2", font = smallFont, command = OUT_HELIUM_2, height = 2, width = 15)
OUT_HELIUM_2_Button.pack()
OUT_HELIUM_2_Button.place(x=400, y=140)

AUTO_Button = Button(win, text = "AUTO", font = smallFont, command = AUTOMATICAL, height = 2, width = 15)
AUTO_Button.pack()
AUTO_Button.place(x=400, y=200)

label_set_value_1 = Label(text= 'step for pump 1:')
label_set_value_1.pack()
label_set_value_1.place(x=120, y=40)

label_set_value_2 = Label(text= 'step for pump 2:')
label_set_value_2.pack()
label_set_value_2.place(x=120, y=130)

left_1 = Label(text= '->')
left_1.pack()
left_1.place(x=300, y=40)

right_2 = Label(text= '->')
right_2.pack()
right_2.place(x=300, y=130)


mainloop()