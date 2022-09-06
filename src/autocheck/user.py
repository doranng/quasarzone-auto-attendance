from cryptography.fernet import Fernet
from getpass import getpass


def load_user_data():
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
    return dict(id=_id, pw=_pw)
