def debug(func):
    def wrapper():
        print("enter {}()".format(func.__name__))
        return func()
    return wrapper


@debug
def say_hello():
    print("hello python")


@debug
def say_bye():
    print("bye python")


say_hello()
say_bye()