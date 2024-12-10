
class car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def describe(self):
        print("This car is a", self.year, self.brand)


car = car("Toyota", 2019)
#car.describe()


class rectangle:
    def __init__(self):
        self.width = None
        self.height = None

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def display_info(self):
        print("Width:", self.width)
        print("Height:", self.height)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())

rectangle = rectangle()
rectangle.set_width(10)
rectangle.set_height(5)
#rectangle.display_info()


class Animal:
    def __init__(self):
        self.name = None
        self.sound = None

    def set_name(self, name):
        self.name = name

    def set_sound(self, sound):
        self.sound = sound

    def get_name(self):
        return self.name
    
    def get_sound(self):
        return self.sound
    
    def display_info(self):
        print("Name:", self.name)
        print("Sound:", self.sound)

animal = Animal()
animal.set_name("Dog")
animal.set_sound("Bark")
#animal.display_info()

class bankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance
    
    def display_info(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

bankAccount = bankAccount("John", 1000)
bankAccount.deposit(500)
bankAccount.withdraw(200)
#bankAccount.display_info()

class carDetails:
    def __init__(self, milage, name):
        self.milage = milage
        self.name = name

    def drive(self, distance):
        self.milage += distance

    def display(self):
        print("Car Name:", self.name)
        print("Total Mileage:", self.milage)


carDetails12 = carDetails(1000, "Toyota")
carDetails12.drive(500)
carDetails12.display()

