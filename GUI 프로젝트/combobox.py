import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("image")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
combobox.pack()
combobox.set("카드결제일")

def btncmd():
    Label(root, text=combobox.get() + "에 \'123,333,546,134,\n596,371,497,369\'"
    "147,649,276,492,545,\n054,298,365,018,165\'\n원이 결제됩니다(통장잔고 : 1000원)", fg = "gray").pack()

btn = Button(root, text="결제", command=btncmd)
btn.pack()

root.mainloop()