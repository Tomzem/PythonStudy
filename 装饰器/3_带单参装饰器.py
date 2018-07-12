def debug(func):
    def wrapper(thing):
        print("enter {}()".format(func.__name__))
        return func(thing)
    return wrapper


@debug
def say(something):
    print("hello {}".format(something))


say("python")