"""
Updated version of my previous GUI built
Includes trig functions (sin, cos, tan)
Exponents and logarithmic functions
"""

from tkinter import *
import math

class Calculator():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False
    
    def press_button(self, num):
        self.eq = False
        text = text_box.get()
        temp = str(num) 
        if self.new_num:
            self.current = temp
            self.new_num = False 
        else:
        #ensure only one decimal place:
            if temp == ".":
                if temp in text:
                    return
            self.current = text + temp
        #display updated text 
        self.display(self.current)
    # for the = button:
    def calc_total(self):
        try:
            self.eq = True
            self.current = float(self.current)
            if self.op_pending == True:
                self.operations()
            else:
                self.total = float(text_box.get())
        
        except ZeroDivisionError:
            text_box.insert(0, "Error!")
            return None
    
    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def operations(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "subtract":
            self.total -= self.current
        if self.op == "multiply":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "xroot2":
            self.total = self.current**2
        if self.op == "xpowery":
            self.total = self.total ** self.current
        if self.op == "squareroot":
            self.total = math.sqrt(self.total)
        if self.op == "factorial":
            self.total = int(text_box.get())
            self.total = math.factorial(self.total)
        if self.op == "ln":
            self.total = math.log(self.total)
        if self.op == "log":
            self.total = math.log(self.total, 10)
        if self.op == "exp":
            self.total = math.exp(self.total)
        if self.op == "inverse":
            self.total = 1 / self.total
        self.new_num = True
        self.op_pending = False 
        self.display(self.total)
    #some operations needed their own function especially when calc_total is not needed:
    def pi(self):
        self.eq = False 
        self.current = math.pi
        self.display(self.current)

    def sin(self):
        self.eq = False 
        self.current = math.sin(math.radians(float(text_box.get())))
        self.display(self.current)

    def cos(self):
        self.eq = False 
        self.current = math.cos(math.radians(float(text_box.get())))
        self.display(self.current)

    def tan(self):
        self.eq = False 
        self.current = math.tan(math.radians(float(text_box.get())))
        self.display(self.current)

    def solve(self, s):
        self.current = float(self.current)
        if self.op_pending:
            self.operations()
        elif not self.eq:
            self.total = self.current
        self.new_num = True 
        self.op_pending = True
        self.op = s 
        self.eq = False

    def clear(self):
        self.eq = False 
        self.current = "0"
        self.display(0)
        self.new_num = True 
    
    def clear_all(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False 
        self.current = -(float(text_box.get()))
        self.display(self.current)

yay_science = Calculator()
root = Tk()

root.title("Scientific Calculator")
root.geometry("510x280")
root.configure(background="grey")
text_box = Entry(root, justify=RIGHT, width=25, font="Times 16 bold", bd=5)
text_box.grid(row=1, columnspan=8, ipadx=70, ipady=2)
text_box.insert(0, "0")

#creation of all buttons go here:
button_7 = Button(root, text='7', fg='black', bg='royalblue1', height=3,width=7, command=lambda: yay_science.press_button(7))
button_7.grid(row=2, column=0, padx=2, pady=2, sticky="ew")

button_8 = Button(root, text='8', fg='black', bg='royalblue1', height=3,width=7, command=lambda: yay_science.press_button(8))
button_8.grid(row=2, column=1, padx=2, pady=2, sticky="ew")

button_9 = Button(root, text='9', fg='black', bg='royalblue1', height=3,width=7, command=lambda: yay_science.press_button(9))
button_9.grid(row=2, column=2, padx=2, pady=2, sticky="ew")

button_4 = Button(root, text='4', fg='black', bg='royalblue2', height=3,width=7, command=lambda: yay_science.press_button(4))
button_4.grid(row=3, column=0, padx=2, pady=2, sticky="ew")

button_5 = Button(root, text='5', fg='black', bg='royalblue2', height=3,width=7, command=lambda: yay_science.press_button(5))
button_5.grid(row=3, column=1, padx=2, pady=2, sticky="ew")

button_6 = Button(root, text='6', fg='black', bg='royalblue2', height=3,width=7, command=lambda: yay_science.press_button(6))
button_6.grid(row=3, column=2, padx=2, pady=2, sticky="ew")

button_1 = Button(root, text='1', fg='black', bg='blue2', height=3,width=7, command=lambda: yay_science.press_button(1))
button_1.grid(row=4, column=0, padx=2, pady=2, sticky="ew")

button_2 = Button(root, text='2', fg='black', bg='blue2', height=3,width=7, command=lambda: yay_science.press_button(2))
button_2.grid(row=4, column=1, padx=2, pady=2, sticky="ew")

button_3 = Button(root, text='3', fg='black', bg='blue2', height=3,width=7, command=lambda: yay_science.press_button(3))
button_3.grid(row=4, column=2, padx=2, pady=2, sticky="ew")

button_0 = Button(root, text='0', fg='black', bg='blue3', height=3,width=7, command=lambda: yay_science.press_button(0))
button_0.grid(row=5, columnspan=2, padx=2, pady=2, sticky="ew")

button_dot = Button(root, text=' . ', fg='black', bg='blue2', height=3,width=7, command=lambda: yay_science.press_button('.'))
button_dot.grid(row=5, column=2, padx=2, pady=2, sticky="ew")

button_div = Button(root, text=' / ', fg='black', bg='orange', height=3, width=7, command=lambda: yay_science.solve("divide"))
button_div.grid(row=2, column=3, padx=2, pady=2, sticky="ew")

button_mult = Button(root, text=' x ', fg='black', bg='orange', height=3, width=7, command=lambda: yay_science.solve("multiply"))
button_mult.grid(row=3, column=3, padx=2, pady=2, sticky="ew")
# the "-" is so tiny...
button_minus = Button(root, text=' -- ', font="Arial 9", fg='black', bg='orange', height=3, width=7, command=lambda: yay_science.solve("subtract"))
button_minus.grid(row=4, column=3, padx=2, pady=2, sticky="ew")

button_add = Button(root, text=' + ', fg='black', bg='orange', height=3, width=7, command=lambda: yay_science.solve("add"))
button_add.grid(row=5, column=3, padx=2, pady=2, sticky="ew")

button_ac = Button(root, text="AC", fg="black", bg="red", height=3, width=7, command=yay_science.clear_all)
button_ac.grid(row=2, column=4, padx=2, pady=2, sticky="ew")

button_clear = Button(root, text="C", fg="black", bg="yellow", height=3, width=7, command=yay_science.clear)
button_clear.grid(row=3, column=4, padx=2, pady=2, sticky="ew")

button_neg = Button(root, text="+/-", fg="black", bg="orange", height=3, width=7, command=yay_science.sign)
button_neg.grid(row=4, column=4, padx=2, pady=2, sticky="ew")

button_equal = Button(root, text=" = ", fg="black", bg="orange", height=3, width=7, command=yay_science.calc_total)
button_equal.grid(row=5, column=4, padx=2, pady=2, sticky="ew")

button_pi = Button(root, text="pi", fg="black", bg="seagreen1", height=3, width=7, command=yay_science.pi)
button_pi.grid(row=2, column=5, padx=2, pady=2, sticky="ew")

button_sin = Button(root, text="sin", fg="black", bg="seagreen1", height=3, width=7, command=yay_science.sin)
button_sin.grid(row=3, column=5, padx=2, pady=2, sticky="ew")

button_cos = Button(root, text="cos", fg="black", bg="seagreen1", height=3, width=7, command=yay_science.cos)
button_cos.grid(row=4, column=5, padx=2, pady=2, sticky="ew")

button_tan = Button(root, text="tan", fg="black", bg="seagreen1", height=3, width=7, command=yay_science.tan)
button_tan.grid(row=5, column=5, padx=2, pady=2, sticky="ew")

button_x2 = Button(root, text="x^2", fg="black", bg="seagreen2", height=3, width=7, command=lambda: yay_science.solve("xroot2"))
button_x2.grid(row=2, column=6, padx=2, pady=2, sticky="ew")

button_xy = Button(root, text="x^y", fg="black", bg="seagreen2", height=3, width=7, command=lambda: yay_science.solve("xpowery"))
button_xy.grid(row=3, column=6, padx=2, pady=2, sticky="ew")

button_sqrt = Button(root, text="sqrt(x)", fg="black", bg="seagreen2", height=3, width=7, command=lambda: yay_science.solve("squareroot"))
button_sqrt.grid(row=4, column=6, padx=2, pady=2, sticky="ew")

button_fact = Button(root, text="x!", fg="black", bg="seagreen2", height=3, width=7, command=lambda: yay_science.solve("factorial"))
button_fact.grid(row=5, column=6, padx=2, pady=2, sticky="ew")

button_e = Button(root, text="e^x", fg="black", bg="seagreen3", height=3, width=7, command=lambda: yay_science.solve("exp"))
button_e.grid(row=2, column=7, padx=2, pady=2, sticky="ew")

button_ln = Button(root, text="ln", fg="black", bg="seagreen3", height=3, width=7, command=lambda: yay_science.solve("ln"))
button_ln.grid(row=3, column=7, padx=2, pady=2, sticky="ew")

button_log = Button(root, text="log10", fg="black", bg="seagreen3", height=3, width=7, command=lambda: yay_science.solve("log"))
button_log.grid(row=4, column=7, padx=2, pady=2, sticky="ew")

button_inv = Button(root, text="1/x", fg="black", bg="seagreen3", height=3, width=7, command=lambda: yay_science.solve("inverse"))
button_inv.grid(row=5, column=7, padx=2, pady=2, sticky="ew")

if __name__ == '__main__':
    root.mainloop()
