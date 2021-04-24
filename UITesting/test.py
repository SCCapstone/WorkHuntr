import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# IN ORDER TO RUN TESTS, YOU MUST HAVE THE ACCOUNT CREATED WITH THE INFORMATION BELOW (username & password)
# YOU SHOULD THEN TRY TO LOG INTO THE EMAIL PROVIDED BELOW (gmail & gmailpassword)
# CHROME HAS WAS TOO MANY SECURITY FEATURES I HAVE NO CLUE ON HOW TO BYPASS
# LOGGING IN ON ANY CHROME BROWSER FIRST SHOULD IDEALLY ENSURE THAT WHEN THE TESTS TRY TO RUN
# YOU DON'T GET THAT "hey you're logging in from a new location" MESSAGE
# THERE IS NO BACKUP EMAIL AND THERE IS NO BACKUP PHONE NUMBER, SO IT SHOULDN'T ASK FOR ONE


# WorkHuntr test login
USERNAME = "Matthewjre"
PASSWORD = "Workhuntr1"
GMAIL = "newworkhuntrtester@gmail.com"
GMAILPASSWORD = "thispass142"
testCount = 0
failedTests = ""

driver = webdriver.Chrome("chromedriver.exe")

print("RUNNING TESTS...")

try:
    print("RUNNING LOGIN TEST...")
    # Go to login page
    urlLogin = "https://workhuntr.herokuapp.com/login/"
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

    wait = WebDriverWait(driver, 20)
    wait.until(lambda driver: driver.current_url == "https://mail.google.com/mail/u/0/#inbox")

    source = driver.page_source

    driver.implicitly_wait(4)

    subSTR = source.find("Your two-factor verification code for WorkHuntr is ")

    key = ""
    for i in range(subSTR+51, subSTR+56):
        key += source[i]

    print("Debug: KEY=" + key)

#    driver.find_element_by_xpath("//*[@id=\":28\"]/div[1]/span").click()


#    driver.find_element_by_xpath("//*[@id=\":4\"]/div/div[1]/div[1]/div/div/div[2]/div[3]/div").click()

    driver.close()#close gmail

    driver.switch_to.window(driver.window_handles[0])#workhuntr

    driver.find_element_by_name("number").send_keys(key)

    driver.find_element_by_id("loginButton").click()

    print("LOGIN SUCCESSFUL")
    testCount += 1
except:
    print("Login failed")
    failedTests += "\nlogin test fail\n"

"""
try:
    print("RUNNING PROFILE UPDATE TEST...")

    #go to the profile and start editing
    driver.find_element_by_xpath("//*[@id=\"dashProfileButton\"]").click()
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
    print("TESTING ADDING SKILLS AND HISTORY...")
    # from profile, click on the skills
    driver.find_element_by_id("skillBTN").click()

    # add a skill and submit
    driver.find_element_by_xpath("//*[@id=\"id_skill\"]").send_keys("writing tests")
    driver.find_element_by_xpath("/html/body/main/div/form/div/button").click()

    # click on history
    driver.get("http://127.0.0.1:8000/add_work_history/WorkhuntrTester/")

    # Fill out the history form
    driver.find_element_by_xpath("//*[@id=\"id_company\"]").send_keys("Worhuntr development")
    driver.find_element_by_xpath("//*[@id=\"id_start_date\"]").send_keys("08/22/2015")
    driver.find_element_by_xpath("//*[@id=\"id_end_date\"]").send_keys("08/22/2018")
    driver.find_element_by_xpath("//*[@id=\"id_description\"]").send_keys("try to do things without breaking more")

    # submit
    driver.find_element_by_xpath("/html/body/main/div/form/div/button").click()

    print("ADDING SKILLS AND HISTORY SUCCESSFUL")
    testCount += 1
except:
    print("ADDING SKILLS AND HISTORY FILED")
    failedTests += "\nadding skills and history fail\n"

try:
    print("TESTING LISTING CREATION")
    # find listing field
    driver.get("http://127.0.0.1:8000/current_listings/")

    # create Listing
    driver.find_element_by_id("CreateListingBTN").click()

    ListingTitle = "CREATE THIS TEST"

    driver.find_element_by_name("title").send_keys(ListingTitle)
    driver.find_element_by_name("price").send_keys("10")
    driver.find_element_by_name("description").send_keys("This is a generated test listing")

    driver.find_element_by_id("ListingSubmitBTN").click()

    fetch = driver.find_element_by_xpath("/html/body/main/div/div/div[1]").text
    testCount += 1
except:
    print("LISTING TEST FAILED")
    failedTests += "\nlisting test fail\n"

print("\n\nSUCCESSFULLY RAN " + str(testCount) + " TESTS")
if failedTests != "":
    print(str(failedTests) + " TESTS FAILED DURING RUNNING")


driver.switch_to.window(driver.window_handles[0])  # workhuntr
driver.close()"""