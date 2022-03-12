from asyncore import write
import tkinter
import pickle
file_name = "봉사시간관리/Workedtime.txt"
with open(file_name, "r") as w:
    retime = w.readline()
    print(retime)
    time = input("몇 시간동안 봉사를 했습니까?")
    retime = int(retime) + int(time)
with open(file_name, "w") as w:
    w.write(str(retime))