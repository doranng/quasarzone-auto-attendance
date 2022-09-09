"""
quasar-zone auto attendance check
v0.2.0
"""
from src.autocheck.message.message import Message
from src.autocheck.user import User
from src.autocheck.check import Check
from src.autocheck.driver import Driver


def main():
    driver = Driver.create_web_drive()
    user = User()
    results = Check().check(driver, user)
    Message().send_message(user, results)


if __name__ == "__main__":
    main()
