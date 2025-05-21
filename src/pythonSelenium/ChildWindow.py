import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service_obj = Service("E:/PythonSeleniumAutomation/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpended = driver.window_handles
driver.switch_to.window(windowsOpended[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(windowsOpended[0])

assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text