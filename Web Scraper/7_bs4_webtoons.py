import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#네이버 웹툰 전체 목록 가져오기
caetoons = soup.find_all("a", attrs={"class":"title"})
for caetoon in caetoons:
    print(caetoon.get_text())

