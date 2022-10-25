import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.gismeteo.ru/")

sleep(3)
browser.find_element(By.XPATH, '//input[@type="search"]').click()
sleep(3)
browser.find_element(By.XPATH, '//input[@type="search"]').send_keys('донецк ростовская область')
sleep(3)
browser.find_element(By.XPATH, '//div/a[@class="search-item list-item icon-menu icon-menu-gray"][position() <= 1]').click()
sleep(3)

# url = "https://www.gismeteo.ru/"
#
# headers = {
#     "accept": "*/*",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
# }
# reg = requests.get(url, headers=headers)
# src = reg.text
# # print(src)
#
# with open("index.html", "w", encoding="utf 8") as file:
#     file.write(src)


