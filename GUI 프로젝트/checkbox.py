from tkinter import *

root = Tk()
root.title("image")
root.geometry("640x480")

chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() = 체크
# #chkbox.deselect() = 해제
chkbox.pack()

chkvar2 = IntVar()
chkbox = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox.pack()

def btncmd():
    print(chkvar.get()) #0:체크해제, 1: 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()