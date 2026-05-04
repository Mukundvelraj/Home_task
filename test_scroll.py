from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = None
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    print(f"Scrolled to bottom")
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    print(f"Scrolled to Top")
    driver.execute_script("window.scrollBy(0,600)")
    time.sleep(3)
    print(f"Scrolled to Frame")
    element_frame = driver.find_element(By.XPATH,"(//a[contains(text(),'Frame')])[1]")
    driver.execute_script("arguments[0].scrollIntoView();",element_frame)
    element_frame.click()
    verify = driver.find_element(By.XPATH,"//h3[contains(text(),'Frames')]")
    assert verify.is_displayed(), "Directed to wrong page"
    print(f"Directed to right page")
except Exception as e:
    print(f"The Error raised as {e}")
    raise
finally:
    driver.quit()