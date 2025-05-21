import json
import os.path
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage
test_data_path = "../data/test_E2ETestFramework.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance

    loginPage = LoginPage(driver)
    print("Title is " + loginPage.getTitle())
    shopPage = loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])

    shopPage.add_product_to_cart(test_list_item["productName"])
    print("Title is " + shopPage.getTitle())
    checkout_confirmation = shopPage.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address(test_list_item["deliveryAddress"])
    checkout_confirmation.validate_order()