input("오늘의 날씨는?")
if input() == "비" or input() == "눈":
    print("우산을 챙기세요")
elif input()  == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("오늘은 준비물이 필요 없어요")

temp = int(input("오늘 온도는"))
if 30 <= temp:
    print("너무 더워요 나가지 마세요")
elif 10 <= temp and temp < 30:
    print('괜찮은 날씨에요')
elif 0<= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")