#ist tkinter trial program see if its ok

from tkinter import *

#open a window
window = Tk()
window.title("Teddys Application")
window.geometry('350x200')


#add a label
lbl = Label(window, text="Hello Ted", font=("Arial Bold", 20))
#lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

#add a button
#btn = Button(window, text="Click Me to stop")
btn = Button(window, text="Click Me to stop", bg="cyan", fg="black")
btn.grid(column=1, row=0)

def clicked():
    lbl.configure(text="Button was clicked !!")
    btn = Button(window, text="Click Me", command=clicked)
    btn.grid(column=1, row=0)
    
window.mainloop()