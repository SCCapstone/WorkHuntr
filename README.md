# WorkHuntr

WorkHuntr is a website that aids users in their job search or their search for help on projects. Each user is divided into one of two categories: a huntee, someone who is looking for assistance on a job/project, or a hunter, someone who is looking to be hired for a job/project. Your category is determined by your choice on the create profile screen, which is where you will also provide your general personal information (name, age, sex) and the company you currently work for (you'll also have the ability to declare unemployed). Once on the home screen, you will get the option to navigate between the different pages (https://github.com/SCCapstone/GiantNerds/wiki/Design). The goal is to create an easy to use hub where potential employers and employees can have quick access to one another in a centralized place. A lot of the interaction between users comes from the built-in inbox functionality and the listing pages, where huntees can post jobs they're looking for assistance on, or hunters can search for new projects to work on. We will also have a built-in payment function, allowing huntees to pay the hunters that work on their projects.

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
Unit testing such as the one for testing listing database functionality uses Django’s built in unittest module. There are currently 11 tests for Workhuntr's databases. The UI tests utilize selenium and ChromeDriver to automate tests for login page functionality. Including the "test" for creating the test user, there are currently 5 UI Tests.

## Testing Technology

For unit tests, nothing more is currently needed outside of built in Django modules. For UI testing, selenium must be installed using pip (refer to prerequisites and setup above) and ChromeDriver must also be downloaded and placed in the `UITesting/` directory. ChromeDriver is specific to the tester user and the version required is dependent on the OS the tester is using as well as the version of Google Chrome the tester has installed. The currently uploaded version of ChromeDriver in the repo is for Google Chrome Version 88.0.4324.104 (Official Build) (64-bit) on Windows and uses ChromeDriver version ChromeDriver 88.0.4324.96.

Download Chromedriver [here](https://sites.google.com/a/chromium.org/chromedriver/home).

## Running Tests

To run Unit Tests, run `python3 manage.py test` in the `workhuntr/` directory. This command will run all test/test files that begin with `test`. 

To run UI Tests, go into the `UITesting/` and read the README associated with UI Testing for specific information / instrctions.

# Authors

* ***Manager, Pessimist*** Timothy Bollman tbollman@email.sc.edu

* ***Editor*** Noah Shaw ncshaw@email.sc.edu

* ***Repo Master*** Justin Hill jah18@email.sc.edu

* ***Tester, Challenger*** Matthew "Re" Re mjre@email.sc.edu

* ***Researcher*** Angel Nguyen tienn@email.sc.edu
