python = "Python is Amazing"
print(python.lower())#소문자로 바꾸기
print(python.upper())#대문자로 바꾸기
print(python[0].isupper())#0번째 위치가 대문자인가?
print(len(python))#길이
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))
#print(python.index("java")) <- 이것을 치면 에러

print(python.count("n"))#몇개 있는지