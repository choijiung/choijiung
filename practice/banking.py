def open_account():
    print("새로운 계좌가 생성되었습니다.")
    print("환영합니다")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은{0}원 입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다".format(balance))

def withdraw_night(blance, money):
    commission = 100
    return commission, blance - money - commission

def Questions():
    input("어떤 서비스를 이용하시겠습니까? \n1.입금\n2.출금\n3.잔액확인\n4.프로그램 종료")



while True:
    input("성함이 어떻게 되십니까?")
    name = input()
    open_account()
    dicbalance = {"none": 1}
    dicbalance[name] = 0
    balanece = dicbalance.get(name)
    password = "choi1118!@"
    Questions()
    awnser = str(input())
    if awnser == '입금':
        input("얼마를 입금하시겠슴니까?(숫자만 입력하세요)")
        awnser = int(input())
        deposit(balanece, awnser)
        dicbalance[name] = awnser + balanece
        balanece = dicbalance.get(name)
        continue

    elif awnser == '출금':
        input("얼마를 출금하시겠습니까?(숫자만 입력하세요)")
        awnser = int(input())
        withdraw(balanece, awnser)
        balanece -= awnser
        dicbalance[name] = balanece - awnser
        continue

    if awnser == '잔액확인':
        print('남은 잔액은 {0}원 입니다'.format(dicbalance.get(name)))
        continue

    elif awnser == "프로그램 종료":
        print("프로그램을 종료합니다.")
        break

    elif awnser == password:
        print("관리자 권한에 접속하였습니다")
        print("모든 고객들의 정보를 출력합니다")
        print(dicbalance)
        continue

    else:
        print("잘못 입력하셨습니다")
        continue
