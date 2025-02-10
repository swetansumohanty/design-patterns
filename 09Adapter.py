"""
:Adapter:
=========

- Adapter is a structural design pattern, that allows incompatible objects to collaboarte.
- The adapter acts as a wrapper between two objects, it catches call from one object and transform them to format and 
  interface recognizable to by second object.
"""

#  :using Inheritence:
print("# using Inheritence #")


class Target:
    def request(self):
        return "i am target"


class Adaptee:
    def specifi_request(self):
        return "i am specific request"


class Adapter(Target, Adaptee):
    def request(self):
        return self.specifi_request()[::-1]


def client_code(target):
    return target.request()


if __name__ == "__main__":
    print("-- creating target object")
    target = Target()
    target_response = client_code(target)
    print("-- target response: {}".format(target_response))

    print("-- creating Adaptee ")
    adaptee = Adaptee()
    adaptee_response = adaptee.specifi_request()
    print("-- adaptee response: {}".format(adaptee_response))

    print(" -- create Adapter ")
    adapter = Adapter()
    adapter_response = client_code(adapter)
    print("-- adaptee_response: {}".format(adapter_response))


# :using composition:
print("# using composition #")


class Target:
    def request(self):
        return "i am target"


class Adaptee:
    def specifi_request(self):
        return "i am specific request"


class Adapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specifi_request()[::-1]


def client_code(target):
    return target.request()


if __name__ == "__main__":
    print("-- creating target object")
    target = Target()
    target_response = client_code(target)
    print("-- target response: {}".format(target_response))

    print("-- creating Adaptee ")
    adaptee = Adaptee()
    adaptee_response = adaptee.specifi_request()
    print("-- adaptee response: {}".format(adaptee_response))

    print(" -- create Adapter ")
    adapter = Adapter(adaptee)
    adapter_response = client_code(adapter)
    print("-- adaptee_response: {}".format(adapter_response))
