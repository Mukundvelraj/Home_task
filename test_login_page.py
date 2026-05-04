from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
print(f"Page opened successfully")
page_title = driver.title
driver.maximize_window()
assert page_title == "Swag Labs",f"Wrong page"
print(f"The Page sucessfully scanned")
username = driver.find_element(By.XPATH,"//input[@id = 'user-name']")
username.send_keys("standard_user")
time.sleep(3)
password = driver.find_element(By.XPATH,"//input[@id = 'password']")
password.send_keys("secret_sauce")
time.sleep(3)
login_bt = driver.find_element(By.XPATH,"//input[@id='login-button']")
login_bt.click()
assert "inventory.html" in driver.current_url, f"Page is wrong"
print(f"Successfully scanned the page")