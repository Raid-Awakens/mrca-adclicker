from seleniumwire import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

mod_url = "https://modrinth.com/mod/chaos-awakens" #mod
proxy = "user:pass@ip:port" #proxy

options = {
'proxy': {
    'http': 'http://'+proxy,
    'https': 'https://'+proxy,
    'no_proxy': 'localhost,127.0.0.1,dev_server:8080'
    }
}
c = Options()
c.add_argument("--headless")

count = 0
while (count < 100):   
    count = count + 1
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    driver = webdriver.Firefox(seleniumwire_options=options, firefox_profile=firefox_profile, options=c)
    driver.get(mod_url)
    driver.find_element(By.CLASS_NAME,"ea-text").click()
    time.sleep(2)
    driver.quit()
    print("Clicked on Ad")