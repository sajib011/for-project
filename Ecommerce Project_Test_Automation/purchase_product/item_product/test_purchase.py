from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

# open webbrowser

class login_web():
    def w_login(self):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://demo.nopcommerce.com/')
        driver.maximize_window()

        # login:
        driver.find_element(By.LINK_TEXT,'Log in').click()
        time.sleep(3)
        driver.find_element(By.ID,'Email').send_keys("sahasajib377@gmail.com")
        driver.find_element(By.ID,'Password').send_keys("sajib__Nob@110")
        driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button').click()
        time.sleep(5)

#         mouse ActionChains:
        computer=driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/a')
        desktop=driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[1]/a')
        actions=ActionChains(driver)
        actions.move_to_element(computer).move_to_element(desktop).click().perform()
        time.sleep(3)

#         select one item for purchase
        item1=driver.find_element(By.LINK_TEXT,'Build your own computer')
        item1.click()
        time.sleep(5)

#         dropdown:
        dropdown=driver.find_element(By.ID,'product_attribute_1')
        dropdown_values=Select(dropdown)
        dropdown_values.select_by_visible_text('2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00]')
        time.sleep(5)

        dropdown1=driver.find_element(By.ID,'product_attribute_2')
        dropdown_values1=Select(dropdown1)
        dropdown_values1.select_by_value('4')
        time.sleep(5)

#       radio :
        driver.find_element(By.ID,'product_attribute_3_6').click()
        time.sleep(5)

        driver.find_element(By.ID, 'product_attribute_4_9').click()
        time.sleep(5)

        driver.find_element(By.ID, 'product_attribute_5_12').click()
        time.sleep(5)

        quantity=driver.find_element(By.ID,'product_enteredQuantity_1')
        quantity.clear()
        quantity.send_keys('3')
        time.sleep(5)

#         button
        driver.find_element(By.XPATH,'//*[@id="add-to-cart-button-1"]').click()
        time.sleep(5)

#         add review
        driver.find_element(By.LINK_TEXT,'Add your review').click()
        time.sleep(5)

#         check review title & box is enable or disable
        title = driver.find_element(By.ID,'AddProductReview_Title')
        title_display_sate=title.is_enabled()
        print(title_display_sate)

        review_test=driver.find_element(By.ID,'AddProductReview_ReviewText')
        review_test_sate=review_test.is_enabled()
        print(review_test_sate)

        driver.find_element(By.XPATH,'//*[@id="topcartlink"]/a/span[1]').click()
        time.sleep(15)


obj=login_web()
obj.w_login()