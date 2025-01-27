import json
from selenium.webdriver.common.by import By
from urllib import parse
from autocheck.message.MessagePool import MessagePool

LOGIN_ID = "login_id"
PASSWORD = "password"
BODY = "body"
NETLOC = "netloc"
URL_ZONE = "https://quasarzone.com/ajax/user/attendanceInsert"
URL_PLAY = "https://quasarplay.com/ajax/user/attendanceInsert"
BTN_CLASS_NAME_ZONE = "btn-login"
BTN_CLASS_NAME_PLAY = "login-bt"


class Checker:
    def check(self, driver, user_data):
        MessagePool().add_message(self.__check_core(driver, URL_ZONE, user_data, BTN_CLASS_NAME_ZONE))
        MessagePool().add_message(self.__check_core(driver, URL_PLAY, user_data, BTN_CLASS_NAME_PLAY))

    @staticmethod
    def __check_core(driver, url, user, btn_class_name):
        driver.get(url)
        driver.find_element(by=By.NAME, value=LOGIN_ID).send_keys(user.id)
        driver.find_element(by=By.NAME, value=PASSWORD).send_keys(user.pw)
        driver.find_element(by=By.CLASS_NAME, value=btn_class_name).click()

        result = json.loads(driver.find_element(by=By.TAG_NAME, value=BODY).text)
        result[NETLOC] = parse.urlparse(url).netloc

        return result
