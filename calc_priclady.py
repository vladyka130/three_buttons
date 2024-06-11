from tkinter import *
import random
import smtplib
import customtkinter


w = Tk()
w.title('Табличка множення для Арсена v.1.0')
w["bg"] = '#2F4F4F'
w.geometry("700x500")
w.resizable(height=False, width=False)
frame = Frame().place(x=14, y=48)

start = Button(text='ПОКАЗАТИ ПРИКЛАДИ', bg="#0B615E", width=49)                       #command=tabl
start.place(x=15, y=10)
proverka = Button(text='ПЕРЕВІРТИ РЕЗУЛЬТАТИ', bg="#0B615E", width=41, state=DISABLED) #command=proverka)
proverka.place(x=390, y=10)

priclady_Label, symbol_ravno, answer_Entry = [], [], []

x_priclady, y_priclady, x_ravno, y_ravno = 16, 50, 240, 45
for i in range(15):
    priclady_Label.append(Label(width=30, text='', background='#A9F5D0', relief='ridge'))
    priclady_Label[i].place(x=x_priclady, y=y_priclady)
    symbol_ravno.append(Label(background='#2F4F4F', text='=', font=1))
    symbol_ravno[i].place(x=x_ravno, y=y_ravno)
    answer_Entry.append(Entry(width=16, background='#A9F5D0', relief='solid'))
    answer_Entry[i].place(x=x_priclady+250, y=y_priclady+1)
    y_ravno += 25
    y_priclady += 25

w.mainloop()
