from tkinter import *
window = Tk()

#set window
window.title("Welcome to Teddys App")
window.geometry('500x200')

#set label
lbl = Label(window, text="Hello", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

#set button click code
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me To Stop", bg="cyan", fg="black", command=clicked)
btn.grid(column=1, row=10)

window.mainloop()