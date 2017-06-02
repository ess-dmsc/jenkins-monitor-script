#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os, time, sys, getpass

if len(sys.argv) != 2:
   print("usage: wall_display.py username")
   sys.exit(0)

user=sys.argv[1]
print("please enter password for user " + user)
paswd=getpass.getpass("> ")

#os.environ["DISPLAY"] = ":10.0"
os.environ["DISPLAY"] = ":0.0"

drivers = []

def login(driver, nuser, npass, tuser, tpass):
   try:
      username = driver.find_element_by_name(nuser)
      password = driver.find_element_by_name(npass)
   except Exception:
      print("find_element_by_name failed")
      driver.close()
      sys.exit()

   username.send_keys(Keys.CLEAR)
   username.send_keys(tuser)

   password.send_keys(Keys.CLEAR)
   password.send_keys(tpass)
   password.send_keys(Keys.RETURN)


def launch(url, x, y, ref, nusr, tusr, npwd, tpwd):
   global drivers
   profile = webdriver.FirefoxProfile()
   ext_path = "ff_ext/"
   profile.add_extension(extension=ext_path + "hide_tabbar-2.1.0-fx.xpi")
   profile.add_extension(extension=ext_path + "hidenavbar.xpi")
   profile.set_preference("extensions.hidtb.auto_hide", True)
   profile.set_preference("extensions.hidtb.auto_hide_one_tab", True)
   profile.set_preference("hidenavbar.autohide", True)
   profile.set_preference("hidenavbar.hideonstart", 1)

   driver = webdriver.Firefox(profile, timeout = 100)
   driver.set_window_position(x, y)
   driver.set_window_size(2000, 1000)
   try:
      driver.get(url)
   except Exception:
      driver.close()
      sys.exit()

   drivers.append([driver, url, ref])
   if nusr != "":
      login(driver, nusr, npwd, tusr, tpwd)

launch("http://status.esss.se",     2000,    0, 1, "", "", "", "")
launch("http://jenkins.esss.dk/dm", 4000,    0, 1, "", "", "", "")
launch("http://172.17.5.35:3000/dashboard/db/detector-activity",   2000, 1000, 0, "username", "admin", "password", "admin")
launch("https://jira.esss.lu.se/secure/RapidBoard.jspa?rapidView=167&projectKey=DM&view=reporting&chart=cumulativeFlowDiagram&swimlane=287&swimlane=288&column=674&column=734&column=675&column=678&column=677&column=676" , 4000, 1000, 1, "UserName", user, "Password", paswd)

try:
   while True:
      time.sleep(10)
      for x in drivers:
         drv = x[0]
         url = x[1]
         ref = x[2]
         if ref:
            drv.get(url)
except Exception:
   for x in drivers:
      x[0].close()
