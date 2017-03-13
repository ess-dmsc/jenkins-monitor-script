# jenkins-monitor-script

If you want the disk image used to run the monitor, get in contact with me.

The following lines are run when the window manager has started up:

```
@git -C /home/pi/jenkins-monitor-script/ pull
@bash /home/pi/jenkins-monitor-script/start_script.sh
```

These lines should be located in the file:

```
/home/pi/.config/lxsession/LXDE/autostart
```

If you have a problem, the log file for these commands can be found here:

```
/home/pi/.cache/lxsession/LXDE/run.log
```

For clean installations, it is best to install selenium using `pip`:
```
sudo pip install selenium
```

You will also need to download geckodriver from [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases). It appears that version of 0.15 geckodriver does not support the `set_page_load_timeout()` command of selenium.
