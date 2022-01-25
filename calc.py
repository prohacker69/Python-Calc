#Ibrahim Mahmud
#Computer science 30
#01/24/22

import tkinter
import math
import random
import os



cc = tkinter.Tk()
cc.title("Simple Calculator")

problem = ""

#Creation of Calulator Functions
def add(value):
    global problem
    problem += value
    bar.config(text=problem)

def reset():
    global problem
    problem = ""
    bar.config(text=problem)
    
def ansr():
    result = eval(problem)
    print(result)

#Bar is th small rectangular area the numbers you input are displayed
bar = tkinter.Label(cc, text="")
bar.grid(row=0, column=0, columnspan=5)

#numbers
one = tkinter.Button(cc, text="1", command=lambda: add("1"))
one.grid(row=1,column=0)
two = tkinter.Button(cc, text="2", command=lambda: add("2"))
two.grid(row=1,column=2)
three = tkinter.Button(cc, text="3", command=lambda: add("3"))
three.grid(row=1,column=3)
four = tkinter.Button(cc, text="4", command=lambda: add("4"))
four.grid(row=2,column=0)
five = tkinter.Button(cc, text="5", command=lambda: add("5"))
five.grid(row=2,column=2)
six = tkinter.Button(cc, text="6", command=lambda: add("6"))
six.grid(row=2,column=3)
seven = tkinter.Button(cc, text="7", command=lambda: add("7"))
seven.grid(row=3,column=0)
eight = tkinter.Button(cc, text="8", command=lambda: add("8"))
eight.grid(row=3,column=2)
nine = tkinter.Button(cc, text="9", command=lambda: add("9"))
nine.grid(row=3,column=3)
zero = tkinter.Button(cc, text="0", command=lambda: add("0"))
zero.grid(row=4,column=2)

#functions 
#division
div = tkinter.Button(cc, text="/", command=lambda: add("/"))
div.grid(row=1,column=4)
#multiplication
mult = tkinter.Button(cc, text="*", command=lambda: add("*"))
mult.grid(row=2,column=4)
#subtractions
minus = tkinter.Button(cc, text="-", command=lambda: add("-"))
minus.grid(row=3,column=4)
#clear/reset
clear = tkinter.Button(cc, text="C", command=lambda: reset())
clear.grid(row=4,column=0)
#decimal point
deci = tkinter.Button(cc, text=".", command=lambda: add("."))
deci.grid(row=4,column=3)
#addition
addit = tkinter.Button(cc, text="+", command=lambda: add("+"))
addit.grid(row=4,column=4)
#equal button or answer button
equal = tkinter.Button(cc, text="=", command=lambda: ansr())
equal.grid(row=5,column=0, rowspan=4)
#pi button
pi = tkinter.Button(cc, text="π", command=lambda: add("3.14159265359"))
pi.grid(row=5,column=2)






cc.mainloop()

   





