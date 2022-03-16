class Hosue:
    def __init__(self, location, hosue_type, deal_type, price, completion_year):
        self.location = location
        self.hosue_type = hosue_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.hosue_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = Hosue("강남", "아파트", "매매", "10억", "2010년")
house2 = Hosue("마포", "오피스텔", "전세", "5억", "2007년")
house3 = Hosue("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)
print("총 {0} 대의 매물이 있습니다".format(len(houses)))
for house in houses:
    print(house.show_detail())