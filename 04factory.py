"""
1. Simple Factory Design Pattern
================================
Factory design pattern is a creational design pattern offering a clean and 
organized way to handle object creation.
"""


class Enemy:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def new_attack(self):
        # basic attack
        pass

    def take_damage(self):
        # damage
        pass


class Lesely(Enemy):
    def __init__(self):
        super().__init__("Lesely", 7, 5)

    def new_attack(self):
        print(f"attack with sniper having attack {self.attack} and defense {self.defense} ")

    def take_damage(self):
        print(f"medium damage")


class Bruno(Enemy):
    def __init__(self):
        super().__init__("Bruno", 8, 6)

    def attack(self):
        print(f"attack with a football having attack {self.attack} and defense {self.defense}")

    def take_damage(self):
        print(f"good damage")


# let's build the factory

class EnemyFactory:
    enemies :dict = {
        "Lesely": Lesely,
        "Bruno": Bruno
    }

    @staticmethod
    def create_enemy(enemy_type):
        enemy = EnemyFactory.enemies.get(enemy_type)
        if not enemy:
            raise ValueError(f"invalid enemy type {enemy_type}")
        return enemy()
    
enemy_lasely = EnemyFactory.create_enemy("Lesely")
enemy_lasely.new_attack()
# enemy_lasely.attack()




'''
2. Abstract Factory Pattern
========================
- Abstract factory pattern is also a creational design pattern
  that allows us to produce objects that belongs to same group 
  or category without specifying their concrete class.
'''
import random

class ClothingFactory:

    '''factory for clothes'''

    def __init__(self, cloth_fac = None): 
        self.cloth_fac = cloth_fac

    def show_cloth(self):

        '''used to display cloth'''
        
        cloth = self.cloth_fac()

        print(f'cloth type : {cloth}')
        print(f'MRP : {cloth.price()}')


class MensWear:

    '''cloth for men'''

    def __str__(self):
        
        return 'MensWear'

    def price(self):
        
        '''price'''

        return 2999
    

class KidsWear:

    '''cloth for women'''

    def __str__(self):
        
        return 'KidsWear'

    def price(self):

        '''price'''

        return 999
    

class WomensWear:

    '''cloth for women'''

    def __str__(self):
        
        return 'WomensWear'

    def price(self):

        '''price'''

        return 1999
    

def random_cloth():

    '''pick random cloth from the list'''

    return random.choice([KidsWear, MensWear, WomensWear])


if __name__ == '__main__':

    cloth = ClothingFactory(random_cloth())
 
    for i in range(5):
        cloth.show_cloth()
