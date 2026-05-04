from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time
driver = None
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/")
    driver.maximize_window()
    navi = driver.find_element(By.XPATH,"//a[contains(text(),'Dropdown')]")
    driver.execute_script("arguments[0].scrollIntoView();", navi)
    navi.click()
    print("Page navigated to Dropdown page")
    try:
        verify = driver.find_element(By.XPATH,"//h3[contains(text(),'Dropdown List')]")
        assert verify.is_displayed(), "Indirected to another page"
        print("Verified the dropdown page")
    except Exception as e:
        print(f"Error occurs : {e}")
        print(driver.save_screenshot("Error_img.png"))
        raise
    dp = driver.find_element(By.XPATH,"//h3[contains(text(),'Dropdown List')]//parent::div/select[@id='dropdown']")
    print("Dropdown is selected")
    select = Select(dp)
    select.select_by_index(1)
    print("Option 1 is selected")
    time.sleep(3)
    select.select_by_value("2")
    print("Option 2 is selected")
    time.sleep(2)
    select.select_by_visible_text("Option 1")
    print("Again Option 1 is selected")
    time.sleep(3)
    count = len(select.options)
    print(f"The Total length of the dropdown list is {count}")
    option_found = False

    for opt in select.options:
        if opt.text == "Option 2":
            option_found = True
            break

    if option_found:
        select.select_by_visible_text("Option 2")
        print("Option 2 is selected Again")
    else:
        print("Option 2 is not in the list")
except Exception as e:
    print(f"The Error occured : {e}")
    raise
finally:
    input("Enter any key to close the browser")
    driver.quit()