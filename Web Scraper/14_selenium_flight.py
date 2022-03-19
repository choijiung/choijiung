from selenium import webdriver
import time
browser = webdriver.Chrome(r"D:\지웅현서\Coding File\Web Scraper\chromedriver.exe")
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
browser.find_element_by_class_name("sc-crzoAE hnpClg inner").click()

time.sleep(20)