def opps():
    raise MyException("It's a feature, not a bug")


def test():
    pass

class MyException(Exception):
    pass