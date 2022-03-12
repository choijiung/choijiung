from asyncore import write
from inspect import formatannotationrelativeto
import tkinter
import pickle
file_name = "봉사시간관리/Workedtime.pickle"
with open(file_name, "rb") as r:
    retime = pickle.load(r)
    time = input("몇 시간동안 봉사를 했습니까?")
    ltime = int(retime) + int(time)
with open(file_name, "wb") as w:
    pickle.dump(str(ltime), w)