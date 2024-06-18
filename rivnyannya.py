from tkinter import *
import random

w = Tk()
w.title('Приклади для Арсена v.1.0')
w["bg"] = '#2F4F4F'
w.geometry("382x600")
w.resizable(height=False, width=False)
Frame(width=372, height=592, relief="ridge", bg='#2F4F4F', bd=1).place(x=5, y=4)


def priklad():
    diya = []
    x, y = random.randint(2, 100), random.randint(2, 1000)
    diya_1 = [f'(x + {y}) = {x + y}', x]
    diya.append(diya_1)
    x, y = random.randint(2, 1000), random.randint(2, 1000)
    diya_2 = [f'({y} + x) = {y + x}', x]
    diya.append(diya_2)
    while True:
        x, y = random.randint(2, 1000), random.randint(2, 1000)
        if x > y:
            diya_3 = [f'(x - {y}) = {x - y}', x]
            diya.append(diya_3)
            break
    x, y = random.randint(2, 10), random.randint(2, 10)
    diya_4 = [f'({y} * x) = {y * x}', x]
    diya.append(diya_4)
    while True:
        x, y = random.randint(2, 100), random.randint(2, 10)
        if x > y and x % y == 0:
            diya_5 = [f'(x : {y}) = {int(x / y)}', int((x/y)*y)]
            diya.append(diya_5)
            break
    return random.choice(diya)


def tabl():
    result.clear()
    proverka.configure(state=NORMAL)
    for i in range(15):
        p = priklad()
        answer_Entry[i].configure(background='#A9F5D0')
        result.append(p[1])
        priclady_Label[i].configure(text=p[0])
        answer_Entry[i].delete(0, END)

result = []

def proverka():
    answer = []
    for i in range(15):
        if answer_Entry[i].get() != '' and answer_Entry[i].get().isdigit():
            answer.append(int(answer_Entry[i].get()))
        else:
            answer.append("")
            answer_Entry[i].delete(0, END)
            answer_Entry[i].insert(0, '')
            answer_Entry[i].configure(bg='#F78181')  # червоний

    for i in range(15):
        if result[i] == answer[i]:
            answer_Entry[i].configure(background='#9FF781')
        else:
            answer_Entry[i].configure(background='#F78181')


start = Button(text='ПОКАЗАТИ ПРИКЛАДИ', bg="#0B615E", width=49, command=tabl)
start.place(x=15, y=10)
proverka = Button(text='ПЕРЕВІРТИ РЕЗУЛЬТАТИ', bg="#0B615E", width=49, state=DISABLED, command=proverka)
proverka.place(x=15, y=40)

priclady_Label, symbol_ravno, answer_Entry, priklady, results = [], [], [], [], []
x_priclady, y_priclady = 16, 80,
x_ravno, y_ravno = 240, 77

for i in range(15):
    priclady_Label.append(Label(width=30, text='', background='#A9F5D0', relief='ridge'))
    priclady_Label[i].place(x=x_priclady, y=y_priclady)
    symbol_ravno.append(Label(background='#2F4F4F', text='=', font=1))
    symbol_ravno[i].place(x=x_ravno, y=y_ravno)
    answer_Entry.append(Entry(width=16, background='#A9F5D0', relief='solid'))
    answer_Entry[i].place(x=x_priclady + 250, y=y_priclady + 1)
    y_ravno += 25
    y_priclady += 25

w.mainloop()