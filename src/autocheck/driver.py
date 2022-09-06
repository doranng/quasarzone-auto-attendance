import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def create_web_drive():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = uc.Chrome(use_subprocess=True, options=options)
    WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    return driver
