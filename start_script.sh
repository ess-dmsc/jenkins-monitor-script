#!/usr/bin/env bash

#chromium-browser --incognito --allow-running-insecure-content --kiosk http://jenkins.esss.dk/dm/view/Monitor%20view/

#DISPLAY=:0.0 firefox -private -url https://jenkins.esss.dk/dm/view/Monitor%20view/

rm geckodriver.log
python /home/pi/jenkins-monitor-script/browser_ctrl.py
