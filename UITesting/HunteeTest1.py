import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# IN ORDER TO RUN TESTS, YOU MUST HAVE THE ACCOUNT CREATED WITH THE INFORMATION BELOW (username & password)
# YOU SHOULD THEN TRY TO LOG INTO THE EMAIL PROVIDED BELOW (gmail & gmailpassword)
# CHROME HAS WAS TOO MANY SECURITY FEATURES I HAVE NO CLUE ON HOW TO BYPASS
# LOGGING IN ON ANY CHROME BROWSER FIRST SHOULD IDEALLY ENSURE THAT WHEN THE TESTS TRY TO RUN
# YOU DON'T GET THAT "hey you're logging in from a new location" MESSAGE
# THERE IS NO BACKUP EMAIL AND THERE IS NO BACKUP PHONE NUMBER, SO IT SHOULDN'T ASK FOR ONE

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
    print("RUNNING LOGIN TEST...")
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
    print("RUNNING PROFILE UPDATE TEST...")

    #go to the profile and start editing
    driver.find_element_by_id("dashProfileButton").click()
    driver.find_element_by_xpath("/html/body/main/div[2]/div/div/a").click()

    #add a website
    driver.find_element_by_name("website").send_keys("http://Workhuntr.com")

    # update the privacy of the profile
    dropdown = Select(driver.find_element_by_xpath("//*[@id=\"id_privacy\"]"))
    dropdown.select_by_value("Private")

    #update the profile
    driver.find_element_by_xpath("/html/body/main/div/form/div/button").click()
    print("PROFILE UPDATE SUCCESSFUL")
    testCount += 1
except:
    failedTests += "\nprofile update test fail\n"

try:
    print("TESTING ADDING AND DELETING SKILLS...")
    # from profile, click on the skills
    driver.find_element_by_id("SkillHistoryBTN").click()
    driver.find_element_by_id("skillBTN").click()

    # add a skill and submit
    driver.find_element_by_id("id_skill").send_keys("writing tests")
    driver.find_element_by_xpath("/html/body/main/div/form/div/button").click()

    # Delete the added skill
    driver.find_element_by_xpath("/html/body/main/div[2]/div/div/h6/a").click()
    driver.find_element_by_xpath("/html/body/main/div/form/input[2]").click()
    print("PROFILE UPDATE SUCCESSFUL")
    testCount += 1
except:
    print("ADDING/DELETING SKILLS FILED")
    failedTests += "\nskills test fail\n"

try:
    print("TESTING ADDING AND DELETING HISTORY...")
    # click on history
    driver.find_element_by_id("historyBTN").click()

    # Fill out the history form
    driver.find_element_by_name("company").send_keys("Worhuntr")

    # add start date
    driver.find_element_by_id("id_start_date").click()
    driver.find_element_by_id("id_start_date").send_keys(Keys.SPACE + Keys.TAB + Keys.RETURN)
    driver.find_element_by_id("id_start_date").send_keys("2015")

    # Add end date
    driver.find_element_by_id("id_end_date").click()
    driver.find_element_by_id("id_end_date").send_keys(Keys.SPACE + Keys.TAB + Keys.RETURN)

    driver.find_element_by_name("description").send_keys("try to do things without breaking more")

    # submit
    driver.find_element_by_xpath("/html/body/main/div/form/div/button").click()

    # Delete the history
    driver.find_element_by_xpath("//*[@id=\"accordion1\"]/h5/a[1]").click()
    driver.find_element_by_xpath("/html/body/main/div/form/input[2]").click()

    print("ADDING AND DELETING HISTORY SUCCESSFUL")
    testCount += 1
except:
    print("ADDING AND DELETING HISTORY FILED")
    failedTests += "\nadding history fail\n"

try:
    print("TESTING LISTING CREATION")
    # find listing field
    driver.find_element_by_xpath("//*[@id=\"navbarToggle\"]/div[1]/a[2]").click()

    # create Listing
    driver.find_element_by_id("createListingBTN").click()

    ListingTitle = "CREATE THIS TEST"

    # Fill in the proper elements
    driver.find_element_by_name("title").send_keys(ListingTitle)
    driver.find_element_by_name("price").send_keys("10")
    driver.find_element_by_name("description").send_keys("This is a generated test listing")
    dropdown = Select(driver.find_element_by_xpath("//*[@id=\"id_tag_one\"]"))
    dropdown.select_by_value("Java")
    dropdown = Select(driver.find_element_by_xpath("//*[@id=\"id_tag_two\"]"))
    dropdown.select_by_value("Design")

    # submit
    driver.find_element_by_id("ListingSubmitBTN").click()

    # Check for success
    fetch = driver.find_element_by_xpath("/html/body/main/div/div/ul/p").text
    if fetch == "Your listing \"" + ListingTitle +"\" has been created!":
        print("LISTING CREATION SUCCESSFUL")
        testCount += 1
except:
    print("LISTING TEST FAILED")
    failedTests += "\nlisting test fail\n"

try:
    print("TESTING LISTING MODIFICATION")

    ListingTitle = "CREATE THIS TEST"
    # Modify the description of the listing
    driver.find_element_by_id("modifyBTN").click()
    driver.find_element_by_name("description").send_keys(Keys.CONTROL+"A")
    driver.find_element_by_name("description").send_keys("This listing has been modified")
    # submit
    driver.find_element_by_id("submitModBTN").click()
    # Check for success
    fetch = driver.find_element_by_xpath("/html/body/main/div/div/ul/p").text
    if fetch == "Your listing \"" + ListingTitle +"\" has been modified!":
        print("LISTING MODIFICATION SUCCESSFUL")
        testCount += 1
except:
    print("LISTING MODIFICATION TEST FAILED")
    failedTests += "\nlisting modification test fail\n"

# This message needs to be stored outside a test since it will be called in the send and the receive test
TESTMESSAGE = "Howdy, fella!"

try:
    print("TESTING MESSAGE SENDING")

    # Access the message tab from the navbar
    driver.find_element_by_xpath("//*[@id=\"navbarToggle\"]/div[1]/li/a").click()

    # Search for the Hunter user from the search box
    driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/form/input[2]").send_keys(USERNAMEHUNTER)
    driver.find_element_by_id("MSGSearchBTN").click()

    # Send a message using the message saved above
    driver.find_element_by_id("message").send_keys(TESTMESSAGE)
    driver.find_element_by_id("MSGsendBTN").click()

    # Check for url change to signal successful send
    if driver.current_url == "http://127.0.0.1:8000/contacts/conversation/WorkhuntrHunter":
        print("MESSAGE SENT TEST SUCCESSFUL")
        testCount += 1
    else:
        print("MESSAGE SENDING FAILED")
        failedTests += "\nmessage sending test fail\n"


except:
    print("MESSAGE SENDING FAILED")
    failedTests += "\nmessage sending test fail\n"

driver.switch_to.window(driver.window_handles[0])  # workhuntr
driver.close()

if testCount == 7:
    print("All (" + str(testCount) + ") tests ran without errors.")
else:
    print("\n\n" + "Number of test run: " + str(testCount) + " + Account creation test.")
    print("\nFailed tests:\n"+failedTests)
