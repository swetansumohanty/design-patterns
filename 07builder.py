"""
Builder Design Pattern
----------------------
It is a creational design pattern and used to create complex object in step by step.
"""

from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.__product = Product()

    @property
    def product(self):
        product = self.__product
        self.reset()
        return product

    def step1(self):
        self.__product.add("partA")

    def step2(self):
        self.__product.add("partB")

    def step3(self):
        self.__product.add("partC")


class ConcreteBuilder2(Builder):
    pass


class Product:
    def __init__(self):
        self.__arr = []

    def add(self, part):
        self.__arr.append(part)

    def list_products(self):
        return ",".join(item for item in self.__arr)


class Director:
    def __init__(self, builder):
        self.__builder = builder

    def build_minimal_product(self):
        self.__builder.step1()

    def build_full_fleged_product(self):
        self.__builder.step1()
        self.__builder.step2()
        self.__builder.step3()


if __name__ == "__main__":
    #  building minimal product
    concrete_builder1_obj = ConcreteBuilder1()
    dir_obj = Director(concrete_builder1_obj)

    dir_obj.build_minimal_product()
    products = concrete_builder1_obj.product.list_products()
    print("product with minimal feature", products)

    # -------------

    #  building full fledged product
    dir_obj.build_full_fleged_product()
    products = concrete_builder1_obj.product.list_products()
    print("product with maximum feature", products)
