from tkinter import *

window = Tk()
window.title("Tk GUI")
window.minsize(width=400, height=100)


my_label = Label(text="LABEEL", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked():
    my_label.config(text="click, click, click :)")

button = Button(text="click", command=button_clicked)
button.pack()

input = Entry()
input.pack()

window.mainloop()