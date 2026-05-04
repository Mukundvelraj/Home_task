from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.hotstar.com"
driver.get(url)
time.sleep(3)
print(f"Successfully opened the browser Jio")
driver.maximize_window()
assert driver.title == "JioHotstar - Watch TV Shows, Movies, Specials, Live Cricket & Football",f"Assertion Failed"
print("Assertion completed")
time.sleep(2)
driver.quit()