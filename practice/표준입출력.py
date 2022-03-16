# import sys
# print("파이썬, 자바", sep =",", end = "?")
# print(" 무엇이 더 재미있을까요")
# print("파이썬, 자바", file=sys.stderr)
# print("파이썬, 자바", file=sys.stdout)

#scores = {"수학": 0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3))


# awnser = input("아무 값이나 입력하세요")
awnser = 10
print(type(awnser))
print("입력하신 값은 " + awnser + "입니다")