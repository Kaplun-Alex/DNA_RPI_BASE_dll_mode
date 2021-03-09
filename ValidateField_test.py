from tkinter import *
import tkinter as tk
import tkinter.font

root = Tk()
root.title("MyApp")
smallFont = tkinter.font.Font(family = 'Hervetica', size = 8, weight = 'bold')
root.geometry("400x200+25+25")
myvar = StringVar()

def print_myvar():
    print(myvar.get())

def mywarWritten(*args):
    print ("mywarWritten", myvar.get())
    
    
def step_input():
    step_string_in = text_entry.get()
    step_in = int(step_string_in)
    print(step_in+1)
    
Button = Button(root, text = "myvar_value", font = smallFont, command = step_input, height = 2, width = 15)   ##Кнопка вихід та її положення
Button.pack()
Button.place(x=250, y=140)   
    
myvar.trace("w", mywarWritten)

label = Label(root, textvariable=myvar)
label.pack()

text_entry = Entry()
text_entry.pack()


#class window2:
    #def __init__(self, master1):
       # self.panel2 = tk.Frame(master1)
       # self.panel2.grid()
       # self.button2 = tk.Button(self.panel2, text = "Quit", command = self.panel2.quit)
        #self.button2.grid()
       # vcmd = (master1.register(self.validate),
       #         '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
      #  self.text1 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd)
     #   self.text1.grid()
    #    self.text1.focus()
#
   # def validate(self, action, index, value_if_allowed,
   #                    prior_value, text, validation_type, trigger_type, widget_name):
   #     if text in '0123456789':
   #         try:
    #            float(value_if_allowed)
    #            return True
   #         except ValueError:
  #              return False
 #       else:
#            return False

#root1 = tk.Tk()
#window2(root1)
root.mainloop()