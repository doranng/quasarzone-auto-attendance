class MessagePool:
    _instance = None
    __messages = []

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def add_message(self, message):
        self.__messages.append(message)

    def get_messages(self):
        return self.__messages

    def clear_messages(self):
        self.__messages = []
