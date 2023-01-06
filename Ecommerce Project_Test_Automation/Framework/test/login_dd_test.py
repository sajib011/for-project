import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from Framework.pages.login_page import LoginPage
# from Framework.utils import excel_utils

# Read data and implementing in test

class LoginTest(unittest.TestCase):

    def test_valid_login(self):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get('https://demo.nopcommerce.com/login?returnUrl=%2F')
        time.sleep(3)

#         Excel Implement
#         file = "D:\\software testing class\\Ecommerce Project\\Framework\\data\\login_data.xlsx"
#         sheet = "Sheet1"
#
#         number_of_rows = excel_utils.get_row_count(file, sheet)
#
#         for r in range(2, number_of_rows + 1):
#             email_data = excel_utils.read_data(file, sheet, r, 1)
#             password_data= excel_utils.read_data(file, sheet, r, 2)
#             lp = LoginPage(driver)
#             lp.login_ecommerce(email_data,password_data)
#         driver.close()

        lp=LoginPage(driver)
        lp.login_ecommerce("sahasajib377@gmail.com", "sajib__Nob@110")
        driver.close()

    def test_invalid_login(self):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get('https://demo.nopcommerce.com/login?returnUrl=%2F')
        time.sleep(3)
        lp = LoginPage(driver)
        lp.login_ecommerce("sahasajib400@gmail.com", "saju@saju")
        driver.close()

