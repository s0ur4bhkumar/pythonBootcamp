from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com")

firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference("detach", True)

driver = webdriver.Firefox(options=firefox_options)
driver.get("https://www.python.org/")

date_elements = driver.find_elements(
    By.CSS_SELECTOR, ".medium-widget.event-widget.last li"
)

py_event = {}
for date_element in date_elements:
    year = date_element.find_element(By.CLASS_NAME, "say-no-more")
    date = date_element.find_element(By.CSS_SELECTOR, "time")
    full_date = year.get_attribute("textContent") + date.text  # type: ignore
    event = date_element.find_element(By.CSS_SELECTOR, "a")
    py_event[full_date] = event.text

print(py_event)

input("press Enter to exit")
