abset = [2,5]#결석
no_book = [7]
for student in range(1,11):
    if student in abset:
        continue
    elif student in no_book:
        print("너{0}은 당장 종아리 태형 99999999대를 맞고 오늘 수업은 끝내겠다 어명이다".format(no_book))
        print("그래 나는 왕이다")
        break
    print("{0}, 당장 책을 읽거라 어명이다!!!".format(student))