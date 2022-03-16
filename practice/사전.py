cabinet = {3:'유재석', 100:'최지웅'}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) <- ERROR
print(cabinet.get(5)) # <- NONE
print(cabinet.get(5, "사용가능"))

print(3 in cabinet)
print(5 in cabinet)



cabinet = {"A-1":"최지웅", "B-2":"유재석"}
print(cabinet.get("A-1"))
print(cabinet.get("B-2"))

#새 손님
print(cabinet)
cabinet["A-1"] = "김종국"
cabinet["C-3"] = "조세호"
print(cabinet)

#간 손님
del cabinet["B-2"]
print(cabinet)

#key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key,value 쌍으로 출력
print(cabinet.items())

#목욕탕 영업종료
cabinet.clear()
print(cabinet)