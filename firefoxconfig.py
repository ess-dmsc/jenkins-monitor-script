
from selenium import webdriver

def set_options(x, y, w, h):
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
    return driver
