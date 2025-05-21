from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage
from utils.browserUtils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.NAME, "password")
        self.signInButton = (By.ID, "signInBtn")



    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signInButton).click()
        shopPage = ShopPage(self.driver)
        return shopPage