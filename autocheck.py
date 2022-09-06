"""
quasar-zone auto attendance check
v0.2.0
"""
import json
import logging
import undetected_chromedriver as uc
from cryptography.fernet import Fernet
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

fernet = Fernet(bytes(b'8bfv1k2-gZ74BDdUmT6T3kA66eZSJSbHr6YtPGgZ598='))

try:
    f = open('userinfo.txt', 'r')
    data = f.readlines()
    _id = data[0].strip()
    _pw = fernet.decrypt(bytes(data[1], 'utf-8')).decode()
except FileNotFoundError:
    _id = input("id:")
    _pw = getpass("pw:")
    f = open('userinfo.txt', 'w')
    data = "%s\n%s" % (_id, fernet.encrypt(_pw.encode()).decode('utf-8'))
    f.write(data)
f.close()

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = uc.Chrome(use_subprocess=True, options=options)
wait = WebDriverWait(driver, 2)
driver.implicitly_wait(2)

driver.get('https://quasarzone.com/ajax/user/attendanceInsert')

driver.find_element(by=By.NAME, value="login_id").send_keys(_id)
driver.find_element(by=By.NAME, value="password").send_keys(_pw)
driver.find_element(by=By.CLASS_NAME, value="login-bt").click()

results = [json.loads(driver.find_element(by=By.TAG_NAME, value="body").text)]
results[-1]['site'] = 'QuasarZone'

driver.get('https://quasarplay.com/ajax/user/attendanceInsert')

driver.find_element(by=By.NAME, value="login_id").send_keys(_id)
driver.find_element(by=By.NAME, value="password").send_keys(_pw)
driver.find_element(by=By.XPATH, value='//*[@class="login-bt"]/a').click()

results.append(json.loads(driver.find_element(by=By.TAG_NAME, value="body").text))
results[-1]['site'] = 'QuasarPlay'

for result in results:
    if result['result'] == 'fail':
        logging.error('[' + result['site'] + '] ' + result['msg'])
