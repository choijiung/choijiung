from selenium import webdriver  
import time

browser = webdriver.Chrome(r"D:\지웅현서\Coding File\Web Scraper\chromedriver.exe")
browser.get("https://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("wow")
browser.find_element_by_id("pw").send_keys("wow")
browser.find_element_by_class_name("switch_btn").click()


# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")


print(browser.page_source)

time.sleep(20)

browser.quit()