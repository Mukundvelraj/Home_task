from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver,10)
    driver.get("https://www.saucedemo.com/")
    username = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='user-name']"))).send_keys("standard_user")
    password = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'password']"))).send_keys("secret_sauce")
    lgt_button = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login-button']"))).click()
except Exception as e:
    print(f"error occured {e}")
    raise
    