from selenium.webdriver.common.by import By
from utils.common_utils import wait_element_then_click

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        wait_element_then_click(by=By.ID, locator="login-button", driver=self.driver)
