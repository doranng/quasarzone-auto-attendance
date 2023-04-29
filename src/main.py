"""
quasar-zone auto attendance check
v0.3.0
"""
from autocheck.message.Messenger import Messenger
from autocheck.User import User
from autocheck.Checker import Checker
from autocheck.WebDriver import WebDriver


def main():
    driver = WebDriver.create()
    user = User()
    if driver:
        Checker().check(driver, user)
    Messenger().send_messages(user)


if __name__ == "__main__":
    main()
