# Note: you need chromedriver, download that from the site
# https://sites.google.com/chromium.org/driver/downloads
# and add that chromedriver to your environment path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


print("Hello World")
USERNAME="Your Stupid USERNAME"
PASSWORD="Your Stupid PASSWORD*"
driver = webdriver.Chrome()
WEBSITE=f'https://172.22.2.6/connect/PortalMain'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
driver.get(WEBSITE)
print(driver.title)


"""
id="LoginUserPassword_auth_username"
id="LoginUserPassword_auth_password"
id="UserCheck_Login_Button_span"

"""


field1 = driver.find_element(By.ID ,"LoginUserPassword_auth_username")
field2 = driver.find_element(By.ID, "LoginUserPassword_auth_password")
form = driver.find_element(By.ID ,"UserCheck_Login_Button_span")
field1.send_keys(USERNAME)
field2.send_keys(PASSWORD)
form.click()
print("COMPLETE")


time.sleep(10)
driver.quit()