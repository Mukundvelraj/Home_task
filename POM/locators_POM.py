from selenium.webdriver.common.by import By
class Locators:
    user_name = (By.XPATH,"//input[@id='user-name']")
    pass_word = (By.XPATH,"//input[@id = 'password']")
    lgt_bt = (By.XPATH,"//input[@id='login-button']")
    alert_close = (By.XPATH,"//button[@class='error-button']")
    verification = (By.XPATH,"//span[contains(text(),'Products')]")
    bug_bt = (By.ID, "react-burger-menu-btn")
    log_out = (By.XPATH,"//a[@id = 'logout_sidebar_link']")


