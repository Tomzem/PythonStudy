class Debug(object):
    def __init__(self, who="tomeze"):
        self.who = who

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("{} enter {}()".format(self.who, func.__name__))
            return func(*args, **kwargs)
        return wrapper


@Debug(who="tony")
def say(something):
    print("hello {}".format(something))


say("python")
