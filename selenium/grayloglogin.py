#!/usr/bin/python

import time, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = 1

if chrome:
    driver = webdriver.Chrome()
else:
    profile = webdriver.FirefoxProfile()
    driver = webdriver.Firefox(profile, timeout = 100)

driver.get("http://172.17.12.11:9000")


def grayloglogin():
    username=driver.find_element_by_xpath("//input[@placeholder='Username']")
    password=driver.find_element_by_xpath("//input[@placeholder='Password']")
    username.send_keys(Keys.CLEAR)
    username.send_keys('admin')
    password.send_keys(Keys.CLEAR)
    password.send_keys('graylogadmin')
    password.send_keys(Keys.ENTER)

try:
    grayloglogin()
except:
    try:
        grayloglogin()
    except:
        print("Error logging into Graylog web interface")
        driver.close()
        sys.exit(1)

try:
    print("Ctrl-C to exit")
    while (1):
        time.sleep(1)
except:
    driver.close()
