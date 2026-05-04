from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://xamsor.com/blog/find-pages-linking-to-a-page/")
driver.maximize_window()
print(f"The Page Opened Successfully")
links = driver.find_elements(By.TAG_NAME,"a")
print(f"The total no of links", len(links))
img = driver.find_element(By.XPATH,"(//nav[contains(@id,'navbar')]//img[contains(@src,'/static/img/xamsor-logo.png')])")
assert img.is_displayed(),f"The Photo is not displayed"
print(f"Scanned successfully")
driver.quit()
