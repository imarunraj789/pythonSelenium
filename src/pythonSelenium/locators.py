import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("E:/PythonSeleniumAutomation/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("imarunraj@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("TendlyWall$01")
driver.find_element(By.ID,"exampleCheck1").click()

# XPATH //tagname[@attribute='value']  //input[@type='submit']
# CSS  tagname[attribute='value']   input[name='name'], #id, .classname

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Arun")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

# Static Drop down
dropDown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropDown.select_by_visible_text("Female")

driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("HelloAgain")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
time.sleep(4)