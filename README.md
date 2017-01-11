The following lines are run when the window manager has started up:

```
@git -C /home/pi/raspberry-pi-script/ pull
@bash /home/pi/raspberry-pi-script/start_script.sh
```

These lines should be located in the file:

```
/home/pi/.config/lxsession/LXDE/config
```

Note that the (storage) memory on the PI is currently *VERY* limited. You should probably only set another web site address and nothing else.