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
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpended = driver.window_handles
driver.switch_to.window(windowsOpended[1])
entireText = driver.find_element(By.CSS_SELECTOR,".im-para.red").text
expectedText = entireText.split("at")
expectedEmailText = expectedText[1].split("with")
email = expectedEmailText[0].lstrip().rstrip()
driver.close()
driver.switch_to.window(windowsOpended[0])
wait = WebDriverWait(driver,10)
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.ID,"signInBtn").click()
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)