# author: Tyler Elenberger
# date finished: 5/30/2020

from tkinter import *

#setting up the GUI
root = Tk()
root.title("Calculator App")
root.geometry("270x325")
root.configure(background="grey")

#global variable here:
expression = ""

#functionality part of the calculator:
def press(n):
    global expression
    expression = expression + str(n)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set(expression)

def equalto():
    try:
        global expression
        #eval function parses str to calc math result
        total = str(eval(expression))
        #update the new total result
        equation.set(total)
        expression = ""

    #for handling any math errors like dividing by 0:
    except:
        equation.set("Error!")
        expression = ""

#setup for the text entry box; variable expression used to modify equation
equation = StringVar()
text_entry = Entry(root, textvariable=equation, background="gold")
text_entry.grid(row=1, columnspan=4, ipadx=70, ipady=5)
equation.set('enter equation here: ')

#buttons initialized and programmed here:
button_1 = Button(root, text='1', fg='black', bg='gold', height=3,width=7, command=lambda: press(1))
button_1.grid(row=2, column=0)

button_2 = Button(root, text='2', fg='black', bg='gold', height=3,width=7, command=lambda: press(2))
button_2.grid(row=2, column=1)

button_3 = Button(root, text='3', fg='black', bg='gold', height=3,width=7, command=lambda: press(3))
button_3.grid(row=2, column=2)

button_4 = Button(root, text='4', fg='black', bg='gold', height=3,width=7, command=lambda: press(4))
button_4.grid(row=3, column=0)

button_5 = Button(root, text='5', fg='black', bg='gold', height=3,width=7, command=lambda: press(5))
button_5.grid(row=3, column=1)

button_6 = Button(root, text='6', fg='black', bg='gold', height=3,width=7, command=lambda: press(6))
button_6.grid(row=3, column=2)

button_7 = Button(root, text='7', fg='black', bg='gold', height=3,width=7, command=lambda: press(7))
button_7.grid(row=4, column=0)

button_8 = Button(root, text='8', fg='black', bg='gold', height=3,width=7, command=lambda: press(8))
button_8.grid(row=4, column=1)

button_9 = Button(root, text='9', fg='black', bg='gold', height=3,width=7, command=lambda: press(9))
button_9.grid(row=4, column=2)

button_0 = Button(root, text='0', fg='black', bg='gold', height=3, width=7, command=lambda: press(0))
button_0.grid(row=5, column=0)

button_decimal = Button(root, text=' . ', fg='black', bg='gold', height=3, width=7, command=lambda: press('.'))
button_decimal.grid(row=5, column=1)

button_equal = Button(root, text=' = ', fg='black', bg='gold', height=3, width=7, command=equalto)
button_equal.grid(row=5, column=2)

button_add = Button(root, text=' + ', fg='black', bg='yellow', height=3, width=7, command=lambda: press('+'))
button_add.grid(row=2, column=3)

button_subtract = Button(root, text=' - ', fg='black', bg='yellow', height=3, width=7, command=lambda: press('-'))
button_subtract.grid(row=3, column=3)

button_multiply = Button(root, text=' * ', fg='black', bg='yellow', height=3, width=7, command=lambda: press('*'))
button_multiply.grid(row=4, column=3)

button_divide = Button(root, text=' / ', fg='black', bg='yellow', height=3, width=7, command=lambda: press('/'))
button_divide.grid(row=5, column=3)

button_clear = Button(root, text='clear', fg='black', bg='gold', height=3, width=7, command=clear)
button_clear.grid(row=6, column=0)

button_left_par = Button(root, text=" ( ", fg='black', bg='gold', height=3, width=7, command=lambda: press('('))
button_left_par.grid(row=6, column=1)

button_right_par = Button(root, text=" ) ", fg='black', bg='gold', height=3, width=7, command=lambda: press(')'))
button_right_par.grid(row=6, column=2)

#vital in order for GUI to run:
root.mainloop()
