import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utils.common_utils import wait_until_element_is_visible

URL = "https://www.saucedemo.com/"


@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.mark.parametrize(
        "username,password",
        [
            ("standard_user", "secret_sauce"),
            ("problem_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            ("error_user", "secret_sauce"),
            ("visual_user", "secret_sauce"),
        ]
    )
    def test_valid_login(self, username, password):
        login_page = LoginPage(self.driver)
        self.driver.get(URL)

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        #TODO: enhance validation
        assert "inventory.html" in self.driver.current_url.lower()

    @pytest.mark.parametrize(
        "username,password",
        [
            ("standard_user1", "secret_sauce"),
            ("locked_out_user", "secret_sauce11"),
            ("problem_user21", "secret_sauce"),
            ("aa", "secret_sauce"),
        ]
    )
    def test_invalid_login(self, username, password):
        login_page = LoginPage(self.driver)
        self.driver.get(URL)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        error_msg = wait_until_element_is_visible(
            by=By.XPATH,
            locator="//*[@data-test='error']",
            driver=self.driver
        )
        assert "username and password do not match any user in this service" in error_msg.text.lower()

    #Test with usage of pytest hooks
    def test_valid_login_with_hooks(self, username, password):
        login_page = LoginPage(self.driver)
        self.driver.get(URL)

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        assert "inventory.html" in self.driver.current_url.lower()
