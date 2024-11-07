# Basic python class
# class Dog:
#     attr1 = "mammal"
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print(f"My name is {self.name}")

# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")

# print("Rodger is a {}".format(Rodger.__class__.attr1))
# print("Tommy is also a {}".format(Tommy.__class__.attr1))
# Rodger.speak()
# Tommy.speak()
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))

# Python code to demonstrate how parent constructors
# are called.

# Inheritance
# class Person(object):
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
    
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
#         Person.__init__(self, name, idnumber)
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Post: {}".format(self.post))

# a = Employee('Rahul', 886012, 200000, "Intern")
# a.display()
# a.details()

# Polymorphism
# class Bird:
#     def intro(self):
#         print("There are many types of birds.")
#     def flight(self):
#         print("Most of the birds can fly but some cannot.")

# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.")

# class ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly.")

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()
# obj_bird.intro()
# obj_bird.flight()
# obj_spr.intro()
# obj_spr.flight()
# obj_ost.intro()
# obj_ost.flight()

# Python program to
# demonstrate private members
# "__" double underscore represents private attribute. 
# Private attributes start with "__".

# # Creating a Base class
# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "GeeksforGeeks private" 

# # Creating a derived class
# class Derived():
#     def __init__(self):
#         super().__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)


# Driver code
# obj1 = Base()
# obj2 = Derived()
# print(obj1.a)
# print(obj1.__c)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class

# Abstraction
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length  # Private attribute
#         self.__width = width    # Private attribute
#     def area(self):
#         return self.__length * self.__width
#     def perimeter(self):
#         return 2 * (self.__length + self.__width)


# rect = Rectangle(5, 3)
# print(f"Area: {rect.area()}")          # Output: Area: 15
# print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 16

# print(rect.__length)  # This will raise an AttributeError as length and width are private attributes

# abstractmethod
# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def print():
#         pass

# class callable(abstract):
#     pass

# # a = abstract() # cant create object of an abstract class
# b = callable()
# b.print() # gives error. we didnt initialized the abstract method

from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def print(self):
        pass

class callable(abstract):
    def print(self):
        print("I initialized it")

b = callable()
b.print()