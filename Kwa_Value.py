from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Desired capabilities using UiAutomator2Options
options = UiAutomator2Options()
options.platformName = 'Android'
options.deviceName = 'Google Pixel'
options.appPackage = 'com.code2lead.kwad'
options.appActivity = 'com.code2lead.kwad.MainActivity'

# Initialize the Appium driver
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# Find the element using its ID
click = driver.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/EnterValue')
click.click()

# Add a delay to observe the interaction (optional)
time.sleep(3)

# Quit the driver
driver.quit()
