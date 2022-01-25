#functions 
#division
def functions():
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
