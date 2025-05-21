import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
service_obj = Service("E:/PythonSeleniumAutomation/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("JavaScriptExecutionScreenshot.png")