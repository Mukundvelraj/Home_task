from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")
driver.maximize_window()
print("Driver opened successfully")
time.sleep(5)
yt_link = driver.find_element(By.XPATH,"//yt-icon[@id='logo-icon']")
yt_link.click()
page_title = driver.title
assert page_title == "YouTube",f"The page is not same"
print("Successfully covered the page")

