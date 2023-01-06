from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time
from selenium.webdriver.common.by import By

class registerecommerce():
    def test_register(self):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://demo.nopcommerce.com/')
        driver.find_element(By.LINK_TEXT,'Register').click()
        time.sleep(5)
        # select redio gender

        gender=driver.find_element(By.ID,'gender-male')
        gender.click()
        time.sleep(5)

        first_name = driver.find_element(By.ID,'FirstName')
        first_name.send_keys("sajib")

        last_name= driver.find_element(By.ID,'LastName')
        last_name.send_keys("saha")
        time.sleep(5)


#         dropdown for dob
#         day
        day=driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[1]')
        day_values=Select(day)
        day_values.select_by_visible_text('1')
        time.sleep(2)

#         month
        month = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[2]')
        month_values = Select(month)
        month_values.select_by_visible_text('January')
        time.sleep(2)

#         year
        year = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[3]')
        year_values = Select(year)
        year_values.select_by_visible_text('1998')
        time.sleep(2)

#         email
        driver.find_element(By.ID,'Email').send_keys("sahasajib377@gmail.com")
        time.sleep(2)

#         company name
        driver.find_element(By.ID,'Company').send_keys("RK yarn Trading")
        time.sleep(2)

#         password create

        driver.find_element(By.ID,'Password').send_keys("sajib__Nob@110")
        driver.find_element(By.ID,'ConfirmPassword').send_keys("sajib__Nob@110")
        time.sleep(2)

#         Buttom
        driver.find_element(By.XPATH,'//*[@id="register-button"]').click()
        time.sleep(10)


obj = registerecommerce()
obj.test_register()



