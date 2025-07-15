from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

DEFAULT_TIMEOUT = 10

def wait_element_then_click(
        by: By,
        locator: str,
        driver: webdriver,
        timeout: int = DEFAULT_TIMEOUT
):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.visibility_of_element_located((by, locator)))
    element.click()

def wait_until_element_is_visible(
        by: By,
        locator: str,
        driver: webdriver,
        timeout: int = DEFAULT_TIMEOUT
):
    wait = WebDriverWait(driver, timeout)
    #TODO: add try catch
    element = wait.until(EC.visibility_of_element_located((by, locator)))
    return element