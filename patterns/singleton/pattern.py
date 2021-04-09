class SingletonType(type):
    """
    A SingletonType can be used as a metaclass which is inherited by the class we want to make Singleton of.
    In this way, we can keep all the instances of all the Singletons created in the _instances map object.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass:
    """
    This is a simple Singleton Class. This code would be repeated for any class we would like to make a Singleton
    of. Meaning: high verbosity and low reusability.
    """
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls._instance
