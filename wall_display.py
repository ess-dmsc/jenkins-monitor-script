#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import os           # os.environ
import time         # time.sleep
import sys          # sys.argv, sys.exit
import getpass      # getpass.getpass

class wallDisplay(object):
    def __init__(self):
        self.groups = {}

    def login(self, driver, nuser, npass, tuser, tpass):
        try:
            username = driver.find_element_by_name(nuser)
            password = driver.find_element_by_name(npass)
        except Exception:
            print("find_element_by_name failed")
            return

        username.send_keys(Keys.CLEAR)
        username.send_keys(tuser)
        password.send_keys(Keys.CLEAR)
        password.send_keys(tpass)
        password.send_keys(Keys.RETURN)

    def register(self, group, url, refreshNeeded, nusr, tusr, npwd, tpwd):
        if not group in self.groups:
            self.groups[group] = []
        self.groups[group].append([url, refreshNeeded, nusr, tusr, npwd, tpwd])

    # @todo currently only works for a single group and up to four windows
    def pos2xy(self, pos, n):
        print("pos %d, n %d, x %d\n" % (pos, n, pos%(n/2)))

        if pos == 0:
            return [2000,    0, 2000, 1000]
        elif pos == 1:
            return [4000,    0, 2000, 1000]
        elif pos == 2:
            return [2000, 1075, 2000, 1000]
        elif pos == 3:
            return [4000, 1075, 2000, 1000]

    def launch(self):
        for g in self.groups:
            cGroup = self.groups[g]
            for pos, view in enumerate(cGroup):
                x, y, w, h = self.pos2xy(pos, len(cGroup))
                drv = self.weblaunch(x, y, w, h, *view)
                view.append(drv)

    def weblaunch(self, x, y, w, h, url, refreshNeeded, nusr, tusr, npwd, tpwd):
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
       driver.set_window_size(w, h)
       try:
          driver.get(url)
       except Exception:
          driver.close()

       if nusr != "":
          self.login(driver, nusr, npwd, tusr, tpwd)
       return driver

    def updateloop(self, updint):
        try:
            while True:
                time.sleep(updint)
                for g in self.groups:
                    cGroup = self.groups[g]
                    for url, refreshNeeded, nusr, tusr, npwd, tpwd, drv in cGroup:
                        if refreshNeeded:
                            drv.get(url)
        except Exception:
            self.exit()

    def exit(self):
        for x in self.drivers:
           x[0].close(0)
        sys.exit(0)

# ------------------------------------------------------------------------------------------------
def main():
    if len(sys.argv) != 2:
       print("usage: wall_display.py username")
       sys.exit(0)

    walldisp = wallDisplay()

    user=sys.argv[1]
    print("please enter password for user " + user)
    paswd=getpass.getpass("> ")

    #os.environ["DISPLAY"] = ":10.0"
    os.environ["DISPLAY"] = ":0.0"

    walldisp.register(0, "http://status.esss.se",      1, "", "", "", "")
    walldisp.register(0, "http://jenkins.esss.dk/dm",  1, "", "", "", "")
    walldisp.register(0, "http://127.0.0.1:3000",      0, "username", "admin", "password", "admin")
    walldisp.register(0, "https://jira.esss.lu.se/secure/RapidBoard.jspa?rapidView=167&projectKey=DM&view=reporting&chart=cumulativeFlowDiagram&swimlane=287&swimlane=288&column=674&column=734&column=675&column=678&column=677&column=676" , 1, "UserName", user, "Password", paswd)
    #walldisp.register(1, "http://status.esss.se",      1, "", "", "", "")

    walldisp.launch()
    #walldisp.updateloop(3)

if __name__ == "__main__":
    main()
