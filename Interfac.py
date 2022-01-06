from tkinter import *
import SecondWindow
import WhatsAppScript
window = Tk()
e1_str = StringVar()
window.geometry("500x500")
window.title("HOME")
def forward():
    window.destroy()
    print(e1_str.get())
    WhatsAppScript.automate(client = e1_str.get(),code = 1)
    SecondWindow.SecondWin(client = e1_str.get())
l1_str = StringVar()
t1 = Label(window,textvariable = l1_str)
l1_str.set("Label")
t1.grid(row = 1,column = 1)

e1 = Entry(window,textvariable = e1_str)
e1.grid(row = 1,column = 2)
b1 = Button(window,text = "Execute",command = forward)
b1.grid(row = 2,column = 1,columnspan = 20)

window.mainloop()
