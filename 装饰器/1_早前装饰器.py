def debug(func):
    def wrapper():
        print("enter {}()".format(func.__name__))
        return func()
    return wrapper

def say_hello():
    print("hello python")

def say_bye():
    print("bye python")

say_hello = debug(say_hello)
say_bye = debug(say_bye)
say_hello()
say_bye()