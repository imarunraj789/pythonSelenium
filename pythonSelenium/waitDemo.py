import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:/PythonSeleniumAutomation/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)

productResults = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(productResults)

assert count > 0

for productResult in productResults:
    productResult.find_element(By.XPATH,"div/button").click()
# time.sleep(3)

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# time.sleep(6)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
