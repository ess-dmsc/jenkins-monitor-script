# jenkins-monitor-script

## Installation instructions

1. Download a version of Raspian from [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/) and put it on a microSD card. The version of 2017-08-16 was used for this guide.
2. Move the files ```ssh``` and ```wpa_supplicant.conf``` from the ```pi_boot```directory of this repository into the ```boot``` partition.
3. Edit the ```wpa_supplicant.conf``` file so that the pi connects to your network.
4. Log on to the pi using username **pi** and password **raspian**.
5. Install additional software: ```sudo apt-get install lxde-core xserver-xorg xinit firefox-esr git python3-pip```.
6. Make sure that lxde auto logins with user name pi and that the task bar hides automatically.
6. Install selenium: ```sudo pip3 install selenium```.
7. Download the geckodriver [here](https://github.com/mozilla/geckodriver/releases).
8. Make the binary executable: ```chmod +x geckodriver``` and move it to some appropriate location: ```sudo mv geckodriver /usr/local/bin/```
6. Clone this repository onto the pi: ```git clone https://github.com/ess-dmsc/jenkins-monitor-script.git```.
7. Copy and paste the following two lines into ```/home/pi/.config/lxsession/LXDE/autostart```: ```@git -C /home/pi/jenkins-monitor-script/ pull```and ```@bash /home/pi/jenkins-monitor-script/start_script.sh```

If you have a problem, the log file for these commands can be found here:

```
/home/pi/.cache/lxsession/LXDE/run.log
```
