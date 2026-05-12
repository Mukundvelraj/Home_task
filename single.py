from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:
    __driver = None

    @staticmethod
    def get_driver():
        if DriverManager.__driver is None:
            service = Service(ChromeDriverManager().install())
            DriverManager.__driver = webdriver.Chrome(service=service)
        return DriverManager.__driver


d1 = DriverManager.get_driver()
d2 =  DriverManager.get_driver()

print(d1 is d2)

