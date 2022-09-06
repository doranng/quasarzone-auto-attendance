"""
quasar-zone auto attendance check
v0.2.0
"""
from src.autocheck.driver import create_web_drive
from src.autocheck.user import load_user_data
from src.autocheck.check import check
from src.autocheck.log import create_log


def main():
    driver = create_web_drive()
    user_data = load_user_data()
    results = check(driver, user_data)
    create_log(results)


if __name__ == "__main__":
    main()
