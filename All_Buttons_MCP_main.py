from tkinter import *
import tkinter.font
import smbus          ##Бібліотека керування I2C шиною
import sys            ##Бібліотека керування I2C шиною
import getopt
import time
import RPi.GPIO as io ##Бібліотека керування GPIO портами
from time import sleep
io.setwarnings(False) ##Ігнор помилки GPIO порт зайнятий після попереднього запуску.


##------------------------------------------------------------------РЕЗЕРВ КОНФІГУРУВАННЯ GPIO ВИВОДІВ
#io.setmode(io.BOARD)  ##Змуушуєм працювати GPIO по номеру Піну, а не по назві виходу.
#io.setup(40, io.OUT)  ##Пін 40 працює тільки на вихід
#io.setup(38, io.OUT)  ##Пін 38 працює тільки на вихід
#io.output(40, io.LOW) ##Пін 40 в любому випадку при запуску програми вимкнути клапан.
#io.output(38, io.LOW) ##Пін 38 в любому випадку при запуску програми вимкнути клапан.


##------------------------------------------------------------------КОНФІГУРУВАННЯ ШИНИ І2С
bus = smbus.SMBus(1)  ##РОбоча шина в РІ 3  - 1("sudo i2cdetect -y 1" пошук по шині!!!)
bus.write_byte_data(0x20,0x00,0x00)     ##Сетап всіх виводів чіпу 20 банку А на МСР в output
bus.write_byte_data(0x20,0x06,0x00)
bus.write_byte_data(0x20,0x01,0x00)     ##Сетап всіх виводів чіпу 20 банку B на МСР в output
bus.write_byte_data(0x20,0x06,0x00)
bus.write_byte_data(0x21,0x00,0x00)     ##Сетап всіх виводів чіпу 21 банку А на МСР в output
bus.write_byte_data(0x21,0x06,0x00)
bus.write_byte_data(0x21,0x01,0x00)     ##Сетап всіх виводів чіпу 21 банку B на МСР в output
bus.write_byte_data(0x21,0x06,0x00)
bus.write_byte_data(0x22,0x00,0x00)     ##Сетап всіх виводів чіпу 22 банку А на МСР в output
bus.write_byte_data(0x22,0x06,0x00)
bus.write_byte_data(0x22,0x01,0x00)     ##Сетап всіх виводів чіпу 22 банку B на МСР в output
bus.write_byte_data(0x22,0x06,0x00)
bus.write_byte_data(0x23,0x00,0x00)     ##Сетап всіх виводів чіпу 23 банку А на МСР в output
bus.write_byte_data(0x23,0x06,0x00)
bus.write_byte_data(0x23,0x01,0x00)     ##Сетап всіх виводів чіпу 23 банку B на МСР в output
bus.write_byte_data(0x23,0x06,0x00)


##------------------------------------------------------------------ЗМІННІ ДЛЯ СЕРВОПРИВОДУ
DIR = 20     ##використовуєм для контакту 20 GPIO контакт. Змінна треба щоб прокручувати двіг в одну чи іншу торону. 
STEP = 21    ##використовуєм для контакту 21 GPIO контакт
CW = 1       ##зміна що обертатиме двигун по часовій стрілці
CCW = 0      ##змінна що обертатиме двигун проти часової стрілки
SPR = 200    ##Прораховано для двигуна у якого один крок 7.5 градусів 360/7.5=48!!!
AUTO = 10


##------------------------------------------------------------------КОНФІГУРУВАННЯ ШИНИ КЕРУВАННЯ СЕРВОПРИВОДОМ
io.setmode(io.BCM)
io.setup(DIR, io.OUT)     ##конфігуруємо контакт 20 для вихлопу
io.setup(STEP, io.OUT)    ##конфігуруємо контакт 21 для вихлопу
io.setup(16, io.OUT)      ##конфігуруємо контакт 16 для вихлопу
io.setup(19, io.OUT)      ##конфігуруємо контакт 19 для вихлопу
io.setup(26, io.OUT)      ##конфігуруємо контакт 21 для вихлопу
io.setup(5, io.IN)

io.output(DIR, CW)        ##По іншому було б io.output(20, OUT)// на виході контакту 20 вмикаєм через змінні 1-цю (3.3В)
io.output(26, io.LOW)     ##настройка шагу драйвера(див таблицю по DRV8825)\1\
io.output(19, io.HIGH)    ##настройка шагу драйвера(див таблицю по DRV8825)\0\ зараз 1\8
io.output(16, io.HIGH)    ##настройка шагу драйвера(див таблицю по DRV8825)\1\

step_count = SPR          ##Присвоюєм кількість кроків
delay = .0005             ##Затримка між кроками


##-------------------------------------------------------------------ФУНКЦІЇ КЕРУВАННЯ СЕРВОПРИВОДОМ
def COLLECT_HELIUM_1():
    print("ON Button pressed")
    io.output(DIR, CW)             ##зміна що обертатиме двигун по часовій стрілці
    for x in range(step_count):
        if io.input(5) == 1:
            print("PUMP FULL")
            break
        io.output(STEP, io.HIGH)
        sleep(delay)
        io.output(STEP, io.LOW)
        sleep(delay)
def COLLECT_HELIUM_2():
    print("ON Button pressed")
    io.output(DIR, CW)             ##зміна що обертатиме двигун по часовій стрілці
    for x in range(step_count):
        if io.input(5) == 1:
            print("PUMP FULL")
            break
        io.output(STEP, io.HIGH)
        sleep(delay)
        io.output(STEP, io.LOW)
        sleep(delay)
def OUT_HELIUM_1():
    print("OFF Button pressed")
    io.output(DIR, CCW)            ##змінна що обертатиме двигун проти часової стрілки
    for x in range(step_count):
        if io.input(5) == 1:
            print("PUMP EMPTY")
            break
        io.output(STEP, io.HIGH)
        sleep(delay)
        io.output(STEP, io.LOW)
        sleep(delay)
def OUT_HELIUM_2():
    print("OFF Button pressed")
    io.output(DIR, CCW)            ##змінна що обертатиме двигун проти часової стрілки
    for x in range(step_count):
        if io.input(5) == 1:
            print("PUMP EMPTY")
            break
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


##---------------------------------------------------------------ФУНКЦІЇ КНОПОК/КЛАПАНІВ
   
def Valve_0x20_0x12(new,mcpadr):
    print("Valve_01 button pressed")
    old = 0
    z = 0
    y = 0
    old = int(bus.read_byte_data(mcpadr,0x12))
    print(old)
    print(mcpadr)
    z = old | new
    y = old ^ new
    if old != z:
        bus.write_byte_data(mcpadr,0x12,z)

    else:
        bus.write_byte_data(mcpadr,0x12,y)


def Valve_0x20_0x13(new,mcpadr):
    print("Valve_01 button pressed")
    old = 0
    z = 0
    y = 0
    old = int(bus.read_byte_data(mcpadr,0x13))
    print(old)
    print(mcpadr)
    z = old | new
    y = old ^ new
    if old != z:
        bus.write_byte_data(mcpadr,0x13,z)

    else:
        bus.write_byte_data(mcpadr,0x13,y)
        
def Close_All_Valve():
    bus.write_byte_data(0x20,0x12,0)
    bus.write_byte_data(0x20,0x13,0)
    bus.write_byte_data(0x21,0x12,0)
    bus.write_byte_data(0x21,0x13,0)
    bus.write_byte_data(0x22,0x12,0)
    bus.write_byte_data(0x22,0x13,0)
    bus.write_byte_data(0x23,0x12,0)
    bus.write_byte_data(0x23,0x13,0)
    print ('Close all valve')
    
##  def clearing_system():
def FUN():
    for x in range(1,256):
        bus.write_byte_data(0x20,0x12,x)
        sleep(0.05)
        bus.write_byte_data(0x20,0x13,x)
        sleep(0.05)
        bus.write_byte_data(0x21,0x12,x)
        sleep(0.05)
        bus.write_byte_data(0x21,0x13,x)
        sleep(0.05)
        bus.write_byte_data(0x22,0x12,x)
        sleep(0.05)
        bus.write_byte_data(0x22,0x13,x)
        sleep(0.05)
        bus.write_byte_data(0x23,0x12,x)
        sleep(0.05)
        bus.write_byte_data(0x23,0x13,x)
        sleep(0.05)
        
              
def exitProgram():
    print("Exit Button pressed")
    io.cleanup()
    win.destroy()

win = Tk()

myFont = tkinter.font.Font(family = 'Hervetica', size = 12, weight = 'bold')     ##присвоюєм за замовченням стиль та розмір шрифта
smallFont = tkinter.font.Font(family = 'Hervetica', size = 8, weight = 'bold')  ##мій шрифт для малих кнопок
win.title("DNA Switcher")   ##назва вікна
win.geometry("1000x660+25+25")     ##розмір вікна// ('"800x600"+50+50) зміщення по координатах Х та У//    
    
exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)   ##Кнопка вихід та її положення
exitButton.pack()
exitButton.place(x=800, y=600)



##-----------------------------------------------------------------КНОПКИ ЗМІНИ КРОКІВ СЕРВОПРИВРОДІВ
SetButton_1 = Button(win, text = "SET", font = smallFont, command = step_input_1, height = 1, width = 3)   ##Кнопка вихід та її положення
SetButton_1.pack()
SetButton_1.place(x=670, y=35)

SetButton_2 = Button(win, text = "SET", font = smallFont, command = step_input_2, height = 1, width = 3)   ##Кнопка вихід та її положення
SetButton_2.pack()
SetButton_2.place(x=670, y=125)

##-----------------------------------------------------------------ПОЛЯ ВНЕСЕНЯ КРОКІВ СЕРВОПРИВРОДІВ
step_entry_1 = Entry()
step_entry_1.pack()
step_entry_1.place(x=600, y=39, height = 20, width = 50)

step_entry_2 = Entry()
step_entry_2.pack()
step_entry_2.place(x=600, y=129, height = 20, width = 50)

##-----------------------------------------------------------------КНОПКИ КЕРУВАННЯ СЕРВОПРИВОДОМ ВГОРУ/ВНИЗ
COLLECT_HELIUM_1_Button = Button(win, text = "COLLECT_HELIUM_1", font = smallFont, command = COLLECT_HELIUM_1, height = 2, width = 15)
COLLECT_HELIUM_1_Button.pack()
COLLECT_HELIUM_1_Button.place(x=750, y=10)

OUT_HELIUM_1_Button = Button(win, text = "OUT_HELIUM_1", font = smallFont, command = OUT_HELIUM_1, height = 2, width = 15)
OUT_HELIUM_1_Button.pack()
OUT_HELIUM_1_Button.place(x=750, y=50)
    
COLLECT_HELIUM_2_Button = Button(win, text = "COLLECT_HELIUM_2", font = smallFont, command = COLLECT_HELIUM_2, height = 2, width = 15)
COLLECT_HELIUM_2_Button.pack()
COLLECT_HELIUM_2_Button.place(x=750, y=100)

OUT_HELIUM_2_Button = Button(win, text = "OUT_HELIUM_2", font = smallFont, command = OUT_HELIUM_2, height = 2, width = 15)
OUT_HELIUM_2_Button.pack()
OUT_HELIUM_2_Button.place(x=750, y=140)

##-----------------------------------------------------------------НАДПИСИ ТА СТРІЛКИ В ПРОГРАМІ
label_set_value_1 = Label(text= 'step for pump 1:')
label_set_value_1.pack()
label_set_value_1.place(x=480, y=40)

label_set_value_2 = Label(text= 'step for pump 2:')
label_set_value_2.pack()
label_set_value_2.place(x=480, y=130)

left_1 = Label(text= '->')
left_1.pack()
left_1.place(x=650, y=40)

right_2 = Label(text= '->')
right_2.pack()
right_2.place(x=650, y=130)

##------------------------------------------------------------------КНОПКИ РОЗШИРЮВАЧА №1 0x20

Valve_01_Button = Button(win, text = "Valve 1", font = smallFont, command = lambda:Valve_0x20_0x12(1,0x20), height = 2, width = 10)
Valve_01_Button.pack()
Valve_01_Button.place(x=10, y=10)

Valve_02_Button = Button(win, text = "Valve 2", font = smallFont, command = lambda:Valve_0x20_0x12(2,0x20), height = 2, width = 10)
Valve_02_Button.pack()
Valve_02_Button.place(x=10, y=50)

Valve_03_Button = Button(win, text = "Valve 3", font = smallFont, command = lambda:Valve_0x20_0x12(4,0x20), height = 2, width = 10)
Valve_03_Button.pack()
Valve_03_Button.place(x=10, y=90)

Valve_04_Button = Button(win, text = "Valve 4", font = smallFont, command = lambda:Valve_0x20_0x12(8,0x20), height = 2, width = 10)
Valve_04_Button.pack()
Valve_04_Button.place(x=10, y=130)

Valve_05_Button = Button(win, text = "Valve 5", font = smallFont, command = lambda:Valve_0x20_0x12(16,0x20), height = 2, width = 10)
Valve_05_Button.pack()
Valve_05_Button.place(x=10, y=170)

Valve_06_Button = Button(win, text = "Valve 6", font = smallFont, command = lambda:Valve_0x20_0x12(32,0x20), height = 2, width = 10)
Valve_06_Button.pack()
Valve_06_Button.place(x=10, y=210)

Valve_07_Button = Button(win, text = "Valve 7", font = smallFont, command = lambda:Valve_0x20_0x12(64,0x20), height = 2, width = 10)
Valve_07_Button.pack()
Valve_07_Button.place(x=10, y=250)

Valve_08_Button = Button(win, text = "Valve 8", font = smallFont, command = lambda:Valve_0x20_0x12(128,0x20), height = 2, width = 10)
Valve_08_Button.pack()
Valve_08_Button.place(x=10, y=290)

Valve_09_Button = Button(win, text = "Valve 9", font = smallFont, command = lambda:Valve_0x20_0x13(1,0x20), height = 2, width = 10)
Valve_09_Button.pack()
Valve_09_Button.place(x=10, y=330)

Valve_10_Button = Button(win, text = "Valve 10", font = smallFont, command = lambda:Valve_0x20_0x13(2,0x20), height = 2, width = 10)
Valve_10_Button.pack()
Valve_10_Button.place(x=10, y=370)

Valve_11_Button = Button(win, text = "Valve 11", font = smallFont, command = lambda:Valve_0x20_0x13(4,0x20), height = 2, width = 10)
Valve_11_Button.pack()
Valve_11_Button.place(x=10, y=410)

Valve_12_Button = Button(win, text = "Valve 12", font = smallFont, command = lambda:Valve_0x20_0x13(8,0x20), height = 2, width = 10)
Valve_12_Button.pack()
Valve_12_Button.place(x=10, y=450)

Valve_13_Button = Button(win, text = "Valve 13", font = smallFont, command = lambda:Valve_0x20_0x13(16,0x20), height = 2, width = 10)
Valve_13_Button.pack()
Valve_13_Button.place(x=10, y=490)

Valve_14_Button = Button(win, text = "Valve 14", font = smallFont, command = lambda:Valve_0x20_0x13(32,0x20), height = 2, width = 10)
Valve_14_Button.pack()
Valve_14_Button.place(x=10, y=530)

Valve_15_Button = Button(win, text = "Valve 15", font = smallFont, command = lambda:Valve_0x20_0x13(64,0x20), height = 2, width = 10)
Valve_15_Button.pack()
Valve_15_Button.place(x=10, y=570)

Valve_16_Button = Button(win, text = "Valve 16", font = smallFont, command = lambda:Valve_0x20_0x13(128,0x20), height = 2, width = 10)
Valve_16_Button.pack()
Valve_16_Button.place(x=10, y=610)


##------------------------------------------------------------------КНОПКИ РОЗШИРЮВАЧА №2 0x21

Valve_17_Button = Button(win, text = "Valve 17", font = smallFont, command = lambda:Valve_0x20_0x12(1,0x21), height = 2, width = 10)
Valve_17_Button.pack()
Valve_17_Button.place(x=130, y=10)

Valve_18_Button = Button(win, text = "Valve 18", font = smallFont, command = lambda:Valve_0x20_0x12(2,0x21), height = 2, width = 10)
Valve_18_Button.pack()
Valve_18_Button.place(x=130, y=50)

Valve_19_Button = Button(win, text = "Valve 19", font = smallFont, command = lambda:Valve_0x20_0x12(4,0x21), height = 2, width = 10)
Valve_19_Button.pack()
Valve_19_Button.place(x=130, y=90)

Valve_20_Button = Button(win, text = "Valve 20", font = smallFont, command = lambda:Valve_0x20_0x12(8,0x21), height = 2, width = 10)
Valve_20_Button.pack()
Valve_20_Button.place(x=130, y=130)

Valve_21_Button = Button(win, text = "Valve 21", font = smallFont, command = lambda:Valve_0x20_0x12(16,0x21), height = 2, width = 10)
Valve_21_Button.pack()
Valve_21_Button.place(x=130, y=170)

Valve_22_Button = Button(win, text = "Valve 22", font = smallFont, command = lambda:Valve_0x20_0x12(32,0x21), height = 2, width = 10)
Valve_22_Button.pack()
Valve_22_Button.place(x=130, y=210)

Valve_23_Button = Button(win, text = "Valve 23", font = smallFont, command = lambda:Valve_0x20_0x12(64,0x21), height = 2, width = 10)
Valve_23_Button.pack()
Valve_23_Button.place(x=130, y=250)

Valve_24_Button = Button(win, text = "Valve 24", font = smallFont, command = lambda:Valve_0x20_0x12(128,0x21), height = 2, width = 10)
Valve_24_Button.pack()
Valve_24_Button.place(x=130, y=290)

Valve_25_Button = Button(win, text = "Valve 25", font = smallFont, command = lambda:Valve_0x20_0x13(1,0x21), height = 2, width = 10)
Valve_25_Button.pack()
Valve_25_Button.place(x=130, y=330)

Valve_26_Button = Button(win, text = "Valve 26", font = smallFont, command = lambda:Valve_0x20_0x13(2,0x21), height = 2, width = 10)
Valve_26_Button.pack()
Valve_26_Button.place(x=130, y=370)

Valve_27_Button = Button(win, text = "Valve 27", font = smallFont, command = lambda:Valve_0x20_0x13(4,0x21), height = 2, width = 10)
Valve_27_Button.pack()
Valve_27_Button.place(x=130, y=410)

Valve_28_Button = Button(win, text = "Valve 28", font = smallFont, command = lambda:Valve_0x20_0x13(8,0x21), height = 2, width = 10)
Valve_28_Button.pack()
Valve_28_Button.place(x=130, y=450)

Valve_29_Button = Button(win, text = "Valve 29", font = smallFont, command = lambda:Valve_0x20_0x13(16,0x21), height = 2, width = 10)
Valve_29_Button.pack()
Valve_29_Button.place(x=130, y=490)

Valve_30_Button = Button(win, text = "Valve 30", font = smallFont, command = lambda:Valve_0x20_0x13(32,0x21), height = 2, width = 10)
Valve_30_Button.pack()
Valve_30_Button.place(x=130, y=530)

Valve_31_Button = Button(win, text = "Valve 31", font = smallFont, command = lambda:Valve_0x20_0x13(64,0x21), height = 2, width = 10)
Valve_31_Button.pack()
Valve_31_Button.place(x=130, y=570)

Valve_32_Button = Button(win, text = "Valve 32", font = smallFont, command = lambda:Valve_0x20_0x13(128,0x21), height = 2, width = 10)
Valve_32_Button.pack()
Valve_32_Button.place(x=130, y=610)


##------------------------------------------------------------------КНОПКИ РОЗШИРЮВАЧА №3 0x22

Valve_17_Button = Button(win, text = "Valve 17", font = smallFont, command = lambda:Valve_0x20_0x12(1,0x22), height = 2, width = 10)
Valve_17_Button.pack()
Valve_17_Button.place(x=250, y=10)

Valve_18_Button = Button(win, text = "Valve 18", font = smallFont, command = lambda:Valve_0x20_0x12(2,0x22), height = 2, width = 10)
Valve_18_Button.pack()
Valve_18_Button.place(x=250, y=50)

Valve_19_Button = Button(win, text = "Valve 19", font = smallFont, command = lambda:Valve_0x20_0x12(4,0x22), height = 2, width = 10)
Valve_19_Button.pack()
Valve_19_Button.place(x=250, y=90)

Valve_20_Button = Button(win, text = "Valve 20", font = smallFont, command = lambda:Valve_0x20_0x12(8,0x22), height = 2, width = 10)
Valve_20_Button.pack()
Valve_20_Button.place(x=250, y=130)

Valve_21_Button = Button(win, text = "Valve 21", font = smallFont, command = lambda:Valve_0x20_0x12(16,0x22), height = 2, width = 10)
Valve_21_Button.pack()
Valve_21_Button.place(x=250, y=170)

Valve_22_Button = Button(win, text = "Valve 22", font = smallFont, command = lambda:Valve_0x20_0x12(32,0x22), height = 2, width = 10)
Valve_22_Button.pack()
Valve_22_Button.place(x=250, y=210)

Valve_23_Button = Button(win, text = "Valve 23", font = smallFont, command = lambda:Valve_0x20_0x12(64,0x22), height = 2, width = 10)
Valve_23_Button.pack()
Valve_23_Button.place(x=250, y=250)

Valve_24_Button = Button(win, text = "Valve 24", font = smallFont, command = lambda:Valve_0x20_0x12(128,0x22), height = 2, width = 10)
Valve_24_Button.pack()
Valve_24_Button.place(x=250, y=290)

Valve_25_Button = Button(win, text = "Valve 25", font = smallFont, command = lambda:Valve_0x20_0x13(1,0x22), height = 2, width = 10)
Valve_25_Button.pack()
Valve_25_Button.place(x=250, y=330)

Valve_26_Button = Button(win, text = "Valve 26", font = smallFont, command = lambda:Valve_0x20_0x13(2,0x22), height = 2, width = 10)
Valve_26_Button.pack()
Valve_26_Button.place(x=250, y=370)

Valve_27_Button = Button(win, text = "Valve 27", font = smallFont, command = lambda:Valve_0x20_0x13(4,0x22), height = 2, width = 10)
Valve_27_Button.pack()
Valve_27_Button.place(x=250, y=410)

Valve_28_Button = Button(win, text = "Valve 28", font = smallFont, command = lambda:Valve_0x20_0x13(8,0x22), height = 2, width = 10)
Valve_28_Button.pack()
Valve_28_Button.place(x=250, y=450)

Valve_29_Button = Button(win, text = "Valve 29", font = smallFont, command = lambda:Valve_0x20_0x13(16,0x22), height = 2, width = 10)
Valve_29_Button.pack()
Valve_29_Button.place(x=250, y=490)

Valve_30_Button = Button(win, text = "Valve 30", font = smallFont, command = lambda:Valve_0x20_0x13(32,0x22), height = 2, width = 10)
Valve_30_Button.pack()
Valve_30_Button.place(x=250, y=530)

Valve_31_Button = Button(win, text = "Valve 31", font = smallFont, command = lambda:Valve_0x20_0x13(64,0x22), height = 2, width = 10)
Valve_31_Button.pack()
Valve_31_Button.place(x=250, y=570)

Valve_32_Button = Button(win, text = "Valve 32", font = smallFont, command = lambda:Valve_0x20_0x13(128,0x22), height = 2, width = 10)
Valve_32_Button.pack()
Valve_32_Button.place(x=250, y=610)



##------------------------------------------------------------------КНОПКИ РОЗШИРЮВАЧА №4 0x23

Valve_17_Button = Button(win, text = "Valve 17", font = smallFont, command = lambda:Valve_0x20_0x12(1,0x23), height = 2, width = 10)
Valve_17_Button.pack()
Valve_17_Button.place(x=370, y=10)

Valve_18_Button = Button(win, text = "Valve 18", font = smallFont, command = lambda:Valve_0x20_0x12(2,0x23), height = 2, width = 10)
Valve_18_Button.pack()
Valve_18_Button.place(x=370, y=50)

Valve_19_Button = Button(win, text = "Valve 19", font = smallFont, command = lambda:Valve_0x20_0x12(4,0x23), height = 2, width = 10)
Valve_19_Button.pack()
Valve_19_Button.place(x=370, y=90)

Valve_20_Button = Button(win, text = "Valve 20", font = smallFont, command = lambda:Valve_0x20_0x12(8,0x23), height = 2, width = 10)
Valve_20_Button.pack()
Valve_20_Button.place(x=370, y=130)

Valve_21_Button = Button(win, text = "Valve 21", font = smallFont, command = lambda:Valve_0x20_0x12(16,0x23), height = 2, width = 10)
Valve_21_Button.pack()
Valve_21_Button.place(x=370, y=170)

Valve_22_Button = Button(win, text = "Valve 22", font = smallFont, command = lambda:Valve_0x20_0x12(32,0x23), height = 2, width = 10)
Valve_22_Button.pack()
Valve_22_Button.place(x=370, y=210)

Valve_23_Button = Button(win, text = "Valve 23", font = smallFont, command = lambda:Valve_0x20_0x12(64,0x23), height = 2, width = 10)
Valve_23_Button.pack()
Valve_23_Button.place(x=370, y=250)

Valve_24_Button = Button(win, text = "Valve 24", font = smallFont, command = lambda:Valve_0x20_0x12(128,0x23), height = 2, width = 10)
Valve_24_Button.pack()
Valve_24_Button.place(x=370, y=290)

Valve_25_Button = Button(win, text = "Valve 25", font = smallFont, command = lambda:Valve_0x20_0x13(1,0x23), height = 2, width = 10)
Valve_25_Button.pack()
Valve_25_Button.place(x=370, y=330)

Valve_26_Button = Button(win, text = "Valve 26", font = smallFont, command = lambda:Valve_0x20_0x13(2,0x23), height = 2, width = 10)
Valve_26_Button.pack()
Valve_26_Button.place(x=370, y=370)

Valve_27_Button = Button(win, text = "Valve 27", font = smallFont, command = lambda:Valve_0x20_0x13(4,0x23), height = 2, width = 10)
Valve_27_Button.pack()
Valve_27_Button.place(x=370, y=410)

Valve_28_Button = Button(win, text = "Valve 28", font = smallFont, command = lambda:Valve_0x20_0x13(8,0x23), height = 2, width = 10)
Valve_28_Button.pack()
Valve_28_Button.place(x=370, y=450)

Valve_29_Button = Button(win, text = "Valve 29", font = smallFont, command = lambda:Valve_0x20_0x13(16,0x23), height = 2, width = 10)
Valve_29_Button.pack()
Valve_29_Button.place(x=370, y=490)

Valve_30_Button = Button(win, text = "Valve 30", font = smallFont, command = lambda:Valve_0x20_0x13(32,0x23), height = 2, width = 10)
Valve_30_Button.pack()
Valve_30_Button.place(x=370, y=530)

Valve_31_Button = Button(win, text = "Valve 31", font = smallFont, command = lambda:Valve_0x20_0x13(64,0x23), height = 2, width = 10)
Valve_31_Button.pack()
Valve_31_Button.place(x=370, y=570)

Valve_32_Button = Button(win, text = "Valve 32", font = smallFont, command = lambda:Valve_0x20_0x13(128,0x23), height = 2, width = 10)
Valve_32_Button.pack()
Valve_32_Button.place(x=370, y=610)

##--------------------------------------

Clear_System_Button = Button(win, text = "Clear System", font = smallFont, command = Close_All_Valve, height = 2, width = 10)
Clear_System_Button.pack()
Clear_System_Button.place(x=550, y=530)

Close_All_Valve_Button = Button(win, text = "Close All Valve", font = smallFont, command = Close_All_Valve, height = 2, width = 10)
Close_All_Valve_Button.pack()
Close_All_Valve_Button.place(x=550, y=610)

FUN_Button = Button(win, text = "FUN", font = smallFont, command = FUN, height = 2, width = 10)
FUN_Button.pack()
FUN_Button.place(x=550, y=450)

mainloop()
