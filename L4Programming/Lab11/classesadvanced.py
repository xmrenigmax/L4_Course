class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name, age, sound, breed):
        super().__init__(name, age, sound)
        self.breed = breed

    def display(self):
        print(f"{self.name} is a {self.species} and is {self.age} years old.")

dog_1 = Dog("Rover", 5, "Woof", "Golden Retriever")
#print(type(dog_1))


# class 2

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
    
#     def __str_(self):
#         return f"{self.name} earns {self.salary} per month."
    

# class Manager(Employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department = department
    
#     def __str_(self):
#         return f"{self.name} earns {self.salary} per month and manages the {self.department} department."
    
# class Developer(Employee):
#     def __init__(self,name,salary,language):
#         super().__init__(name,salary)
#         self.language = language

#     def __str_(self):
#         return f"{self.name} earns {self.salary} per month and codes in {self.language}."
    

# manager1 = Manager("Alice", 10000, "HR")
# manager2 = Manager("Bob", 12000, "IT")
# developer1 = Developer("Charlie", 8000, "Python")
# developer2 = Developer("David", 9000, "Java")

# multiclass inheritance
class Base1:
    def __init__(self):
        print("Base1 class constructor")

class Base2:
    def __init__(self):
        print("Base2 class constructor")

class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived class constructor")

#derived = Derived()


# multiple inheritance employee
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

class Job:
    def __init__(self, salary, position):
        self.salary = salary
        self.position = position

    def __str__(self):
        return f"earns {self.salary} per month and is a {self.position}."

class Employee(Person, Job):
    def __init__(self, name, age, salary, position):
        Person.__init__(self, name, age)
        Job.__init__(self, salary, position)

    def __str__(self):
        return f"{Person.__str__(self)} and {Job.__str__(self)}"

employee = Employee("Alice", 25, 10000, "HR")
#print(employee)
