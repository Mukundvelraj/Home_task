from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from locators_POM import Locators
import time

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout=10,poll_frequency=2)
    
    def uname(self,username):
        name = self.wait.until(EC.visibility_of_element_located(Locators.user_name))
        name.clear()
        name.send_keys(username)
    
    def pa_word(self,password):
        pass_use = self.wait.until(EC.visibility_of_element_located(Locators.pass_word))
        pass_use.clear()
        pass_use.send_keys(password)

    def error(self):
        alert_message = self.driver.find_elements(By.XPATH, '//h3[@data-test="error"]')
        return len(alert_message)
        time.sleep(2)

    def close_error(self):
        self.wait.until(EC.visibility_of_element_located(Locators.alert_close)).click()
        time.sleep(3)
    
    def log_button(self):
        self.wait.until(EC.visibility_of_element_located(Locators.lgt_bt)).click()
    
    def verify(self):
        product = self.wait.until(EC.visibility_of_element_located(Locators.verification))
        assert product.is_displayed(),"Page is incorrect"
        time.sleep(5)
    
    def click_buger(self):
        self.wait.until(EC.visibility_of_element_located(Locators.bug_bt)).click()
        time.sleep(2)

    def lg_out(self):
        self.wait.until(EC.visibility_of_element_located(Locators.log_out)).click()
        time.sleep(2)
    

        