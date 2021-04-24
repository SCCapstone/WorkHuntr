# IMPORTANT

DO NOT RUN ANY TEST FILES WHILE THE MOVE FROM LOCAL TO WEB IS IN PLACE. nothing works anyway, but running the test_init will create an account on the physical website that cannot (easily) be deleted / modified as I'm trying to fix everything.


## Testing Technology

For UI testing, selenium must be installed using pip (refer to prerequisites and setup above) and ChromeDriver must also be downloaded and placed in the `UITesting/` directory. ChromeDriver is specific to the tester user and the version required is dependent on the OS the tester is using as well as the version of Google Chrome the tester has installed. The currently uploaded version of ChromeDriver in the repo is for Google Chrome Version 90.0.4430.85 (Official Build) (64-bit) on Windows and uses ChromeDriver version ChromeDriver 90.0.4430.24

Download Chromedriver [here](https://sites.google.com/a/chromium.org/chromedriver/home).

## Running Tests
Before running any tests, you must initialize the test user by running the `test_init.py` file by navigating to the `UITesting/` directory and running `python3 test_init.py`. This will open selenium chromedriver and automatically navigate to the user creation of WorkHuntr and create the profile with the correct username, password, and Gmail necessary for running the tests.

Creating this testUser via `test_init.py` only needs to be done once to your local copy.

To run the UI Tests, run `python3 test.py` in the `UITesting/` directory. All the tests are run in the one file. 


# IMPORTANT
Due to how selenium interacts with Gmail, the inbox for the Gmail provided must be empty for the tests to run properly. Selenium is looking for the substring that Workhuntr sends with the 2FA code, and if the tests are run when there is more than one 2FA email, it is currently unable to differentiate which code is for the current instance. 

you can access the Gmail with this information:
GMAIL = "WorkhuntrTester@gmail.com"
GMAILPASSWORD = "thispass142"

Each time a test is run, if you wish to run another, log into the Gmail and clear out the inbox.

# IMPORTANT

Because of Gmail security, whenever attempting to login to a Gmail account, Gmail will attempt to have the user login to the email by either using a phone number or adding a phone number. There is no phone number associated with the Gmail account. To prevent this from interfering with the UITesting process, use the above Gmail login to attempt to login to the Gmail before running the tests. You will be prompted to add/enter a phone number. By simply closing the browser on that windows, Gmail seems to stop asking. This only has to be done once assuming your IP / location is not changing.

# Known bugs:

~ With Gmail, there is an issue in viewing the page's source that occurs one in very few instances of trying to run the tests. Selenium fetches the 2FA code by viewing the inbox's source page and searching for the substring that contains the 2FA password. Rarely, the source will not display the 2FA email and instead just have a message saying there's an issue and that the Gmail is currently unavailable. It is currently unknown what causes this issue. Should this issue arise during testing, close all browsers that have the Gmail open and wait a minute before running the test again. This normally fixes the issue, albeit temporarily.
