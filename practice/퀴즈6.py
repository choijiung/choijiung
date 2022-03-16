def std_weight(height, gender):
    global standard_weight
    if gender == "남자":
        standard_weight = int(height) * int(height) * 22 / 10000
        standard_weight = round(standard_weight, 2)
        print("키 {0}의 남자의 표준 체중은 {1}kg 입니다".format(height, standard_weight))

    elif gender == "여자":
        standard_weight = int(height) * int(height) * 21 / 10000
        standard_weight = round(standard_weight, 2)
        print("키 {0}의 여자의 표준 체중은 {1}kg 입니다".format(height, standard_weight))

std_weight(175, "남자")