import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


BrowserSortedVeggiesList = []
service_obj = Service("E:/PythonSeleniumAutomation/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#Click on Sorting on the column
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

#Collect the Name of the veggies and store it in a list - BrowserSortedVeggiesList
AllVeggies = driver.find_elements(By.XPATH,"//tr/td[1]")
for veggie in AllVeggies:
    BrowserSortedVeggiesList.append(veggie.text)

#Copy the List and store it in a different list before sorting
OriginalBrowserSortedList = BrowserSortedVeggiesList.copy()

#Sort Original List
BrowserSortedVeggiesList.sort()

#Compare the Sorted Original List and Copied List
assert BrowserSortedVeggiesList == OriginalBrowserSortedList