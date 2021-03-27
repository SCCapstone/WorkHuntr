import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# IN ORDER TO RUN TESTS, YOU SHOULD TRY TO LOG INTO THE EMAIL PROVIDED BELOW
# CHROME HAS WAS TOO MANY SECURITY FEATURES I HAVE NO CLUE ON HOW TO BYPASS
# LOGGING IN ON ANY CHROME BROWSER FIRST SHOULD IDEALLY ENSURE THAT WHEN THE TESTS TRY TO RUN
# YOU DON'T GET THAT "hey you're logging in from a new location" MESSAGE
# THERE IS NO BACKUP EMAIL AND THERE IS NO BACKUP PHONE NUMBER, SO IT SHOULDN'T ASK FOR ONE


# WorkHuntr test login
USERNAME = "WorkhuntrTester"
PASSWORD = "Thispass142"
GMAIL = "WorkhuntrTester@gmail.com"
GMAILPASSWORD = "thispass142"

driver = webdriver.Chrome("chromedriver.exe")

try:
    # Go to login page
    urlLogin = "http://127.0.0.1:8000/login/"
    driver.get(urlLogin)
    # Find username field
    driver.find_element_by_name("username").send_keys(USERNAME)
    # Find password field
    driver.find_element_by_name("password").send_keys(PASSWORD)
    # Login
    driver.find_element_by_id("loginButton").click()

    driver.execute_script("window.open('https://www.gmail.com');")

    driver.switch_to.window(driver.window_handles[1])#chrome

    driver.find_element_by_name("identifier").send_keys(GMAIL)

    driver.implicitly_wait(1)

    next = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
    next[0].click()

    driver.set_page_load_timeout(10)

    driver.find_element_by_name('password').send_keys(GMAILPASSWORD)

    nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
    nextButton[0].click()

    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url == "https://mail.google.com/mail/u/0/#inbox")

    source = driver.page_source

    driver.implicitly_wait(4)

    subSTR = source.find("Your two-factor verification code for WorkHuntr is ")

    key = ""
    for i in range(subSTR+51, subSTR+56):
        key += source[i]

    driver.find_element_by_xpath("//*[@id=\":28\"]/div[1]/span").click()

    driver.find_element_by_xpath("//*[@id=\":4\"]/div/div[1]/div[1]/div/div/div[2]/div[3]/div").click()

    driver.switch_to.window(driver.window_handles[0])#workhuntr

    driver.find_element_by_name("number").send_keys(key)

    driver.find_element_by_id("loginButton").click()





    print("Login successful")
except:
    print("Login failed")

driver.switch_to.window(driver.window_handles[1])#chrome
driver.close()
driver.switch_to.window(driver.window_handles[0])#workhuntr
driver.close()