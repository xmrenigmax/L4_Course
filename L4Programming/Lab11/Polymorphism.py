import math
class Living_Being:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        return f"{self.name} is walking."

class Person(Living_Being):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def walk(self):
        return f"{self.name} is {self.age} years old and walks on two legs."

class Animal(Living_Being):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species
    
    def walk(self):
        return f"{self.name} is a {self.species}, {self.age} years old and walks on four legs."

# Create instances
# person1 = Person("Alice", 25)
# animal1 = Animal("Max", 5, "Dog")

# # Test the polymorphic behavior
# print(person1.walk())
# print(animal1.walk())


class Shape:    
    def area(self) -> 0:
        return 0
    
class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side**2
        
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius**2
    

# def print_area(shape: Shape):
#     print(shape.area())

# shapes = [Square(5), Circle(5)]
# for shape in shapes:
#     print_area(shape)