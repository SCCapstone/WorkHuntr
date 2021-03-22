from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# For testing a successful login

# WorkHuntr test login
USERNAME = "testMaker"
PASSWORD = "Workhuntr1"

driver = webdriver.Chrome("chromedriver.exe")

# Go to login page
urlLogin = "http://127.0.0.1:8000/login/"
driver.get(urlLogin)
# Find username field
driver.find_element_by_name("username").send_keys(USERNAME)
# Find password field
driver.find_element_by_name("password").send_keys(PASSWORD)
# Login
driver.find_element_by_id("loginButton").click()

# Wait for load
WebDriverWait(driver=driver, timeout=20)

url = driver.current_url

# find listing field
driver.find_element_by_id("dashListingButton").click()

#create Listing
driver.find_element_by_id("CreateListingBTN").click()

ListingTitle="CREATE THIS TEST"

driver.find_element_by_name("title").send_keys(ListingTitle)
driver.find_element_by_name("price").send_keys("10")
driver.find_element_by_name("description").send_keys("This is a generated test listing")

driver.find_element_by_id("ListingSubmitBTN").click()

fetch = driver.find_element_by_xpath("/html/body/main/div/div/div[1]").text

whatToCompare = "The listing " + ListingTitle + " has been created!"

if fetch == whatToCompare:
    print("LISTING TEST SUCCESSFUL")
else:
    print("LISTING TEST FAILURE")

driver.close()