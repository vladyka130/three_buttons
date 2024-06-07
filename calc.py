from tkinter import *
from tkinter import ttk
import random

w = Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

w["bg"] = '#2F4F4F'
w.geometry("700x400")
w.resizable(height=False, width=False)

canva = Canvas(width=687, height=389, bg='#2F4F4F',)
canva.place(x=5, y=3)
canva.create_line(373, 7, 373, 386, width=1)

def tabl():
    for i in l:
        x, y = random.randint(2, 9), random.randint(2, 9)
        insert_text = f'{x} * {y}'
        i.configure(text=insert_text)
        res = x * y                                          # РЕЗУЛЬТАТ
        ress.append(res)                                     # додаємо кожен результат в список
    otvet.configure(text=ress)                               # втвід результатів у Label


start = Button(text='НАДРУКУВАТИ ТАБЛИЧКУ МНОЖЕННЯ', bg="#0B615E", width=49, command=tabl)
start.place(x=15, y=10)
proverka = Button(text='ПЕРЕВІРТИ РЕЗУЛЬТАТИ', bg="#0B615E", width=39)
proverka.place(x=390, y=10)

text_priklad = Label(text='=', bg="#2F4F4F", font=14)

l = []
ress = []
otvet = Label(bg='#2F4F4F', font=('Comic Sans MS', 9))
otvet.place(x=15, y=300)

l1 = Label(width=15, text='')
l.append(l1)
l1.place(x=15, y=50)
text_priklad.place(x=130, y=45)
enter1 = Entry(width=4)
enter1.place(x=150, y=50)

l2 = Label(width=15, text='')
l.append(l2)
l2.place(x=15, y=75)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=70)
enter2 = Entry(width=4)
enter2.place(x=150, y=75)

l3 = Label(width=15)
l.append(l3)
l3.place(x=15, y=100)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=95)
enter3 = Entry(width=4)
enter3.place(x=150, y=100)

l4 = Label(width=15)
l.append(l4)
l4.place(x=15, y=125)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=120)
enter4 = Entry(width=4)
enter4.place(x=150, y=125)

l5 = Label(width=15)
l.append(l5)
l5.place(x=15, y=150)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=145)
enter5 = Entry(width=4)
enter5.place(x=150, y=150)

l6 = Label(width=15)
l.append(l6)
l6.place(x=15, y=175)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=170)
enter6 = Entry(width=4)
enter6.place(x=150, y=175)

l7 = Label(width=15)
l.append(l7)
l7.place(x=15, y=200)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=195)
enter7 = Entry(width=4, )
enter7.place(x=150, y=200)

l8 = Label(width=15)
l.append(l8)
l8.place(x=15, y=225)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=220)
enter8 = Entry(width=4)
enter8.place(x=150, y=225)

l9 = Label(width=15)
l.append(l9)
l9.place(x=15, y=250)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=245)
enter9 = Entry(width=4, )
enter9.place(x=150, y=250)

l10 = Label(width=15)
l.append(l10)
l10.place(x=15, y=275)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=270)
enter10 = Entry(width=4, )
enter10.place(x=150, y=275)

l11 = Label(width=15)
l.append(l11)
l11.place(x=210, y=50)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=45)
enter11 = Entry(width=4, )
enter11.place(x=335, y=50)

l12 = Label(width=15)
l.append(l12)
l12.place(x=210, y=75)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=70)
enter12 = Entry(width=4, )
enter12.place(x=335, y=75)

l13 = Label(width=15)
l.append(l13)
l13.place(x=210, y=100)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=95)
enter13 = Entry(width=4, )
enter13.place(x=335, y=100)

l14 = Label(width=15)
l.append(l14)
l14.place(x=210, y=125)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=120)
enter14 = Entry(width=4, )
enter14.place(x=335, y=125)

l15 = Label(width=15)
l.append(l15)
l15.place(x=210, y=150)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=145)
enter15 = Entry(width=4, )
enter15.place(x=335, y=150)

l16 = Label(width=15)
l.append(l16)
l16.place(x=210, y=175)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=170)
enter16 = Entry(width=4, )
enter16.place(x=335, y=175)

l17 = Label(width=15)
l.append(l17)
l17.place(x=210, y=200)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=195)
enter17 = Entry(width=4, )
enter17.place(x=335, y=200)

l18 = Label(width=15)
l.append(l18)
l18.place(x=210, y=225)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=220)
enter18 = Entry(width=4)
enter18.place(x=335, y=225)

l19 = Label(width=15)
l.append(l19)
l19.place(x=210, y=250)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=245)
enter19 = Entry(width=4, )
enter19.place(x=335, y=250)

l20 = Label(width=15, text="")
l.append(l20)
l20.place(x=210, y=275)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=270)
enter20 = Entry(width=4, )
enter20.place(x=335, y=275)

w.mainloop()
