from tkinter import *
win = Tk()
win.geometry('200x100')

name = Label(win, text="Name")      # To create text label in window
password = Label(win,text="password")
email = Label(win, text="Email ID")
entry_1 = Entry(win)
entry_2 = Entry(win)
entry_3 = Entry(win)
# check = CHECKBUTTON(win,text ="keep me logged in")
name.grid(row=0, sticky = E)
password.grid(row=1,sticky = E)
email.grid(row=2, sticky = E)
entry_1.grid(row=0, column =1)
entry_2.grid(row=1, column =1)
entry_3.grid(row=2, column =1)


# check.grid(columnspan=2)







win.mainloop()