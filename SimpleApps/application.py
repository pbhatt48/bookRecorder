from tkinter import *

#initiate a window
window = Tk()

def km_to_miles():
    print(e1_value.get())
    miles = float(e1_value.get()) * 1.6
    t1.insert(END,miles)


#create a button widget
b1 = Button(window, text="Execute", command=km_to_miles)

#place a button
b1.grid(row=0, column=0)

#create a entry widget
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column =1)

#create a text widget
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column = 2)


window.mainloop()
