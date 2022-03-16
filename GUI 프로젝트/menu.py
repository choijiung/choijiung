from tkinter import *

root = Tk()
root.title("image")
root.geometry("640x480")

def create_new_file():
    print("새 파일을 만듭니다")

menu = Menu(root)

#File 메뉴
menu_File = Menu(menu, tearoff=0)
menu_File.add_command(label="New File", command=create_new_file)
menu_File.add_command(label="New Window")
menu_File.add_separator()
menu_File.add_command(label="Open File...")
menu_File.add_separator()
menu_File.add_command(label="Save All", state="disable")
menu_File.add_separator()
menu_File.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="file", menu = menu_File)

#Edit 메뉴
menu.add_cascade(label="Edit")


#Language 메뉴 추가 (radio 버튼을 통해 택 1)
menu_Lang = Menu(menu, tearoff=0)
menu_Lang.add_radiobutton(label="한국어")
menu_Lang.add_radiobutton(label="English")
menu_Lang.add_radiobutton(label="MewoMewoMewo")
menu_Lang.add_radiobutton(label="RrrRrr")
menu.add_cascade(label="Language", menu=menu_Lang)

#View 메뉴
menu_View = Menu(menu, tearoff=0)
menu_View.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_View)

root.config(menu=menu)

root.mainloop()