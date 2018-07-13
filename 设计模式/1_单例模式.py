class Single(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance


a = Single()
b = Single()
print(a)
print(b)
