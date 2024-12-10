class Circle:
    def __init__(self):
        self.radius = None

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def __str__(self):
        return "Circle with radius: " + str(self.radius) + " and area: " + str(self.area())
    
circle = Circle()
circle.set_radius(5)
#print(circle)


class Student: 
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def set_grades(self, grades):
        self.grades = grades

    def get_grades(self):
        return self.grades
    
    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grades:", self.grades)
        print("Average:", self.get_average())

student = Student("John", 123)
student.set_grades([90, 80, 70])
student.add_grade(100)
#student.display_info()


class Employee:
    employees = [] 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary * 1.03
        Employee.employees.append(self) 

    def give_raise(self, salary):
        return self.salary

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

    def display_all_employees(cls):
        for employee in cls.employees:
            print("Name:", employee.name, "Salary:", employee.salary)

employee1 = Employee("John", 5000)
employee1.give_raise(5000)
employee1.display_info()

employee2 = Employee("Jane", 6000)
employee2.give_raise(6000)
employee2.display_info()

employee3 = Employee("Jack", 7000)
employee3.give_raise(7000)
employee3.display_info()

# Display all employees
Employee.display_all_employees()
