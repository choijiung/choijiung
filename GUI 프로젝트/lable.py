from tkinter import *

root = Tk()
root.title("image")
root.title("image")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="assets/check.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="assets/cross.png")
    label2.config(image=photo2)

btn = Button(text="클릭", command=change)
btn.pack()

root.mainloop()