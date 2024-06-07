from tkinter import *
from tkinter import ttk
import random

w = Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

w["bg"] = '#2F4F4F'
w.geometry("700x400")
w.resizable(height=False, width=False)

start = Button(text='НАДРУКУВАТИ ТАБЛИЧКУ МНОЖЕННЯ', bg="#0B615E", width=49)
start.place(x=15, y=10)

l1 = Label(width=15).place(x=15, y=50)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=45)
enter1 = Entry(width=4, ).place(x=150, y=50)

l2 = Label(width=15).place(x=15,y=75)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=70)
enter1 = Entry(width=4, ).place(x=150, y=75)

l3 = Label(width=15).place(x=15,y=100)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=95)
enter1 = Entry(width=4, ).place(x=150, y=100)

l4 = Label(width=15).place(x=15,y=125)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=120)
enter1 = Entry(width=4, ).place(x=150, y=125)

l5 = Label(width=15).place(x=15,y=150)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=145)
enter1 = Entry(width=4, ).place(x=150, y=150)

l6 = Label(width=15).place(x=15,y=175)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=170)
enter1 = Entry(width=4, ).place(x=150, y=175)

l7 = Label(width=15).place(x=15,y=200)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=195)
enter1 = Entry(width=4, ).place(x=150, y=200)

l8 = Label(width=15).place(x=15,y=225)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=220)
enter1 = Entry(width=4, ).place(x=150, y=225)

l9 = Label(width=15).place(x=15,y=250)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=245)
enter1 = Entry(width=4, ).place(x=150, y=250)

l10 = Label(width=15).place(x=15,y=275)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=270)
enter1 = Entry(width=4, ).place(x=150, y=275)

l11 = Label(width=15).place(x=210,y=50)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=45)
enter1 = Entry(width=4, ).place(x=335, y=50)

l12 = Label(width=15).place(x=210,y=75)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=70)
enter1 = Entry(width=4, ).place(x=335, y=75)

l13 = Label(width=15).place(x=210,y=100)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=95)
enter1 = Entry(width=4, ).place(x=335, y=100)

l14 = Label(width=15).place(x=210,y=125)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=120)
enter1 = Entry(width=4, ).place(x=335, y=125)

l15 = Label(width=15).place(x=210,y=150)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=145)
enter1 = Entry(width=4, ).place(x=335, y=150)

l16 = Label(width=15).place(x=210,y=175)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=170)
enter1 = Entry(width=4, ).place(x=335, y=175)

l17 = Label(width=15).place(x=210,y=200)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=195)
enter1 = Entry(width=4, ).place(x=335, y=200)

l18 = Label(width=15).place(x=210,y=225)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=220)
enter1 = Entry(width=4, ).place(x=335, y=225)

l19 = Label(width=15).place(x=210,y=250)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=245)
enter1 = Entry(width=4, ).place(x=335, y=250)

l20 = Label(width=15).place(x=210,y=275)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=270)
enter1 = Entry(width=4, ).place(x=335, y=275)


w.mainloop()