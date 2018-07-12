def debug(who, why):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("{} enter {}({})".format(who, func.__name__, why))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper


@debug(why="Tomze", who="hi")
def say(something):
    print("hello {}".format(something))


@debug("Tone", "hi")
def say_bye(something, thing):
    print("{} {}".format(something, thing))


say("python")
say_bye("python", "bye")
