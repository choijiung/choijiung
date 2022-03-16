gun = 10

def checkpont(soldiers):
    global gun #전역변수
    gun = gun - soldiers
    print("남은 총은 {0}자루 이지 말입니다".format(gun))

def checkpont_retun(gun, soldiers):
    gun = gun - soldiers
    print("추가로 경계 근무를 가서 남은 총은 {0}자루 이지 말입니다".format(gun))
    return gun

print("전체 총: {0}".format(gun))
input("추웅성!! 몇명이 경계근무를 나가지요?(숫자만)")
awnser = int(input())
if awnser > gun:
    print("총이 없어서 경계근무를 나가지 못합니다!!")
checkpont(awnser)
checkpont_retun(gun, 2)