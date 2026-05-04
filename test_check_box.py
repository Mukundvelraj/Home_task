from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = None
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/")
    check_box = driver.find_element(By.XPATH,"//a[contains(text(),'Checkboxes')]")
    check_box.click()
    verification = driver.find_element(By.XPATH,"//div[@id='content']//h3")
    assert verification.is_displayed(),f"The Page directed is wrong"
    print(f"Successfully directed")
    check_box_2 = driver.find_element(By.XPATH,"(//input[normalize-space(contains(text(),'checkbox 2'))])[2]")
    if not check_box_2.is_selected():
        check_box_2.click()
        print("Checkbox selected")
    else:
        print("Already selected")
    time.sleep(5)
except Exception as e:
    print(f"The Issue for this program {e}")
    raise

finally:
    if driver:
        driver.quit()