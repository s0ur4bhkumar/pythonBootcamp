from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com")

firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference("detach", True)

driver = webdriver.Firefox(options=firefox_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
signup = driver.find_element(By.CLASS_NAME, value="btn")
fname.send_keys("remember")
lname.send_keys("the name")
email.send_keys("rembadsdfj@gmail.com")
signup.click()

input("press enter to exit")
