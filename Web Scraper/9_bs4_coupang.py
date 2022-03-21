import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
hearders = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
res = requests.get(url, headers=hearders)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


items = soup.find_all("li", attrs={"class" : re.compile("^search-product")})
# print(items[0].find("div", attrs={"class" : "name"}).get_text())
for item in items:

    #광고 제외
    ad_badge = item.find("span", attrs={"class" : "ad-badge-text"})
    if ad_badge:
        print("     <광고 상품 제외합니다>")
        continue

    name = item.find("div", attrs={"class" : "name"}).get_text()

    if "Apple" in name:
        print("    <Apple 상품 제외합니다>")
        continue

    price = item.find("strong", attrs={"class" : "price-value"}).get_text()

    #리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class": "rating"})
    if rate:
        rate = rate.get_text()
    else:
        print("     <평점 없는 상품 제외합니다>")
        continue
    rate_count = item.find("span", attrs={"class": "rating-total-count"})
    if rate_count:
        rate_count = rate_count.get_text()
        rate_count = rate_count[1:-1]
    else:
        print("     <평점 없는 상품 제외합니다>")
        continue

    if float(rate) >= 4.5 and int (rate_count) >= 100:
        print("이름 : {0}     /     가격 : {1}      /     평점 : {2}      /         평점 수 : {3}".format(name, price, rate, rate_count))