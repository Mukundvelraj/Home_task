from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from Program_page import Enter_program
from locators_run1 import Locators_page



def test_script():
    driver = None

    prg_data = """
    def even_odd(n):
        if n % 2 == 0:
            return "Even"
        return "Odd"

    print(even_odd(20))
    print(even_odd(17))
    """

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        ps = Enter_program(driver)
        ps.open_pg("https://www.programiz.com/python-programming/online-compiler/")
        ps.verify()
        ps.program(prg_data)
        ps.run_prog()

    except Exception as e:
        print(f"The Exception occured {e}")
        raise
    finally:
        print("Successfully completed the Script")
        driver.quit()
