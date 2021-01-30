from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# For testing a successful login

# workHuntr test login
USERNAME = "testUser"
PASSWORD = "Workhuntr1"

driver = webdriver.Chrome("chromedriver.exe")

# go to login page
urlLogin = "http://127.0.0.1:8000/login/"
driver.get(urlLogin)
# find username field
driver.find_element_by_name("username").send_keys(USERNAME)
# find password field
driver.find_element_by_name("password").send_keys(PASSWORD)
# login
driver.find_element_by_id("loginButton").click()

# wait for load
WebDriverWait(driver=driver, timeout=20)

url = driver.current_url

if url == urlLogin:
    print("LOGIN FAILED")
else:
    print("LOGIN SUCCESSFUL")

# close
driver.close()


# For testing failed login

USERNAME = "dfgdfgdfg"
PASSWORD = "asdasdasd"

driver = webdriver.Chrome("chromedriver.exe")

urlLogin = "http://127.0.0.1:8000/login/"
driver.get(urlLogin)
driver.find_element_by_name("username").send_keys(USERNAME)
driver.find_element_by_name("password").send_keys(PASSWORD)
driver.find_element_by_id("loginButton").click()

WebDriverWait(driver=driver, timeout=500)

url = driver.current_url

if url == urlLogin:
    print("LOGIN FAILED")
else:
    print("LOGIN SUCCESSFUL")

# close
driver.close()

