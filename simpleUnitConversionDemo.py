from tkinter import *

#initiate a window
window =Tk()

#function for conversion
def conversion():
    grams = float(e1_val.get()) * 1000
    tGram.insert(END, grams)

    pounds = float(e1_val.get()) * 2.20463
    tPounds.insert(END, pounds)

    ounces = float(e1_val.get()) * 35.274
    tOunces.insert(END, ounces)

#label window
labelBar = Label(window, height=1, width=20, text="KG")
labelBar.grid(row=0, column=0)


#instantite a button
b1 = Button(window, text="Convert", command=conversion)
#place a button
b1.grid(row=0, column=2)

#instantiate a Entry
e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)

#instantiate a text widget
tGram= Text(window, height= 1, width = 20)
tGram.grid(row=1,column=0)

tPounds = Text(window, height=1, width=20)
tPounds.grid(row=1, column=1)

tOunces = Text(window, height=1, width=20)
tOunces.grid(row=1, column=2)

window.mainloop()
