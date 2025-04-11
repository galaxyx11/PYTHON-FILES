from tkinter import *

#trial 2 set window
window = Tk()
window.title("TEDS APP")
window.geometry('350x200')

#set label
lbl = Label(window, text="Hello Ted",font=("Arial Bold", 20))
lbl.grid(column=0, row=0)



#code for button click go's here
def clicked():
    lbl.configure(text="Button was clicked !!")
    btn = Button(window, text="Click Me", command=clicked)
    btn.grid(column=1, row=0)

window.mainloop()