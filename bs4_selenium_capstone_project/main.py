import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfHk79LcT4ck0noY_xksng0jzDCvBL97dPjDYMCbjtVhs45mQ/viewform"


def fill_form(price, address, link):

    driver.get(GOOGLE_FORM_URL)
    wait = WebDriverWait(driver, timeout=3)
    inputs = driver.find_elements(By.CSS_SELECTOR, ".whsOnd")
    print()


# Selenium configurations
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

response = requests.get(ZILLOW_URL)
zillow_page = response.text

soup = BeautifulSoup(zillow_page, "html.parser")

details = soup.find_all(class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

for detail in details[:6]:
    property_price = detail.find(class_="PropertyCardWrapper__StyledPriceLine")
    link = detail.find(name="a")
    property_address = detail.find(name="address")
    if property_price is not None and property_address is not None and link is not None:
        fill_form(price=property_price, address=property_address, link=link)
