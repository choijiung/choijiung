input("사이트 주소를 입력해 주십시오")
url = input()
temporary = url.replace("https://", "")
temporary = temporary.replace("www.", "")
temporary = temporary[:temporary.index(".")]
password1 = temporary[:3]
password2 = password1 + str(len(temporary))
password3 = password2 + str(temporary.count("e"))
print(password3 + "!")