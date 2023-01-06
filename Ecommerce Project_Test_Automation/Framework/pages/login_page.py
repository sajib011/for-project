import time
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):
        self.driver = driver

    def login_ecommerce(self,email,password):
        email_field=self.driver.find_element(By.ID,"Email")
        password_field=self.driver.find_element(By.ID,"Password")
        login_button=self.driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/button")

        email_field.clear()
        email_field.send_keys(email)
        time.sleep(3)

        password_field.clear()
        password_field.send_keys(password)
        time.sleep(3)

        login_button.click()
        time.sleep(3)