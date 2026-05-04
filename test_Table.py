from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time
driver = None
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://money.rediff.com/gainers/bsc/daily/groupa")
    driver.maximize_window()
    print("Opened the Browser successfully")
    driver.execute_script("window.scrollTo(0,700);")
    data_text = driver.find_element(By.XPATH,"//a[contains(text(),'RBL')]").text
    rows = driver.find_elements(By.TAG_NAME,"tr")
    print(f"The tot num of rows - {len(rows)}")
    cells = driver.find_elements(By.TAG_NAME,'td')
    found = False
    for row in rows:
        for cell in cells:
            if cell.text == data_text:
                print(f"The Data Found")
                found = True
                break
            if found == True:
                break
    if not found:
        print("NOT FOUND")
except Exception as e:
    print(f"The error as {e}")
    raise
finally:
    print("Press enter")
    input()



