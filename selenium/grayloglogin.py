#!/usr/bin/python

import time, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://172.17.0.242:9000/search?saved=58fe2a49edd71f6c06d775f1&width=1247&rangetype=relative&fields=message%2Csource&relative=300&q=")


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
