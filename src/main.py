"""
quasar-zone auto attendance check
v0.3.0
"""
from autocheck.message.Messenger import Messenger
from autocheck.User import User
from autocheck.Checker import Checker
from autocheck.WebDriver import WebDriver


def main():
    user = User()
    driver = WebDriver.create()
    if driver:
        Checker().check(driver, user)
    Messenger().send_messages(user)


if __name__ == "__main__":
    main()
