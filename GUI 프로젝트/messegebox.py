import tkinter.messagebox as mg
from tkinter import *

root = Tk()
root.title("image")
root.geometry("640x480")

#기차표 예매 시스템
def info():
    mg.showinfo("알림", "정상적으로 예매 완료되었습니다")

def warning():
    mg.showwarning("경고", "해당 카드는 한도초과입니다")

def Error():
    mg.showerror("에러", "해당 카드는 도난카드입니다")

def okcancel():
    mg.askokcancel("확인 / 취소", "해당 좌석의 옆자리는 반려동물, 유야동반석입니다. 예매하시겠습니까?")

def retrycancel():
    response = mg.askretrycancel("재시도 / 취소", "튕겼다 하하하 다시 예매할 것인가 하하하 "
    "너의 돈은 이제 내 것이다 하하하 다시 결제하라 하하하 이것은 금융사기다 하하하")
    if response == 1:#재시도
        print("재시도")
    elif response == 0:
        print("취소")#취소

def yesno():
    mg.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 다시 예매할것인가 하하하")

def yesnocancel():
    response = mg.askyesnocancel(title=None, message="예매 기록이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    print("응답:", response) #True, False, None -> 예: 1, 아니오: 0, 그 외
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warning, text="결제").pack()
Button(root, command=Error, text="에러").pack()

Button(root, command=okcancel, text="확인취소").pack()
Button(root, command=retrycancel, text="재시도취소").pack()
Button(root, command=yesno, text="예아니오").pack()
Button(root, command=yesnocancel, text="예아니오취소").pack()

root.mainloop()