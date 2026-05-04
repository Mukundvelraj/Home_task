from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = None
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    username = driver.find_element(By.XPATH,"//input[@id='user-name']")
    username.send_keys("standard_user")
    username.send_keys(Keys.TAB)

    password=driver.switch_to.active_element
    password.send_keys("secret_sauce")
    
    
    button = driver.find_element(By.XPATH,"//input[@id='login-button']")
    password.send_keys(Keys.ENTER)
    time.sleep(5)
except Exception as e:
    print(f"The error as {e}")
    raise
    
