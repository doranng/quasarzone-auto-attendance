import json
from selenium.webdriver.common.by import By
from urllib import parse

URL_ZONE = 'https://quasarzone.com/ajax/user/attendanceInsert'
URL_PLAY = 'https://quasarplay.com/ajax/user/attendanceInsert'


def check_core(driver, url, user_data):
    driver.get(url)
    driver.find_element(by=By.NAME, value="login_id").send_keys(user_data['id'])
    driver.find_element(by=By.NAME, value="password").send_keys(user_data['pw'])
    driver.find_element(by=By.CLASS_NAME, value="login-bt").click()

    result = json.loads(driver.find_element(by=By.TAG_NAME, value="body").text)
    result['netloc'] = parse.urlparse(url).netloc

    return result


def check(driver, user_data):
    results = [check_core(driver, URL_ZONE, user_data), check_core(driver, URL_PLAY, user_data)]
    return results
