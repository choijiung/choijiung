# print("a+b")
# print("a, b")

#방법 1
# print("나는 %d살 입니다. "% 14)#d = 정수
# print("나는 %s를 좋아합니다" %"파이썬")
# # print("Apple는 %c로 시작해여."%'A')
#
# print("나는 %s살 입니다. "% 14)
# print('나는 %s 색과 %s 색을 좋아해요' %("파란", "빨강"))

# #방법 2
# print("나는 {}살 입니다.".format(14))
# print("나는 {}색과 {}색을 좋아해요".format("빨강", "파란"))
# print("나는 {0}색과 {1}색을 좋아해요".format("빨강", "파란"))
# print("나는 {1}색과 {0}색을 좋아해요".format("빨강", "파란"))

# #방법 3
# print("나는{age}살이며, {color}색을 좋아해요.".format(age = 20, color ="빨강"))
# print("나는{age}살이며, {color}색을 좋아해요.".format(color ="빨강", age = "14"))

#방법 4
age = 14
color = "빨강"
print(f"나는 {age}살 이며 {color}색을 좋아해요")
