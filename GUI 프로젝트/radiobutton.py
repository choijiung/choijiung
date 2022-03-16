from tkinter import *

root = Tk()
root.title("image")
root.geometry("640x480")

Label(root, text= "메뉴를 선택하세요").pack()

buger_bar = StringVar()
btn_buger1 = Radiobutton(root, text="햄버거", value="햄버거", variable=buger_bar)
btn_buger1.select()
btn_buger2 = Radiobutton(root, text="치즈버거", value="치즈버거", variable=buger_bar)
btn_buger3 = Radiobutton(root, text="불고기버거", value="불고기버거", variable=buger_bar)

btn_buger1.pack()
btn_buger2.pack()
btn_buger3.pack()

Label(root, text= "음료를 선택하세요").pack()
drink_bar = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라",variable=drink_bar)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다",variable=drink_bar)
btn_drink3 = Radiobutton(root, text="환타", value="환타",variable=drink_bar)
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(buger_bar.get())
    print(drink_bar.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()