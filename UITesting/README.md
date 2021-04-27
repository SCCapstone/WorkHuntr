
## Testing Technology

For UI testing, selenium must be installed using pip (refer to the README in the main directory) and ChromeDriver must also be downloaded and placed in the `UITesting/` directory. Currently, ChomeDriver is already in the proper directory, so no download is needed unless Chrome updates in between me posting this and someone trying to test it) ChromeDriver is specific to the tester user and the version required is dependent on the OS the tester is using as well as the version of Google Chrome the tester has installed. The currently uploaded version of ChromeDriver in the repo is for Google Chrome Version 90.0.4430.85 (Official Build) (64-bit) on Windows and uses ChromeDriver version ChromeDriver 90.0.4430.24

Download Chromedriver [here](https://sites.google.com/a/chromium.org/chromedriver/home).

# IMPORTANT

Because of Gmail security, whenever attempting to login to either Gmail accounts, Gmail will attempt to have the user login to the email by either using a phone number or adding a phone number. There is no phone number associated with the Gmail account. To prevent this from interfering with the UITesting process, use the below Gmail logins to attempt to login to BOTH the Gmails before running the tests. You might be prompted to add/enter a phone number. If there is an update option, simply hitting "update" seems to stop Gmail from asking. If there isn't an "update" option and you only have unclickable "next" options, simply close the browser. This should stop gmail from asking. This only has to be done once assuming your IP / location is not changing. Unfortunately, there is no way around this as there's no way to stop gmail from asking and other email providers have their own security issues.

you can access the Gmail with this information:

Huntee login = "WorkhuntrTester@gmail.com"
password = "thispass142"

Hunter login = "WorkhuntrHunter@gmail.com"
password = "thispass142" (yes, they're the same)

## Preparing To Run Tests
Before running any tests, I recommend starting from a fresh clone. While I've tested with clones that aren't fresh, it made it easier to follow with a clean one.

Before running any tests, if starting from a clean clone, be sure to set up the database file. this can be achieved by navigating to the base `WorkHuntr` directory and running:

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py migrate --run-syncdb

Now that the database is ready, in the same directory, run:

python3 manage.py runserver

to run the local server. Then, in a new terminal, head to the `WorkHuntr/UITesting/` directory to begin running the test files.

## Running Tests

Before running any tests, you must initialize the test users by running the `test_init.py` file by navigating to the `UITesting/` directory and running `python3 test_init.py`. This will open selenium chromedriver and automatically navigate to the user creation of WorkHuntr and create the profiles with the correct username, password, and Gmail necessary for running the tests.

Creating this testUser via `test_init.py` only needs to be done ONCE to your local copy.

To run the UI Tests you mut run 3 different test files. Because of some unexplainable error with gmail, the test files had to be split every time you needed to log into an account and get past the 2FA.

you MUST run the tests in this order:

0) test_init.py (if you haven't already)
1) HunteeTest1.py
2) HunterTest.py
3) HunteeTest2.py

to run these files, run `python3 <testFileName>.py` in the `UITesting/` directory. 


# Known bugs:

~ While this hasn't happened to me since Easter, with Gmail, there is an issue in viewing the page's source that occurs one in very few instances of trying to run the tests. Selenium fetches the 2FA code by viewing the inbox's source page and searching for the substring that contains the 2FA password. Rarely, the source will not display the 2FA email and instead just have a message saying there's an issue and that the Gmail is currently unavailable. It is currently unknown what causes this issue. Should this issue arise during testing, close all browsers that have the Gmail open and wait a minute before running the test again. This normally fixes the issue, albeit temporarily.
