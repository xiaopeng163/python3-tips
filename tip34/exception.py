
class MyException(Exception):
    pass


class NameTooShort(MyException):
    pass

class NameTooLong(MyException):
    pass


class NameNotFound(MyException):
    pass

