from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import getpass
import time

# Github credentials
username = input('username or emeil: ')
password = getpass.getpass(prompt='password:  ')

# initialize the Chrome driver
print("loading driver")
service = Service("/snap/bin/chromium.chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
print("driver ok ")

# head to github login page
driver.get("https://github.com/login")
print("github page loaded")

# find username/email field and send the username itself to the input field
driver.find_element_by_id("login_field").send_keys(username)
# find password input field and insert password as well
driver.find_element_by_id("password").send_keys(password)
# click login button
driver.find_element_by_name("commit").click()

time.sleep(5)
# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

# get the errors (if there are)
errors = driver.find_elements_by_class_name("flash-error")
# print the errors optionally
for e in errors:
     print(e.text)
error_message = "Incorrect username or password."
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

# close the driver
driver.close()
