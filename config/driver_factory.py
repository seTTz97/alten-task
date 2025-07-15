from selenium import webdriver

def get_driver(browser="chrome"):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        options.add_argument("--headless")
        #TODO: add more config needed
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        return driver
    elif browser == "firefox":
        return webdriver.Firefox()
    else:
        raise Exception(f"Browser {browser} is not supported.")
