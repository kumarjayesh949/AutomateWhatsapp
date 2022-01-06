from tkinter import *
import WhatsAppScript
def SecondWin(client):
    dropWin = Tk()
    dropWin.title("MAIN PAGE")
    def direct():
        dropWin.destroy()
        WhatsAppScript.automate(client=client,msg = msg.get(),code = 2)

    lb1 = StringVar()
    lb = Label(dropWin,textvariable = lb1)
    lb1.set("Msg")
    lb.grid(row = 0,column = 0)
    msg = StringVar()
    ent = Entry(dropWin,textvariable = msg)
    ent.grid(row = 0,column = 1)
    btn = Button(dropWin,text = "Send",command = direct)
    btn.grid(row = 1,column = 0,columnspan = 3)
    dropWin.mainloop()
