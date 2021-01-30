# WorkHuntr

WorkHuntr is a website that aids users in their job search or their search for help on projects. Each user is divided into one of two categories: a huntee, someone who is looking for assistance on a job/project, or a hunter, someone who is looking to be hired for a job/project. Your category is determined by your choice on the create profile screen, which is where you will also provide your general personal information (name, age, sex) and the company you currently work for (you'll also have the ability to declare unemployed). Once on the home screen, you will get the option to navigate between the different pages (https://github.com/SCCapstone/GiantNerds/wiki/Design). The goal is to create an easy to use hub where potential employers and employees can have quick access to one another in a centralized place. A lot of the interaction between users comes from the built-in inbox functionality and the listing pages, where huntees can post jobs they're looking for assistance on, or hunters can search for new projects to work on. We will also have a built-in payment function, allowing hunters to pay the huntees that work on their projects.

## Prerequisites

In order to build this project you will first have to install:
* [Python 3](https://www.python.org/downloads/)
* [Pip3](https://pip.pypa.io/en/stable/installing/)
* [Django](https://www.djangoproject.com/download/)
* [Requests](https://pypi.org/project/requests/)
* [Selenium](https://pypi.org/project/selenium/)

See below for installation steps.

## Setup

There are a few steps you will need to follow before running WorkHuntr.

1. To install Python3, run
```
sudo apt-get update
sudo apt-get install python3.6
```
2. To verify installation, run
```
python3 --version
```
2. To install dependencies, run
```
pip3 install -r requirements.txt
```

## Running

1. To start the web app run, `python3 manage.py runserver` within the `workhuntr/` directory.
2. Navigate to `localhost:8000` on your browser.

## Style Guide

The style guide that was used is the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

# Deployment

WorkHuntr is currently deployed to www.workhuntr.com

# Testing

Currently, there are only two tests supported. Unit testing such as the one for testing listing database functionality uses Django’s built in unittest module. The UI tests utilize selenium and ChromeDriver to automate tests for login page functionality.

## Testing Technology

For unit tests, nothing more is currently needed outside of built in Django modules. For UI testing, selenium must be installed using pip (refer to prerequisites and setup above) and ChromeDriver must also be installed. ChromeDriver is specific to the tester user and the version required is dependent on the OS the tester is using as well as the version of Google Chrome the tester has installed. The currently uploaded version of ChromeDriver in the repo is for Google Chrome Version 88.0.4324.104 (Official Build) (64-bit) on Windows and uses ChromeDriver version ChromeDriver 88.0.4324.96.

## Running Tests
Before running any tests, create a user profile on your local copy of the server with the following information: Title, First name, Last name, Gender, Account type, and Email can be anything. the USERNAME must be `testUser` and the PASSWORD must be `Workhuntr1`

For example:
Title=Mr. First name=test Last name=test Gender=Male Account type=Huntee Username=testUser email=test@testing.com Password=Workhuntr1 Password confirmation=Workhuntr1

This is to ensure that when the UI test runs, there is actually a user for it to look for and test that it can log in successfully.

Creating this testUser only needs to be done once to your local copy.

To run Unit Tests, run `python3 manage.py test` in the `workhuntr/` directory. This command will run all test/test files that begin with `test`. 
To run UI Tests, run `python3 #.py` in the `UITesting/` directory, where # is the name of the test file you wish to run. For example, run `python3 test_login.py` in the `UITesting/` directory to run the test for successful and unsuccessful logins.

# Authors

* ***Manager, Pessimist*** Timothy Bollman tbollman@email.sc.edu

* ***Editor*** Noah Shaw ncshaw@email.sc.edu

* ***Repo Master*** Justin Hill jah18@email.sc.edu

* ***Tester, Challenger*** Matthew "Re" Re mjre@email.sc.edu

* ***Researcher*** Angel Nguyen tienn@email.sc.edu
