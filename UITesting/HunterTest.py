import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# WorkHuntr test login
USERNAMEHUNTER = "WorkhuntrHunter"
PASSWORD = "Thispass142"
GMAIL = "WorkhuntrHunter@gmail.com"
GMAILPASSWORD = "thispass142"
testCount = 0
failedTests = ""

driver = webdriver.Chrome("chromedriver.exe")

print("RUNNING TESTS...")

try:
    print("RUNNING LOGIN TEST...")
    # Go to login page
    urlLogin = "http://127.0.0.1:8000/login/"
    driver.get(urlLogin)
    # Find username field
    driver.find_element_by_name("username").send_keys(USERNAMEHUNTER)
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

    # Grabs the page source to fetch the password
    source = driver.page_source
    time.sleep(1)

    # finds the index of the 2FA password in the page source & grabs the 5 random numbers
    subSTR = source.find("Your two-factor verification code for WorkHuntr is ")
    key = ""
    for i in range(subSTR+51, subSTR+56):
        key += source[i]

    # Deletes the email so that it can easily find the code the next time it logs in
    driver.find_element_by_xpath("//*[@id=\":1z\"]/div[1]/span").click()
    driver.find_element_by_xpath("//*[@id=\":4\"]/div/div[1]/div[1]/div/div/div[2]/div[3]/div").click()

    # if you don't wait for a second or two, selenium moves on before gmail registers the click on the trashcan
    time.sleep(2)


    # Close gmail and switch the active tab back to workhuntr
    driver.close()
    driver.switch_to.window(driver.window_handles[0])#workhuntr

    # enter the 2FA code and login
    driver.find_element_by_name("number").send_keys(key)
    driver.find_element_by_id("loginButton").click()

    print("LOGIN SUCCESSFUL")
    testCount += 1
except:
    print("Login failed")
    failedTests += "\nlogin test fail\n"

try:
    testMessage = "Howdy, fella!"
    print("TESTING MESSAGE RECEIVE / REPLY")
    # Head over to message center
    driver.find_element_by_xpath("//*[@id=\"navbarToggle\"]/div[1]/li/a").click()
    # Check for the huntee's message
    driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div/div/div/p[1]/a[1]").click()
    # grab the message & check
    hunteeMessage = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/p[2]").text
    print("HUNTEE MESSAGE:",hunteeMessage)
    if hunteeMessage == testMessage:
        print("MESSAGE RECEIVE SUCCESSFUL")
        testCount+=1
    else:
        print("MESSAGE RECEIVE FAIL")
        failedTests += "\nreceive test fail\n"

    # Attempt to reply
    driver.find_element_by_xpath("//*[@id=\"message\"]").send_keys("Mornin. to ye, feller.")
    driver.find_element_by_xpath("//*[@id=\"MSGsendBTN\"]").click()
    # Check if sent
    sender = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/p[1]").text

    print("SENDER:",sender)
    if sender == "WorkhuntrHunter":
        print("MESSAGE REPLY SUCCESSFUL")
        testCount += 1
    else:
        print("MESSAGE REPLY FAIL")
        failedTests += "\nreply test fail\n"

except:
    print("MESSAGE RECEIVE / REPLY TEST FAIL")

try:
    print("TESTING LISTING CLAIM")

    #Move to the listing tab and claim the Huntee's listing
    driver.find_element_by_xpath("//*[@id=\"navbarToggle\"]/div[1]/a[2]").click()
    driver.find_element_by_xpath("//*[@id=\"ListingsMain\"]/div[1]/table/tbody/tr[2]/td[5]/form/input[2]").click()

    # Check for Success
    textCheck = driver.find_element_by_xpath("/html/body/main/div/div/ul/p").text

    if textCheck == "Listing CREATE THIS TEST has been marked claimed! WorkhuntrTester has been notified!":
        print("LISTING CLAIM SUCCESSFUL")
        testCount+=1
    else:
        print("LISTING CLAIM FAIL")
        failedTests += "\nlisting claim test fail\n"
except:
    print("LISTING CLAIM FAIL")
    failedTests += "\nlisting claim test fail\n"

try:
    print("TESTING LISTING COMPLETION")
    # click on the claimed to start updating the status
    driver.find_element_by_xpath("//*[@id=\"ListingsMain\"]/div[2]/table/tbody/tr[2]/td[4]/a").click()

    # set the status to complete and give a description.
    dropdown = Select(driver.find_element_by_name("status"))
    dropdown.select_by_value("Complete")
    driver.find_element_by_id("id_description").send_keys("This is a test description")
    driver.find_element_by_xpath("//*[@id=\"updateForm\"]/form/fieldset/input").click()

    print("LISTING COMPLETION SUCCESSFUL")
    testCount+=1

except:
    print("LISTING COMPLETION FAIL")
    failedTests += "\nlisting completion test fail\n"

if testCount == 5:
    print("All (" + str(testCount) + ") tests ran without errors.")
else:
    print("\n\n" + "Number of test run: " + str(testCount) + " + Account creation test.")
    print("\nFailed tests:\n"+failedTests)


driver.switch_to.window(driver.window_handles[0])  # workhuntr
driver.close()