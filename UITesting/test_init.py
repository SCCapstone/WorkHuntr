import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

USERNAMEHUNTEE = "WorkhuntrTester"
USERNAMEHUNTER = "WorkhuntrHunter"
PASSWORD = "Thispass142"
GMAIL = "WorkhuntrTester@gmail.com"
GMAILPASSWORD = "thispass142"

driver = webdriver.Chrome("chromedriver.exe")

print("INITIALIZING TEST USER HUNTEE...")

driver.get("http://127.0.0.1:8000/create_account/")

wait = WebDriverWait(driver, 10)
wait.until(lambda driver: driver.current_url == "http://127.0.0.1:8000/create_account/")

driver.find_element_by_id("id_email").send_keys(GMAIL)

driver.find_element_by_name("first_name").send_keys("Test")

driver.find_element_by_name("last_name").send_keys("monkey")

driver.find_element_by_name("birthday").click()
driver.find_element_by_name("birthday").send_keys(Keys.SPACE + Keys.TAB + Keys.RETURN)

driver.find_element_by_name("current_employment").send_keys("test guy")

driver.find_element_by_name("username").send_keys(USERNAMEHUNTEE)

driver.find_element_by_name("password1").send_keys(PASSWORD)

driver.find_element_by_name("password2").send_keys(PASSWORD)

driver.find_element_by_id("signUPBTN").click()

print("TEST HUNTEE CREATED")

print("INITIALIZING TEST USER HUNTER...")

driver.get("http://127.0.0.1:8000/create_account/")

wait = WebDriverWait(driver, 10)
wait.until(lambda driver: driver.current_url == "http://127.0.0.1:8000/create_account/")

dropdown = Select(driver.find_element_by_name("account_type"))
dropdown.select_by_value("Hunter")

driver.find_element_by_id("id_email").send_keys(GMAIL)

driver.find_element_by_name("first_name").send_keys("Test")

driver.find_element_by_name("last_name").send_keys("monkey")

driver.find_element_by_name("birthday").click()
driver.find_element_by_name("birthday").send_keys(Keys.SPACE + Keys.TAB + Keys.RETURN)

driver.find_element_by_name("current_employment").send_keys("test guy")

driver.find_element_by_name("username").send_keys(USERNAMEHUNTER)

driver.find_element_by_name("password1").send_keys(PASSWORD)

driver.find_element_by_name("password2").send_keys(PASSWORD)

driver.find_element_by_id("signUPBTN").click()

print("TEST HUNTER CREATED")


driver.close()









