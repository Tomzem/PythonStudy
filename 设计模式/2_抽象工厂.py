import random

class PetShop(object):

    #一个宠物店
    def __init__(self, pet_factory = None):
        self.pet_factory = pet_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print("这是一只 {}".format(str(pet)))
        print("它的叫声是{}".format(pet.speak()))

class Dog(object):

   def speak(self):
        return "汪汪汪"

   def __str__(self):
       return "Dog"

class DogFactory(Dog):

    def get_pet(self):
        return Dog()


shop = PetShop(DogFactory())
shop.show_pet()