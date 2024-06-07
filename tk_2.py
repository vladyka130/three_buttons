import random
from tkinter import *

w = Tk()
w["bg"] = '#2F4F4F'
w.geometry("500x300")
w.resizable(height=False, width=False)

text = Label(w, text='-First Programm-', font='Verdana 14', fg='black', bg="#0F4F4F")
text.pack(side="top")

text2 = Label(w, text='ANY_TEXT', font='Verdana 14', fg='black', bg="#2F4F4F")
#text2.place(x=195, y=135)

def f1():
    text2.configure(text="cliced_1")
def f2():
    text2.configure(text="cliced_2")
def f3():
    text2.configure(text="cliced_3")
def reset():
    text2['text'] = entry.get()

first_btn = Button(text="1", width=30, command=f1)
first_btn.place(x=139, y=30)

second_btn = Button(text="2", width=30, command=f2)
second_btn.place(x=139, y=65)

thred_btn = Button(text="3", width=30, command=f3)
thred_btn.place(x=139, y=100)

reset = Button(text="RESET", width=30, command=reset)
reset.place(x=139, y=165)

entry = Entry(width=35)
entry.place(x=140, y=195)

text2.place(x=200,y=130)


w.mainloop()


