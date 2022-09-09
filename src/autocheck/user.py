from cryptography.fernet import Fernet
from getpass import getpass


class User:
    def __init__(self):
        self.__load_user_data()

    @property
    def id(self):
        return self.__id

    @property
    def pw(self):
        return self.__pw

    @property
    def telegram_id(self):
        return self.__telegram_id

    def __load_user_data(self):
        fernet = Fernet(bytes(b'8bfv1k2-gZ74BDdUmT6T3kA66eZSJSbHr6YtPGgZ598='))
        try:
            f = open('userinfo.txt', 'r')
            data = f.readlines()
            self.__id = data[0].strip()
            self.__pw = fernet.decrypt(bytes(data[1], 'utf-8')).decode()
            self.__telegram_id = data[2].strip() if len(data) > 2 else None
        except FileNotFoundError:
            self.__id = input("id:")
            self.__pw = getpass("pw:")
            self.__telegram_id = input("telegram_id:")
            f = open('userinfo.txt', 'w')
            data = "%s\n%s\n%s" % (self.__id, fernet.encrypt(self.__pw.encode()).decode('utf-8'), self.__telegram_id)
            f.write(data)
        f.close()
