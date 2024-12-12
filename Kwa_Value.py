from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time



# Desired capabilities using UiAutomator2Options
options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = 'Google Pixel'
options.app_package = 'com.code2lead.kwad'
options.app_activity = 'com.code2lead.kwad.MainActivity'
options.automation_name = 'UiAutomator2'

# Initialize the Appium driver
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
print("Berhasil Start !")



def Enter_value():
    try:
        # Find the element using its ID
        click1 = driver.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/EnterValue')
        click1.click()
        value = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et1"]')
        value.send_keys("HALLO")
        click3 = driver.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Btn1')
        click3.click()
        print("Berhasil isi data !")

    except Exception():
        print("Gagal Isi data !")


    # Add a delay to observe the interaction (optional)
time.sleep(3)
Enter_value()
