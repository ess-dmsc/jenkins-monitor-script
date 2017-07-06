#!/usr/bin/python

import time, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://github.com/orgs/ess-dmsc/dashboard")


def grayloglogin(login_xpath, password_xpath, login_text, password_text):
    username=driver.find_element_by_xpath(login_xpath)
    password=driver.find_element_by_xpath(password_xpath)
    username.send_keys(Keys.CLEAR)
    username.send_keys(login_text)
    password.send_keys(Keys.CLEAR)
    password.send_keys(password_text)
    password.send_keys(Keys.ENTER)

try:
    grayloglogin("//input[@name='login']", "//input[@name='password']", "mortenjc", "xxxxx")
except:
    print("Second time")
    try:
        grayloglogin("//input[@name='login']", "//input[@name='password']", "mortenjc", "xxxxx")
    except:
        print("Error logging into github web interface")
        driver.close()
        sys.exit(1)

try:
    print("Ctrl-C to exit")
    while (1):
        time.sleep(1)
except:
    driver.close()
