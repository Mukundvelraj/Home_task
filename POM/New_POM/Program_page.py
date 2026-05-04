from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators_run1 import Locators_page
import time

class Enter_program:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)
    
    def open_pg(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        print(f"{url} Opened successfully")
    
    def verify(self):
        assert "online-compiler" in self.driver.current_url, "URL is wrong"
        print("URL verified successfully")

    def program(self, script):
        self.wait.until(lambda d: d.execute_script(
            "return typeof ace !== 'undefined' && document.querySelector('.ace_editor') !== null;"
        ))

        self.driver.execute_script("""
        var ace_editor = ace.edit(document.querySelector('.ace_editor'));
        ace_editor.setValue(arguments[0], -1);
        """, script)

        print("Script entered successfully")
        time.sleep(3)

    def run_prog(self):
        time.sleep(2)
        self.wait.until(
            EC.element_to_be_clickable(Locators_page.run_bt)
        ).click()
        print("Run button clicked")