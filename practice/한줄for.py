#번호 바꾸기
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

#학생 이름을 길이로 변환
students = ["Iron man", "Thor", "groot"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 바꾸기
students = ["Iron man", "Thor", "groot"]
students = [i.upper() for i in students]
print(students)