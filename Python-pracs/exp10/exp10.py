import math
from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Number 1:')
        self.lbl2 = Label(win, text='Number 2:')
        self.lbl3 = Label(win, text='Result')
        self.lbl4 = Label(win, text="")
        self.lbl6 = Label(win, text="")
        self.t1 = Entry(bd=3)
        self.t2 = Entry(bd=3)
        self.t3 = Entry(bd=3)

        self.lbl6.grid(row=0, column=0, columnspan=3, ipadx=20)
        self.lbl1.grid(row=1, column=0, columnspan=1, ipadx=20)
        self.t1.grid(row=1, column=1, columnspan=1, ipadx=20)
        self.lbl2.grid(row=2, column=0, columnspan=1, ipadx=20)
        self.t2.grid(row=2, column=1, columnspan=1, ipadx=20)
        self.lbl4.grid(row=3, column=0, columnspan=3, ipadx=20)

        self.b1 = Button(win, text='Add', width=10)
        self.b1.bind('<Button-1>', self.add)
        self.b2 = Button(win, text='Subtract', width=10)
        self.b2.bind('<Button-1>', self.sub)
        self.b3 = Button(win, text='Multiply', width=10)
        self.b3.bind('<Button-1>', self.mul)
        self.b4 = Button(win, text='Divide', width=10)
        self.b4.bind('<Button-1>', self.div)
        self.b5 = Button(win, text='Modulus', width=10)
        self.b5.bind('<Button-1>', self.mod)
        self.b6 = Button(win, text='Sqrt', width=10)
        self.b6.bind('<Button-1>', self.sqroot)
        self.b7 = Button(win, text='Sin', width=10)
        self.b7.bind('<Button-1>', self.sine)
        self.b8 = Button(win, text='Cos', width=10)
        self.b8.bind('<Button-1>', self.cosine)
        self.b9 = Button(win, text='Tan', width=10)
        self.b9.bind('<Button-1>', self.tangent)
        self.b10 = Button(win, text='Power', width=10)
        self.b10.bind('<Button-1>', self.power)

        self.b1.grid(row=4, column=0, columnspan=1, ipadx=20)
        self.b2.grid(row=4, column=1, columnspan=1, ipadx=20)
        self.b3.grid(row=4, column=2, columnspan=1, ipadx=20)
        self.b4.grid(row=5, column=0, columnspan=1, ipadx=20)
        self.b5.grid(row=5, column=1, columnspan=1, ipadx=20)
        self.b6.grid(row=5, column=2, columnspan=1, ipadx=20)
        self.b7.grid(row=6, column=0, columnspan=1, ipadx=20)
        self.b8.grid(row=6, column=1, columnspan=1, ipadx=20)
        self.b9.grid(row=6, column=2, columnspan=1, ipadx=20)
        self.b10.grid(row=7, column=1, columnspan=1, ipadx=20)

        self.lbl5 = Label(win, text="")
        self.lbl5.grid(row=8, column=0, columnspan=1, ipadx=20)
        self.lbl3.grid(row=9, column=0, columnspan=1, ipadx=20)
        self.t3.grid(row=9, column=1, columnspan=1, ipadx=20)

    def add(self, event):
        self.t2.config(state='normal')
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t2.config(state='normal')
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def mul(self, event):
        self.t2.config(state='normal')
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def div(self, event):
        self.t2.config(state='normal')
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 / num2
        self.t3.insert(END, str(result))

    def mod(self, event):
        self.t2.config(state='normal')
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 % num2
        self.t3.insert(END, str(result))

    def sqroot(self, event):
        self.t2.config(state='disabled')
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        result = math.sqrt(num1)
        self.t3.insert(END, str(round(result, 4)))

    def sine(self, event):
        self.t2.config(state='disabled')
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        result = math.sin(num1 * (math.pi / 180))
        self.t3.insert(END, str(round(result, 4)))

    def cosine(self, event):
        self.t2.config(state='disabled')
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        result = math.cos(num1 * (math.pi / 180))
        self.t3.insert(END, str(round(result, 4)))

    def tangent(self, event):
        self.t2.config(state='disabled')
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        result = math.tan(num1 * (math.pi / 180))
        self.t3.insert(END, str(round(result, 4)))

    def power(self, event):
        self.t2.config(state='normal')
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = pow(num1, num2)
        self.t3.insert(END, str(result))

window = Tk()
mywin = MyWindow(window)
window.title('Calculator')
window.geometry("420x260+10+10")
window.mainloop()
