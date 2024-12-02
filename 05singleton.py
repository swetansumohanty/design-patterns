"""
singleton pattern
=================
This pattern is useful when you want to create only one instance of the class.
"""


class Metaclass(type):
    """This is metaclass"""

    _instance = {}

    def __call__(cls, *args, **kwargs):

        # don't create,if the instance is already created
        if cls not in cls._instance:
            cls._instance[cls] = super(Metaclass, cls).__call__(*args, **kwargs)

            return cls._instance[cls]


class Singleton(metaclass=Metaclass):
    """This is singleton class"""

    def __init__(self):
        pass

    def get_item():
        pass


obj: Singleton = Singleton()
print(f"i am obj at {obj}")

obj2: Singleton = Singleton()  # o/p: None
print(f"i am obj at {obj2}")


#  when to use singleton design pattern
# 1 when connecting to third party serive you want only one connection to be opened
# 2 can be used for logging etc
