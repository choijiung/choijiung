from asyncore import write
from inspect import formatannotationrelativeto
from re import T
import tkinter
import pickle

file_name = "봉사시간관리/Workedtime.pickle"

while True:
    print("1. 봉사시간 추가")
    print("2. 현재 봉사시간 조회")
    print("3. 프로그램 종료")
    awnser = input("어느 것을 할 것인가요?")    
    if awnser == "봉사시간 추가":
        with open(file_name, "rb") as r:
            retime = pickle.load(r)
            time = input("몇 시간동안 봉사를 했습니까?")
            ltime = int(retime) + int(time)
        with open(file_name, "wb") as w:
            pickle.dump(str(ltime), w)
            continue
    elif awnser == "현재 봉사시간 조회":
        with open(file_name, "rb") as r:
            readtime = pickle.load(r)
            print("현재 봉사 시간은 {0}시간 입니다".format(readtime))
            continue
    elif awnser == "프로그램 종료":
        break
    else:
        print("다시 입력해 주세요")
        continue
