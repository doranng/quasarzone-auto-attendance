"""
quasar-zone auto attendance check
v0.1.0
"""
import undetected_chromedriver as uc
from cryptography.fernet import Fernet
from getpass import getpass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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
browser = driver

browser.get('https://quasarzone.com/login?nextUrl=https://quasarzone.com/')

browser.find_element(by=By.NAME, value="login_id").send_keys(_id)
browser.find_element(by=By.NAME, value="password").send_keys(_pw)
browser.find_element(by=By.XPATH, value='//*[@class="login-bt"]/a').click()

browser.get('https://quasarzone.com/users/attendance')

try:
    browser.find_element(by=By.XPATH, value='//*[@onclick="anttendanceCheck()"]').click()
    print("check succeeded")
except NoSuchElementException:
    print("already checked")

try:
    wait.until(ec.alert_is_present())
    alert = browser.switch_to.alert
    alert.dismiss()
except TimeoutException:
    print("no alert")

browser.get('https://quasarplay.com/login?nextUrl=https://quasarplay.com/')

browser.find_element(by=By.NAME, value="login_id").send_keys(_id)
browser.find_element(by=By.NAME, value="password").send_keys(_pw)
browser.find_element(by=By.XPATH, value='//*[@class="login-bt"]/a').click()

browser.get('https://quasarplay.com/users/attendance')

try:
    browser.find_element(by=By.XPATH, value='//*[@onclick="anttendanceCheck()"]').click()
    print("check succeeded")
except NoSuchElementException:
    print("already checked")

browser.quit()
