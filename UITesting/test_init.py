import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "WorkhuntrTester"
PASSWORD = "Thispass142"
GMAIL = "WorkhuntrTester@gmail.com"
GMAILPASSWORD = "thispass142"

driver = webdriver.Chrome("chromedriver.exe")

print("INITIALIZING TEST USER...")

driver.get("http://127.0.0.1:8000/dashboard/")

driver.find_element_by_id("createACCBTN").click()

driver.find_element_by_name("email").send_keys(GMAIL)

driver.find_element_by_name("first_name").send_keys("Test")

driver.find_element_by_name("last_name").send_keys("monkey")

driver.find_element_by_name("birthday").send_keys("1999-08-22")

driver.find_element_by_name("current_employment").send_keys("test guy")

driver.find_element_by_name("username").send_keys(USERNAME)

driver.find_element_by_name("password1").send_keys(PASSWORD)

driver.find_element_by_name("password2").send_keys(PASSWORD)

driver.find_element_by_id("signUPBTN").click()

driver.close()









