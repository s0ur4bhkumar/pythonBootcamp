import time

from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference("detach", True)

driver = webdriver.Firefox(options=firefox_options)
driver.get("https://ozh.github.io/cookieclicker/")

cookie = driver.find_element(By.ID, value="bigCookie")


t_end = time.time() + 5
time.sleep(5)
while time.time() < t_end:
    cookie.click()


input("click enter to exit")
