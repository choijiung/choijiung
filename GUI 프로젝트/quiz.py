import os
from tkinter import *
root = Tk()
root.title("제목없음 - windows 메모장")
root.geometry("640x480")
filename = "assets/mynote.txt"
def open_my_note():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_my_note():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))


menu = Menu(root)
menu_File = Menu(menu, tearoff=0)
menu_File.add_command(label="열기", command=open_my_note)
menu_File.add_command(label="저장하기", command=save_my_note)
menu_File.add_separator()
menu_File.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_File)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")
root.config(menu=menu)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.mainloop()