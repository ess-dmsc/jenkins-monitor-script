
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def set_options(url, x, y, w, h):
    chrome_options = Options()
    opt_winpos = "--window-position=" + str(x) + "," + str(y)
    opt_winsize = "--window-size=" + str(w) + "," + str(h)
    opt_noinfobar = "--disable-infobars"
    opt_app = "--app=" + url
    chrome_options.add_argument(opt_winpos)
    chrome_options.add_argument(opt_winsize)
    chrome_options.add_argument(opt_noinfobar)
    chrome_options.add_argument(opt_app)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver
