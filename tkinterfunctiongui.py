from tkinter import *

win = Tk()
win.geometry("100x100")
def fun(event):
    print("welcome to knowledge shelf")


button = Button(win,text="click me")           # Command has been used to bind button with function named fun.
button.bind("<Button-1>",fun)
button.pack()





win.mainloop()