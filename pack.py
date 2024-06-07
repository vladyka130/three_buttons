from tkinter import *

w = Tk()
w["bg"] = '#2F4F4F'
w.geometry("500x300")
w.resizable(height=False, width=False)

# l1 = Label(text="one", bg="red", font=14, width=15).pack(side=LEFT)
# l2 = Label(text='two', bg="blue", font=14, width=15).pack()
# l3 = Label(text='three', bg="green", font=14, width=15).pack()

l1 = Label(text="one", bg="red", font=14, width=15)
l1.place(x=10, y=10)

w.mainloop()