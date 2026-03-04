from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


# Child class1
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")


# Child class2
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")


# Child class3
class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started")


car = Car()
bike = Bike()
bus = Bus()

car.start_engine()
bike.start_engine()
bus.start_engine()