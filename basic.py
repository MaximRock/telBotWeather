from geopy.geocoders import Nominatim
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.gismeteo.ru/")

geolokator = Nominatim(user_agent="user")
location = geolokator.geocode("archipovka, Russia")

lst = list(map(str, location.address.split()))
s = lst.index('область,')
msg = ((f'{lst[2][:-1]} {lst[s-1]} {lst[s][:-1]} {lst[-1]}') if lst[0] == 'городской' else (f'{lst[0][:-1]} {lst[s-1]} {lst[s][:-1]} {lst[-1]}'))

sleep(3)
browser.find_element(By.XPATH, '//input[@type="search"]').click()
sleep(3)
browser.find_element(By.XPATH, '//input[@type="search"]').send_keys(msg)
sleep(3)
browser.find_element(By.XPATH, '//div/a[@class="search-item list-item icon-menu icon-menu-gray"][position() <= 1]').click()
sleep(3)