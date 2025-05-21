import time

from selenium import webdriver
from selenium.webdriver.ie.service import Service

# service_obj = Service("E:/PythonSeleniumAutomation/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
time.sleep(2)