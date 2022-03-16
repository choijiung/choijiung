#클래스는 함수와 변수가 똑같은 구조를 여러번 쓰는 것을 피하기 위해서
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(7))
print(cal1.add(9))