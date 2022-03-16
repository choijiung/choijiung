from tkinter import *

root = Tk()
root.title("image")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(3, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    #listbox.delete(0)#맨 앞 항목을 삭제
    #print("리스트에는" + str(listbox.size()) + "개의 항목이 있습니다")
    #print("1번째부터 3번째까지의 항목:", listbox.get(0, 2))
    print("선택된 항목:", listbox.curselection())




photo2 = PhotoImage(file="assets/Questions.png")
btn = Button(root, image=photo2, command=btncmd)
btn.pack()


root.mainloop()