"""
Prototype Design Pattern
------------------------
- It is a creational design pattern.
- prototype is used to create copy of the object, without depending on concrete class.
"""

from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Enemy(Prototype):
    def __init__(self, name, speed, attack):
        self.name = name
        self.speed = speed
        self.attack = attack

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"name:{self.name}, speed: {self.speed} and attack: {self.attack}"


def client(prototype):
    print("start copying object ...")
    prototype_obj = prototype.clone()
    prototype_obj.speed = "10 kmph"
    prototype_obj.attack = 8
    print("object copied successfully")
    return prototype_obj


if __name__ == "__main__":
    enemy_obj = Enemy(name="saber", speed="19 kmph", attack=20)
    print("actual obj {}".format(enemy_obj))
    cloned_obj = client(enemy_obj)
    print("cloned obj {}".format(cloned_obj))
