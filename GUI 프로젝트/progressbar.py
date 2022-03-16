import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("image")
root.geometry("640x480")

#progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # indeterminate = 영원히 끝나지 않음
#progressbar.start(10)
#progressbar.pack()

#def btncmd():
#   progressbar.stop()

#btn = Button(root, text="다운중지", command=btncmd)
#btn.pack()

p_var = DoubleVar()
progressbar = ttk.Progressbar(root, maximum=100, length=150, variable=p_var)
progressbar.pack()

def btncmd():
   for i in range(1, 101):
       time.sleep(0.01)#0.01초 대기

       p_var.set(i)
       progressbar.update()#ui 업데이트
       print(p_var.get())

btn = Button(root, text="시작", command=btncmd)
btn.pack()


root.mainloop()