import json
from selenium.webdriver.common.by import By
from urllib import parse
from src.autocheck.message.MessagePool import MessagePool


class Checker:
    def __init__(self):
        self.__url_zone = 'https://quasarzone.com/ajax/user/attendanceInsert'
        self.__url_play = 'https://quasarplay.com/ajax/user/attendanceInsert'

    def check(self, driver, user_data):
        MessagePool().add_message(self.__check_core(driver, self.__url_zone, user_data))
        MessagePool().add_message(self.__check_core(driver, self.__url_play, user_data))

    @staticmethod
    def __check_core(driver, url, user):
        driver.get(url)
        driver.find_element(by=By.NAME, value="login_id").send_keys(user.id)
        driver.find_element(by=By.NAME, value="password").send_keys(user.pw)
        driver.find_element(by=By.CLASS_NAME, value="login-bt").click()

        result = json.loads(driver.find_element(by=By.TAG_NAME, value="body").text)
        result['netloc'] = parse.urlparse(url).netloc

        return result
