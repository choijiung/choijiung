import tkinter.messagebox as mg
from tkinter import *

root = Tk()
root.title("image")
root.geometry("640x480")

fram = Frame(root)
fram.pack()

scrollbar = Scrollbar(fram)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(fram, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 31):
    listbox.insert(END, str(i) + '일')
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()