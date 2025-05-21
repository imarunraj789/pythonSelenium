from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_Confirmation:

    def __init__(self,driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, "button[class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "input[type='submit']")
        self.success_message = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self,countryName):

        self.driver.find_element(*self.country_input).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        successText = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in successText

