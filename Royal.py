from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

import time

options = UiAutomator2Options()
options.automation_name = 'UiAutomator2'
options.platform_name = 'Android'
options.device_name = 'MEmu'
options.app_package = 'com.huoys.royaldomino'
options.app_activity = 'com.huoys.activity.MainActivity'
options.no_reset = True

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
print("Berhasil Start !")

time.sleep(20)

klik_pengunjung = {"x": 1360, "y": 600}



def log_in():
    try:
        driver.tap([(klik_pengunjung["x"], [klik_pengunjung["y"]])])
        print("berhasil log in !")

    except Exception:
        print("gagal !")
        pass

log_in()