from tkinter import *
from OOPLeverage.backend import Database

database = Database("books.db")

def get_selected_row(event):
    global  selectedTuple
    index = listBoxUP.curselection()[0]
    selectedTuple = listBoxUP.get(index)
    #return (selectedTuple)

    #fill in the values when you select
    entryTitle.delete(0,END)
    entryTitle.insert(END, selectedTuple[1])

    entryAuthor.delete(0, END)
    entryAuthor.insert(END, selectedTuple[2])

    entryYear.delete(0,END)
    entryYear.insert(END, selectedTuple[3])

    entryISBN.delete(0, END)
    entryISBN.insert(END, selectedTuple[4])

def view_command():
    listBoxUP.delete(0, END)
    for entry in database.view():
        listBoxUP.insert(END, entry)

def search_command():
    listBoxUP.delete(0, END)
    for entry in database.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        listBoxUP.insert(END, entry)

def add_command():
    #listBox.delete((0,END))
    database.insert(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    listBoxUP.delete(0, END)
    listBoxUP.insert(END, (title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()))

def delete_command():
    database.delete(selectedTuple[0])
    view_command()

def update_command():
    database.update(selectedTuple[0], title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    view_command()



window = Tk()
window.title("Book Store Application")


#create label windows
labelTitle = Label(window, height=1, width=20, text="Title")
labelTitle.grid(row=0, column=0)

labelAuthor = Label(window, height=1, text="Author")
labelAuthor.grid(row=0, column=2)

labelYear = Label(window, height=1, width=20, text="Year")
labelYear.grid(row=1, column=0)

labelISBN = Label(window, height=1, width=20, text="ISBN")
labelISBN.grid(row=1, column=2)

#create entry windows
title_text = StringVar()
entryTitle = Entry(window, textvariable=title_text)
entryTitle.grid(row=0, column=1)

author_text = StringVar()
entryAuthor = Entry(window, textvariable=author_text)
entryAuthor.grid(row=0, column=3)

year_text = StringVar()
entryYear = Entry(window, textvariable=year_text)
entryYear.grid(row=1, column=1)

ISBN_text = StringVar()
entryISBN = Entry(window, textvariable=ISBN_text)
entryISBN.grid(row=1, column=3)

#create List Box
listBoxUP = Listbox(window, height=6, width=35)
listBoxUP.grid(row=2, column=0, rowspan=6, columnspan=2)

#create ScrollBar
scrollBar = Scrollbar(window)
scrollBar.grid(row=2, column=2, rowspan=6)

#bind function to select the list what you are selecting
listBoxUP.bind('<<ListboxSelect>>', get_selected_row)

#create Scrolling for the listBox
listBoxUP.configure(yscrollcommand=scrollBar.set)
scrollBar.configure(command=listBoxUP.yview)

#create Buttons
button_viewAll = Button(window, text="View All", width=12, command=view_command)
button_viewAll.grid(row=2, column=3)

button_searchEntry = Button(window, text="Search Entry", width=12, command=search_command)
button_searchEntry.grid(row=3, column=3)

button_addEntry = Button(window, text="Add Entry", width=12, command=add_command)
button_addEntry.grid(row=4, column=3)

button_update = Button(window, text="Update", width=12, command=update_command)
button_update.grid(row=5, column=3)

button_delete = Button(window, text="Delete", width=12, command=delete_command)
button_delete.grid(row=6, column=3)

button_close = Button(window, text="Close", width=12, command=window.destroy)
button_close.grid(row=7, column=3)

window.mainloop()
