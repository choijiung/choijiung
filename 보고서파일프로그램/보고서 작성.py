for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- " + str(i) + "주차 주간보고 -\n부서 : \n이름 : \n업무요악 : ")