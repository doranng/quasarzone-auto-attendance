import undetected_chromedriver as uc
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from autocheck.message.MessagePool import MessagePool


class WebDriver:
    @staticmethod
    def create():
        try:
            options = webdriver.ChromeOptions()
            # options.add_argument('--headless')
            driver = uc.Chrome(use_subprocess=True, options=options)
            WebDriverWait(driver, 10)
            driver.implicitly_wait(10)
            return driver
        except WebDriverException as e:
            MessagePool().add_message({'result': 'fail', 'netloc': 'quasarzone.com', 'msg': e.msg})
