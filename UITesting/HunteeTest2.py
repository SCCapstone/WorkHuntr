import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# WorkHuntr test login
USERNAME = "WorkhuntrTester"
USERNAMEHUNTER = "WorkhuntrHunter"
PASSWORD = "Thispass142"
GMAIL = "WorkhuntrTester@gmail.com"
GMAILPASSWORD = "thispass142"
testCount = 0
failedTests = ""

driver = webdriver.Chrome("chromedriver.exe")

print("RUNNING TESTS...")

try:
    print("Logging into the Huntee account...")
    # Go to login page
    urlLogin = "http://127.0.0.1:8000/login/"
    driver.get(urlLogin)
    # Find username field
    driver.find_element_by_name("username").send_keys(USERNAME)
    # Find password field
    driver.find_element_by_name("password").send_keys(PASSWORD)
    # Login
    driver.find_element_by_id("loginButton").click()

    # open a new tab to access gmail
    driver.execute_script("window.open('https://www.gmail.com');")

    # Switch the driver to gmail tab
    driver.switch_to.window(driver.window_handles[1])#chrome

    # enter the gmail
    driver.find_element_by_name("identifier").send_keys(GMAIL)

    # A wait function that I'm not convinced works
    driver.implicitly_wait(1)

    # next button
    next = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
    next[0].click()

    # Another wait function that I'm not convinced works
    driver.set_page_load_timeout(10)

    # finds password and logs in
    driver.find_element_by_name('password').send_keys(GMAILPASSWORD)
    nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
    nextButton[0].click()

    # A 3rd wait function that im not convinced works
    wait = WebDriverWait(driver, 20)
    # forces Selenium to wait until the inbox has loaded (the url reflects the inbox)
    wait.until(lambda driver: driver.current_url == "https://mail.google.com/mail/u/0/#inbox")
    print("HELLA")
    time.sleep(1)
    # Grabs the page source to fetch the password
    source = driver.page_source
    time.sleep(1)
    print("WPOASD")
    # finds the index of the 2FA password in the page source & grabs the 5 random numbers
    subSTR = source.find("Your two-factor verification code for WorkHuntr is ")
    key = ""
    for i in range(subSTR+51, subSTR+56):
        key += source[i]
    print("Got the key",key)
    # Deletes the email so that it can easily find the code the next time it logs in
    driver.find_element_by_xpath("//*[@id=\":1z\"]/div[1]/span").click()
    driver.find_element_by_xpath("//*[@id=\":4\"]/div/div[1]/div[1]/div/div/div[2]/div[3]/div").click()

    # if you don't wait for a second or two, selenium moves on before gmail registers the click on the trashcan
    time.sleep(2)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])#workhuntr

    # enter the 2FA code and login
    driver.find_element_by_name("number").send_keys(key)
    driver.find_element_by_id("loginButton").click()

    print("LOGIN SUCCESSFUL")
except:
    print("Login failed")
    failedTests += "\nlogin test fail\n"

try:
    print("RUNNING PAYMENT TEST")
    # head to the listing tab
    driver.find_element_by_xpath("//*[@id=\"navbarToggle\"]/div[1]/a[2]").click()

    # hit issue payment
    driver.find_element_by_xpath("//*[@id=\"ListingsMain\"]/div[3]/table/tbody/tr[2]/td[5]/a").click()

    # Fill out the payment form
    driver.find_element_by_id("id_first_name").send_keys("Test")
    driver.find_element_by_id("id_last_name").send_keys("Monkey")
    driver.find_element_by_id("id_card_number").send_keys("1234567891234567")
    driver.find_element_by_id("id_exp_month").send_keys("12")
    driver.find_element_by_id("id_exp_year").send_keys("2025")
    driver.find_element_by_id("id_cvv").send_keys("111")
    driver.find_element_by_id("id_street_address").send_keys("Im not putting my address")
    driver.find_element_by_id("id_billing_city").send_keys("columbia")
    driver.find_element_by_id("id_zip").send_keys("12345")

    # hit issue payment
    driver.find_element_by_xpath("/html/body/main/div/div/div/form/input[2]").click()

    print("PAYMENT TEST SUCCESS")
    testCount+=1
except:
    print("PAYMENT TEST FAIL")
    failedTests += "\npayment test fail\n"

if testCount == 1:
    print("All (" + str(testCount) + ") tests ran without errors.")
else:
    print("\n\n" + "Number of test run: " + str(testCount) + " + Account creation test.")
    print("\nFailed tests:\n"+failedTests)

# Clean up

# Delete the listing so it doesn't get in the way of future tests
driver.find_element_by_xpath("//*[@id=\"ListingsMain\"]/div[4]/table/tbody/tr[2]/td[5]/a").click()
driver.find_element_by_xpath("/html/body/main/div/div/div/form/input[2]").click()

# Head to the messages and delete them
driver.find_element_by_xpath("//*[@id=\"navbarToggle\"]/div[1]/li/a").click()
driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div/div/div/p[1]/a[2]").click()
driver.find_element_by_xpath("/html/body/main/div/div/div/div/form/button").click()

driver.switch_to.window(driver.window_handles[0])  # workhuntr
driver.close()