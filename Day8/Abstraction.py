from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass  

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")


dog = Dog()
dog.sound()
dog.sleep()

cat = Cat()
cat.sound()
cat.sleep()

cow = Cow()
cow.sound()
cow.sleep()