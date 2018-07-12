class Debug(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("enter {}()".format(self.func.__name__))
        return self.func(*args, **kwargs)


@Debug
def say(something):
    print("hello {}".format(something))


say("python")
