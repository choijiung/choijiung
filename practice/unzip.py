kor = ["사과", "바나나", "오랜지"]
eng = ["Apple", "Banana", "Orange"]

print(list(zip(kor, eng)))

mixed = [('사과', 'Apple'), ('바나나', 'Banana'), ('오랜지', 'Orange')]

print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)