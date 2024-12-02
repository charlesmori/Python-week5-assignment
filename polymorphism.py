# Animal base class
class Animal:
    def move(self):
        pass

# Subclass representing a Dog
class Dog(Animal):
    def move(self):
        print("The dog is running on four legs 🐕")

# Subclass representing a Bird
class Bird(Animal):
    def move(self):
        print("The bird is flying in the sky 🐦")

# Vehicle base class
class Vehicle:
    def move(self):
        pass

# Subclass representing a Car
class Car(Vehicle):
    def move(self):
        print("The car is driving on the road 🚗")

# Subclass representing a Plane
class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky ✈️")

# Demonstrating Polymorphism
# Creating instances of animals and vehicles
entities = [Dog(), Bird(), Car(), Plane()]

# Calling the move() method for each entity
for entity in entities:
    entity.move()
