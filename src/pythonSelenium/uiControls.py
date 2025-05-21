from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:/PythonSeleniumAutomation/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButtons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
print(len(radioButtons))
radioButtons[2].click()
radioButtons[2].is_selected()

assert  driver.find_element(By.ID,"displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()
assert  not driver.find_element(By.ID,"displayed-text").is_displayed()