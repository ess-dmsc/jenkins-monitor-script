#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import os
import time
os.environ["DISPLAY"] = ":0.0"
profile = webdriver.FirefoxProfile()
ext_path = "/home/pi/jenkins-monitor-script/ff_ext/"
#ext_path = "/Users/jonasnilsson/FF_ext/"
profile.add_extension(extension=ext_path + "hide_tabbar-2.1.0-fx.xpi")
profile.add_extension(extension=ext_path + "hidenavbar.xpi")
profile.set_preference("extensions.hidtb.auto_hide", True)
profile.set_preference("extensions.hidtb.auto_hide_one_tab", True)
profile.set_preference("hidenavbar.autohide", True)
profile.set_preference("hidenavbar.hideonstart", 1)
driver = webdriver.Firefox(profile, timeout = 100)
driver.maximize_window()

list_of_sites = []
list_of_sites.append(["http://skytoground.org/upcoming_events/", 30])
list_of_sites.append(["https://jenkins.esss.dk/dm/view/Non-master%20broken%20builds%20monitor%20view/", 60])
list_of_sites.append(["https://ess-scandinavia.eu/sitecam/cam01/latest.jpg", 10])
#list_of_sites.append(["http://skytoground.org/score_card.html", 20])
list_of_sites.append(["https://jenkins.esss.dk/dm/view/Master%20monitor%20view/", 60])
list_of_sites.append(["https://ess-scandinavia.eu/sitecam/cam02/latest.jpg", 10])
list_of_sites.append(["http://skytoground.org/upcoming_events/", 30])
list_of_sites.append(["https://jenkins.esss.dk/dm/view/Non-master%20broken%20builds%20monitor%20view/", 60])
list_of_sites.append(["https://ess-scandinavia.eu/sitecam/cam03/latest.jpg", 10])
list_of_sites.append(["https://jenkins.esss.dk/dm/view/Master%20monitor%20view/", 60])
list_of_sites.append(["https://ess-scandinavia.eu/sitecam/cam04/latest.jpg", 10])

driver.set_page_load_timeout(15)
while (True):
    for site in list_of_sites:
        try:
            driver.get(site[0])
        except Exception:
            pass
        time.sleep(site[1])
    

