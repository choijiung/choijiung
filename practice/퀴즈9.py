class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    chicken = 10
    waiting = 1
    while (True):
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하셨습니까?"))
        if order <= 0:
            raise ValueError
        else:
            if order > chicken:
                raise SoldOutError("남은 치킨: {0}마리".format(chicken))
            else:
                print("[대기번호 {0}] {1}마리 주문이 완료되었습니다".format(waiting, order))
                waiting += 1
                chicken -= order

except SoldOutError as err:
    print(err)
    print("재료가 부족합니다")
except ValueError as err:
    print("주문 값이 0보다 작거나 같습니다")
finally:
    print("안녕히가십시오")