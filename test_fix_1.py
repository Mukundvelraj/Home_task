import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_run(browser):
    driver = browser
    driver.maximize_window()
    wait = WebDriverWait(driver,timeout=10)
    username = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='user-name']")))
    username.clear()
    username.send_keys("standard_user")

    password = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'password']")))
    password.clear()
    password.send_keys("secret_sauce")

1