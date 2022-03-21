# from email import header
# from attr import attr
# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
#     "Accept-Language":"ko-KR,ko"
#     }
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")


# movies = soup.find_all("div", attrs={"class" : "ULeU3b neq64b"})
# print(len(movies))

#with open("Web Scraper/movie.html", "w", encoding="utf8") as w:
#    w.write(soup.prettify())
# for movie in movies:
#     title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
#     print(title)

from selenium import webdriver
import time
browser = webdriver.Chrome(r"D:\지웅현서\Coding File\Web Scraper\chromedriver.exe")
browser.maximize_window()

url = "https://www.google.com/search?q=%EC%BD%94%EB%94%A9&rlz=1C1CHZN_koKR971KR971&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj1q5Syotf2AhUsIqYKHZhND7YQ_AUoAXoECAEQAw&biw=1366&bih=625&dpr=1&safe=active&ssui=on"
browser.get(url)

# browser.execute_script("window.scrollTo(0, 768)")
# browser.execute_script("window.scrollTo(0, 2080)")
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height
print("스크롤 완료")
time.sleep(20)