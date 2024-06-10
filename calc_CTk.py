from tkinter import *
import random
import smtplib
import customtkinter



w = customtkinter.CTk()
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("blue")

w.geometry("700x400")
w.resizable(height=False, width=False)
#
# canva = Canvas(width=687, height=389, bg='#2F4F4F',)
# canva.place(x=5, y=3)
# canva.create_line(373, 7, 373, 386, width=1)
# canva.create_line(388, 105, 678, 105, width=1)
# canva.create_line(183, 47, 183, 294, width=1)
#
#
def tabl():
    ress.clear()
    for i in range(20):
        enters[i].delete(0, END)
        enters[i].configure(bg_color='white')
    for i in l:
        x, y = random.randint(2, 9), random.randint(2, 9)
        insert_text = f'{x} * {y}'
        i.configure(text=insert_text, compound='center')
        res = x * y                                          # РЕЗУЛЬТАТ
        ress.append(res)                                     # додаємо кожен результат в список
    otvet.configure(text=ress)                               # втвід результатів у Label
    proverka.configure(state=NORMAL)
    text_virni.configure(text='')
    text_nevirni.configure(text='')
#
def proverka():
    answer = []
    count = 0
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
            enters[i].configure(bg_color='#9FF781')
        else:
            priklad_not_answer.append(l[i]['text'])
            enters[i].configure(bg_color='#F78181')
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
    text = f"{text_ocinka_count['text']} \nВірних відповідей: {count} \n\nневирішені приклади:\n{priklad_not_answer}"
#     send_mail(text)
#
# def send_mail(text):
#     server,  user, password = 'smtp.mail.ru', 'matroskin1999@mail.ru', 'y0k1nvQAwu9cNyiMCayK'
#     recipients, sender = 'music319@gmail.com', 'matroskin1999@mail.ru'
#     msg = text
#     mail = smtplib.SMTP_SSL(server)
#     mail.login(user, password)
#     mail.sendmail(sender, recipients, msg.encode('utf'))
#     mail.quit()
#
start = customtkinter.CTkButton(master=w, text='НАДРУКУВАТИ ТАБЛИЧКУ МНОЖЕННЯ', width=49, command=tabl)
start.place(x=15, y=10)
proverka = customtkinter.CTkButton(master=w, text='ПЕРЕВІРТИ РЕЗУЛЬТАТИ',  width=41,) #command=proverka
proverka.place(x=390, y=10)
proverka.configure(state=DISABLED)

text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14))
text_resultat_virni = customtkinter.CTkLabel(master=w,text=f'ВІРНІ ВІДПОВІДІ: ', font=('Comic Sans MS', 14))
text_resultat_virni.place(x=390, y=46)
text_resultat_nevirni = customtkinter.CTkLabel(master=w,text=f'НЕВІРНІ ВІДПОВІДІ: ',font=('Comic Sans MS', 14))
text_resultat_nevirni.place(x=390, y=70)
text_virni = customtkinter.CTkLabel(master=w, text='', font=('Comic Sans MS', 14))
text_virni.place(x=660, y=46)
text_nevirni = customtkinter.CTkLabel(master=w, text='', font=('Comic Sans MS', 14))
text_nevirni.place(x=660, y=69)
text_ocinka = customtkinter.CTkLabel(master=w,text="ОЦІНКА: ", font=('Comic Sans MS', 14))
text_ocinka.place(x=390, y=115)
text_ocinka_count = customtkinter.CTkLabel(master=w, text='', font=('Comic Sans MS', 14))
text_ocinka_count.place(x=510, y=115)

l = []
ress = []
answer = []
priklad_not_answer = []
otvet = customtkinter.CTkLabel(master=w, text='',  font=('Comic Sans MS', 9))
otvet.place(x=15, y=300)

l1 = customtkinter.CTkLabel(master=w, width=15, text='', compound=CENTER)
l.append(l1)
l1.place(x=15, y=50)
text_priklad.place(x=130, y=45)
enter1 = customtkinter.CTkEntry(master=w, width=6)
enter1.place(x=150, y=50)

l2 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l2)
l2.place(x=15, y=75)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=130, y=70)
enter2 = customtkinter.CTkEntry(master=w, width=6)
enter2.place(x=150, y=75)
#
l3 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l3)
l3.place(x=15, y=100)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=130, y=95)
enter3 = customtkinter.CTkEntry(master=w, width=6)
enter3.place(x=150, y=100)
#
l4 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l4)
l4.place(x=15, y=125)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=130, y=120)
enter4 = customtkinter.CTkEntry(master=w, width=6)
enter4.place(x=150, y=125)
#
l5 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l5)
l5.place(x=15, y=150)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=130, y=145)
enter5 = customtkinter.CTkEntry(master=w, width=6)
enter5.place(x=150, y=150)
#
l6 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l6)
l6.place(x=15, y=175)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=130, y=170)
enter6 = customtkinter.CTkEntry(master=w, width=6)
enter6.place(x=150, y=175)
#
l7 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l7)
l7.place(x=15, y=200)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=130, y=195)
enter7 = customtkinter.CTkEntry(master=w, width=6)
enter7.place(x=150, y=200)
#
l8 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l8)
l8.place(x=15, y=225)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=130, y=220)
enter8 = customtkinter.CTkEntry(master=w, width=6)
enter8.place(x=150, y=225)
#
l9 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l9)
l9.place(x=15, y=250)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=130, y=245)
enter9 = customtkinter.CTkEntry(master=w, width=6)
enter9.place(x=150, y=250)
#
l10 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l10)
l10.place(x=15, y=275)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=130, y=270)
enter10 = customtkinter.CTkEntry(master=w, width=6)
enter10.place(x=150, y=275)
#
l11 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l11)
l11.place(x=200, y=50)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=315, y=45)
enter11 = customtkinter.CTkEntry(master=w, width=6)
enter11.place(x=335, y=50)
#
l12 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l12)
l12.place(x=200, y=75)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=315, y=70)
enter12 = customtkinter.CTkEntry(master=w, width=6)
enter12.place(x=335, y=75)
#
l13 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l13)
l13.place(x=200, y=100)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=315, y=95)
enter13 = customtkinter.CTkEntry(master=w, width=6)
enter13.place(x=335, y=100)
#
l14 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l14)
l14.place(x=200, y=125)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=315, y=120)
enter14 = customtkinter.CTkEntry(master=w, width=6)
enter14.place(x=335, y=125)
#
l15 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l15)
l15.place(x=200, y=150)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=315, y=145)
enter15 = customtkinter.CTkEntry(master=w, width=6)
enter15.place(x=335, y=150)
#
l16 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l16)
l16.place(x=200, y=175)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=315, y=170)
enter16 = customtkinter.CTkEntry(master=w, width=6)
enter16.place(x=335, y=175)
#
l17 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l17)
l17.place(x=200, y=200)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=315, y=195)
enter17 = customtkinter.CTkEntry(master=w, width=6)
enter17.place(x=335, y=200)
#
l18 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l18)
l18.place(x=200, y=225)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=315, y=220)
enter18 = customtkinter.CTkEntry(master=w, width=6)
enter18.place(x=335, y=225)
#
l19 = customtkinter.CTkLabel(master=w, width=15, text='')
l.append(l19)
l19.place(x=200, y=250)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=315, y=245)
enter19 = customtkinter.CTkEntry(master=w, width=6)
enter19.place(x=335, y=250)
#
l20 = customtkinter.CTkLabel(master=w, width=15, text="")
l.append(l20)
l20.place(x=200, y=275)
text_priklad = customtkinter.CTkLabel(master=w, text='=', font=('Comic Sans MS', 14)).place(x=315, y=270)
enter20 = customtkinter.CTkEntry(master=w, width=6)
enter20.place(x=335, y=275)
#
enters = [enter1, enter2, enter3, enter4, enter5,
          enter6, enter7, enter8, enter9, enter10,
          enter11, enter12, enter13, enter14, enter15,
          enter16, enter17, enter18, enter19, enter20]
#
w.mainloop()