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

driver.get("https://172.17.12.31:3000/dashboard/db/cspec-rate-stats")


def grafanalogin():
    username=driver.find_element_by_xpath("//input[@name='username']")
    password=driver.find_element_by_xpath("//input[@name='password']")
    username.send_keys(Keys.CLEAR)
    username.send_keys('admin')
    password.send_keys(Keys.CLEAR)
    password.send_keys('admin')
    password.send_keys(Keys.ENTER)

try:
    grafanalogin()
except:
    try:
        grafanalogin()
    except:
        print("Error logging into Grafana web interface")
        while 1:
            time.sleep(1)
        driver.close()
        sys.exit(1)

try:
    print("Ctrl-C to exit")
    while (1):
        time.sleep(1)
except:
    driver.close()
