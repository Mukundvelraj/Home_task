from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = None
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/")
    print(f"Opened the page successfully")
    element = driver.find_element(By.XPATH,"(//a[contains(text(),'Frame')])[1]")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    verify= driver.find_element(By.XPATH,"//h3[contains(text(),'Frames')]")
    assert verify.is_displayed,"Incorrect page"
    print("Moved to Frame page")
    iframe = driver.find_element(By.XPATH,"//a[contains(text(),'iFrame')]")
    iframe.click()
    print("Clicked the IFRAME")
    driver.find_element(By.XPATH,"//p/span[contains(text(),'TinyMCE')]/ancestor::div//button").click()
    driver.switch_to.frame('mce_0_ifr')
    print("Switched to Iframe")
    print(driver.find_element(By.XPATH,"//p[contains(text(),'')]").text)
    driver.switch_to.default_content
    print("Back to default")
except Exception as e:
    driver.save_screenshot("Error.png")
    print(f"The Error occured {e}")
    raise
finally:
    print("FInally Complted the program")
    driver.quit()