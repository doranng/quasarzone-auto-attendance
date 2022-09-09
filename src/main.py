"""
quasar-zone auto attendance check
v0.2.0
"""
from src.autocheck.driver import create_web_drive
from src.autocheck.message.message import send_message
from src.autocheck.user import load_user_data
from src.autocheck.check import check


def main():
    driver = create_web_drive()
    user_data = load_user_data()
    results = check(driver, user_data)
    send_message(user_data, results)


if __name__ == "__main__":
    main()
