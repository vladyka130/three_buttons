from tkinter import *
import random
import smtplib
from funcs import *


w = Tk()
w.title('Табличка множення для Арсена v.1.0')
w["bg"] = '#2F4F4F'
w.geometry("700x500")
w.resizable(height=False, width=False)
Frame(width=690, height=492, relief="ridge", bg='#2F4F4F', bd=1).place(x=5, y=4)

def priklad():
    results.clear()
    x, y, c, b = random.randint(2, 100), random.randint(2, 100), random.randint(2, 10), random.randint(2, 10)
    diya = []
    diya_1 = [f'({x} + {y}) * {c}', (x + y) * c]
    diya.append(diya_1)
    while True:
        xxx, yyy, zz = random.randint(100, 999), random.randint(100, 999), random.randint(10, 99)
        if xxx > yyy:
            diya_2 = [f'{xxx} - {yyy}', xxx - yyy]
            break
    diya.append(diya_2)
    diya_3 = [f'{xxx} - {c} * {b}', xxx - c * b]
    diya.append(diya_3)
    while True:
        xxx, zz, c = random.randint(100, 999), random.randint(10, 99), random.randint(2, 10)
        if zz % c == 0 :
            diya_4 = [f'({zz} : {c}) + ({xxx} - {zz})', int((zz / c)) + (xxx - zz)]
            break
    diya.append(diya_4)
    return random.choice(diya)

def tabl():
    proverka.configure(state=NORMAL)
    results = []
    for i in range(15):
        p = priklad()
        priclady_Label[i].configure(text=p[0])
        results.append(p[1])
        answer_Entry[i].delete(0, END)
    print(results)

def proverka():
    count = 0
    answer = []
    for i in range(15):
        if answer_Entry[i].get() != '' and answer_Entry[i].get().isdigit():
            answer.append(int(answer_Entry[i].get()))
        else:
            answer_Entry[i].delete(0, END)
            answer_Entry[i].insert(0, '0')
            answer.append("0")


start = Button(text='ПОКАЗАТИ ПРИКЛАДИ', bg="#0B615E", width=49, command=tabl)
start.place(x=15, y=10)
proverka = Button(text='ПЕРЕВІРТИ РЕЗУЛЬТАТИ', bg="#0B615E", width=41, state=DISABLED, command=proverka)
proverka.place(x=390, y=10)

priclady_Label, symbol_ravno, answer_Entry, priklady = [], [], [], []
results = []

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
