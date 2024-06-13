from tkinter import *
import random
import smtplib
import customtkinter
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

w = Tk()
w.title('Табличка множення для Арсена v.1.0')
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("blue")

w["bg"] = '#2F4F4F'
w.geometry("700x450")
w.resizable(height=False, width=False)

canva = Canvas(width=687, height=439, bg='#2F4F4F')
canva.place(x=5, y=3)
canva.create_line(373, 7, 373, 435, width=1)
canva.create_line(388, 105, 678, 105, width=1)
canva.create_line(183, 47, 183, 299, width=1)
canva.create_rectangle(5, 40, 683, 304)
canva.create_rectangle(5, 304, 683, 436)

def tabl():
    ress.clear()
    for i in range(20):
        enters[i].delete(0, END)
        enters[i].configure(background='#A9F5D0')
    for i in range(5):
        o[i].delete(0, END)
        o[i].configure(background='#A9F5D0')
    for i in l:
        x, y = random.randint(2, 9), random.randint(2, 9)
        insert_text = f'{x} * {y}'
        i.configure(text=insert_text)
        res = x * y                                          # РЕЗУЛЬТАТ
        ress.append(res)                                     # додаємо кожен результат в список
    #otvet.configure(text=ress)                               # втвід результатів у Label
    proverka.configure(state=NORMAL)
    text_virni.configure(text='')
    text_nevirni.configure(text='')
    for i in range(5):
        o[i].configure(background='#A9F5D0')
        while True:
            a = random.randint(50, 100)
            b = random.randint(50, 100)
            c = random.randint(3, 100)
            d = random.randint(3, 100)
            if b > a:
                break
        insert_text_2 = f'{c} * {d} + ({b}-{a})'
        resss = c * d + (b - a)
        ress_2.append(resss)
        p[i].configure(text=insert_text_2)


def proverka():
    answer = []
    count = 0
    print(ress)
    for i in range(20):
        if enters[i].get() != '' and enters[i].get().isdigit():
            answer.append(int(enters[i].get()))
        else:
            enters[i].delete(0, END)
            enters[i].insert(0, '0')
            answer.append("0")
    for i in range(20):
        if ress[i] == int(enters[i].get()):
            count += 1
            enters[i].configure(background='#9FF781')
        else:
            priklad_not_answer.append(l[i]['text'])
            enters[i].configure(background='#F78181')
    if count == 20:
        text_ocinka_count.configure(text='Відмінно!')
    elif count < 20 and count > 17:
        text_ocinka_count.configure(text='Добре!')
    elif count < 18 and count > 15:
        text_ocinka_count.configure(text='Задовільно!')
    elif count < 14:
        text_ocinka_count.configure(text='НЕзадовільно!')
    proverka.configure(state=DISABLED)
    text_virni.configure(text=count, fg='green')
    text_nevirni.configure(text=20 - count, fg='red')

    count_2 = 0
    for i in range(5):
        if o[i].get() != '' and o[i].get().isdigit():
            answer_2.append(int(o[i].get()))
        else:
            o[i].delete(0, END)
            o[i].insert(0, '0')
            answer_2.append("0")
    for i in range(5):
        if ress_2[i] == int(o[i].get()):
            count_2 += 1                                  # вірна відповідь
            o[i].configure(background='#9FF781')          # робимо зелений
        else:
            priklad_not_answer_2.append(p[i]['text'])     # приклад  який не вирішено
            o[i].configure(background='#F78181')          # робимо червоне
    if count_2 == 5:
        text_ocinka_count_2.configure(text='Відмінно!')
    elif count_2 == 4:
        text_ocinka_count_2.configure(text='Добре!')
    elif count_2 == 3:
        text_ocinka_count_2.configure(text='Задовільно!')
    elif count_2 <= 2:
        text_ocinka_count_2.configure(text='НЕзадовільно!')
    text = f"{text_ocinka_count['text']} \nВірних відповідей: {count} \n\nневирішені приклади:\n{priklad_not_answer}\n\nПриклади: {text_ocinka_count_2['text']}"
    try:
        send_mail(text)
    except Exception:
        print("Internet connection error!")

def send_mail(text):
    server,  user, password = 'smtp.mail.ru', 'matroskin1999@mail.ru', 'y0k1nvQAwu9cNyiMCayK'
    recipients, sender = 'music319@gmail.com', 'matroskin1999@mail.ru'
    msg = text
    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.encode('utf'))
    mail.quit()

start = Button(text='НАДРУКУВАТИ ТАБЛИЧКУ МНОЖЕННЯ', bg="#0B615E", width=49, command=tabl)
start.place(x=15, y=10)
proverka = Button(text='ПЕРЕВІРТИ РЕЗУЛЬТАТИ', bg="#0B615E", width=41, command=proverka)
proverka.place(x=390, y=10)
proverka.configure(state=DISABLED)

text_priklad = Label(text='=', bg="#2F4F4F", font=14)
text_resultat_virni = Label(text=f'ВІРНІ ВІДПОВІДІ: ', bg="#2F4F4F", font=('Comic Sans MS', 14))
text_resultat_virni.place(x=389, y=46)
text_resultat_nevirni = Label(text=f'НЕВІРНІ ВІДПОВІДІ: ', bg="#2F4F4F", font=('Comic Sans MS', 14))
text_resultat_nevirni.place(x=389, y=70)
text_virni = Label( bg="#2F4F4F", font=('Comic Sans MS', 14))
text_virni.place(x=660, y=46)
text_nevirni = Label(bg="#2F4F4F", font=('Comic Sans MS', 14))
text_nevirni.place(x=660, y=69)
text_ocinka = Label(text="ОЦІНКА: ", font=('Comic Sans MS', 14), bg="#2F4F4F")
text_ocinka.place(x=389, y=115)
text_ocinka_count = Label(font=('Comic Sans MS', 14), bg="#2F4F4F")
text_ocinka_count.place(x=389, y=140)

l = []
ress = []
answer = []
priklad_not_answer = []
otvet = Label(bg='#2F4F4F', font=('Comic Sans MS', 9))
otvet.place(x=15, y=305)

p = []
ress_2 = []
answer_2 = []
priklad_not_answer_2 = []

l1 = Label(width=15, text='', background='#A9F5D0', relief='ridge')
l.append(l1)
l1.place(x=15, y=50)
text_priklad.place(x=130, y=45)
enter1 = Entry(width=4, background='#A9F5D0', relief='solid')
enter1.place(x=150, y=50)

l2 = Label(width=15, text='', background='#A9F5D0', relief='ridge')
l.append(l2)
l2.place(x=15, y=75)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=70)
enter2 = Entry(width=4, background='#A9F5D0', relief='solid')
enter2.place(x=150, y=75)

l3 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l3)
l3.place(x=15, y=100)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=95)
enter3 = Entry(width=4, background='#A9F5D0', relief='solid')
enter3.place(x=150, y=100)

l4 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l4)
l4.place(x=15, y=125)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=120)
enter4 = Entry(width=4, background='#A9F5D0', relief='solid')
enter4.place(x=150, y=125)

l5 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l5)
l5.place(x=15, y=150)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=145)
enter5 = Entry(width=4, background='#A9F5D0', relief='solid')
enter5.place(x=150, y=150)

l6 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l6)
l6.place(x=15, y=175)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=170)
enter6 = Entry(width=4, background='#A9F5D0', relief='solid')
enter6.place(x=150, y=175)

l7 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l7)
l7.place(x=15, y=200)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=195)
enter7 = Entry(width=4, background='#A9F5D0', relief='solid')
enter7.place(x=150, y=200)

l8 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l8)
l8.place(x=15, y=225)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=220)
enter8 = Entry(width=4, background='#A9F5D0', relief='solid')
enter8.place(x=150, y=225)

l9 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l9)
l9.place(x=15, y=250)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=245)
enter9 = Entry(width=4, background='#A9F5D0', relief='solid')
enter9.place(x=150, y=250)

l10 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l10)
l10.place(x=15, y=275)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=130, y=270)
enter10 = Entry(width=4, background='#A9F5D0', relief='solid')
enter10.place(x=150, y=275)

l11 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l11)
l11.place(x=200, y=50)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=45)
enter11 = Entry(width=4, background='#A9F5D0', relief='solid')
enter11.place(x=335, y=50)

l12 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l12)
l12.place(x=200, y=75)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=70)
enter12 = Entry(width=4, background='#A9F5D0', relief='solid')
enter12.place(x=335, y=75)

l13 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l13)
l13.place(x=200, y=100)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=95)
enter13 = Entry(width=4, background='#A9F5D0', relief='solid')
enter13.place(x=335, y=100)

l14 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l14)
l14.place(x=200, y=125)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=120)
enter14 = Entry(width=4, background='#A9F5D0', relief='solid')
enter14.place(x=335, y=125)

l15 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l15)
l15.place(x=200, y=150)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=145)
enter15 = Entry(width=4, background='#A9F5D0', relief='solid')
enter15.place(x=335, y=150)

l16 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l16)
l16.place(x=200, y=175)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=170)
enter16 = Entry(width=4, background='#A9F5D0', relief='solid')
enter16.place(x=335, y=175)

l17 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l17)
l17.place(x=200, y=200)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=195)
enter17 = Entry(width=4, background='#A9F5D0', relief='solid')
enter17.place(x=335, y=200)

l18 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l18)
l18.place(x=200, y=225)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=220)
enter18 = Entry(width=4, background='#A9F5D0', relief='solid')
enter18.place(x=335, y=225)

l19 = Label(width=15, background='#A9F5D0', relief='ridge')
l.append(l19)
l19.place(x=200, y=250)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=245)
enter19 = Entry(width=4, background='#A9F5D0', relief='solid')
enter19.place(x=335, y=250)

l20 = Label(width=15, text="", background='#A9F5D0', relief='ridge')
l.append(l20)
l20.place(x=200, y=275)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=315, y=270)
enter20 = Entry(width=4, background='#A9F5D0', relief='solid')
enter20.place(x=335, y=275)
#
p1: Label = Label(width=24, text='', background='#A9F5D0', relief='ridge')
p1.place(x=15, y=315)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=195, y=312)
o1 = Entry(width=13, text='', background='#A9F5D0', relief='solid')
o1.place(x=215, y=315)

p2: Label = Label(width=24, text='', background='#A9F5D0', relief='ridge')
p2.place(x=15, y=340)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=195, y=337)
o2 = Entry(width=13, text='', background='#A9F5D0', relief='solid')
o2.place(x=215, y=340)

p3: Label = Label(width=24, text='', background='#A9F5D0', relief='ridge')
p3.place(x=15, y=365)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=195, y=359)
o3 = Entry(width=13, text='', background='#A9F5D0', relief='solid')
o3.place(x=215, y=365)

p4: Label = Label(width=24, text='', background='#A9F5D0', relief='ridge')
p4.place(x=15, y=390)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=195, y=384)
o4 = Entry(width=13, text='', background='#A9F5D0', relief='solid')
o4.place(x=215, y=390)

p5: Label = Label(width=24, text='', background='#A9F5D0', relief='ridge')
p5.place(x=15, y=415)
text_priklad = Label(text='=', bg="#2F4F4F", font=14).place(x=195, y=409)
o5 = Entry(width=13, text='', background='#A9F5D0', relief='solid')
o5.place(x=215, y=415)

enters = [enter1, enter2, enter3, enter4, enter5,
          enter6, enter7, enter8, enter9, enter10,
          enter11, enter12, enter13, enter14, enter15,
          enter16, enter17, enter18, enter19, enter20]

p = [p1, p2, p3, p4, p5]
o = [o1, o2, o3, o4, o5]
text_ocinka_2 = Label(text="ОЦІНКА ЗА ПРИКЛАДИ: ", font=('Comic Sans MS', 14), bg='#2F4F4F')
text_ocinka_2.place(x=389, y=310)
text_ocinka_count_2 = Label(font=('Comic Sans MS', 14), bg='#2F4F4F')
text_ocinka_count_2.place(x=389, y=335)

w.mainloop()
