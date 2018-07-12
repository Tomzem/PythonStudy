def debug(func):
    def wrapper(*args, **kwargs):
        print("enter {}()".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


@debug
def say(something, thing):
    print("{} {}".format(thing, something))


say("python", "hello")
