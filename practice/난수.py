from random import *
print(random())# 0.0~1.0미만
print(random()*10)# 0.0~10.0마만
print(int(random() *10))# 0.0~10.0 미만의 정수
count = 10
while count >= 1:
    print(int(random() *10)+1)# 1~10 이하의 정수
    count -= 1
