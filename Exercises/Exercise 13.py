
# 1. Base class Vehicle and derived Car and Bike
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

c = Car()
c.move()
c.wheels()
b = Bike()
b.move()
b.wheels()


# 2. Single inheritance Person -> Employee
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def show(self):
        print("Employee Name:", self.name)

e = Employee("Yash")
e.show()


# 3. Multiple inheritance Teacher, Researcher -> Professor
class Teacher:
    def teach(self):
        print("Teaching students")

class Researcher:
    def research(self):
        print("Doing research")

class Professor(Teacher, Researcher):
    pass

p = Professor()
p.teach()
p.research()


# 4. Multilevel inheritance Animal -> Mammal -> Dog
class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.walk()
d.bark()


# 5. Hierarchical inheritance Shape -> Circle, Rectangle, Triangle
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area of Circle")

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle")

class Triangle(Shape):
    def area(self):
        print("Area of Triangle")

Circle().area()
Rectangle().area()
Triangle().area()


# 6. Abstract class Payment
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

class NetBanking(Payment):
    def pay(self):
        print("Paid using Net Banking")

CreditCard().pay()
UPI().pay()
NetBanking().pay()


# 7. Method overloading using default arguments
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

cal = Calculator()
print(cal.add(5))
print(cal.add(5, 10))
print(cal.add(5, 10, 15))


# 8. Method overriding Bird -> Parrot
class Bird:
    def sound(self):
        print("Bird sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot talks")

Parrot().sound()


# 9. Exception if withdrawal > balance
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amount

acc = BankAccount(1000)
try:
    acc.withdraw(1500)
except ValueError as e:
    print(e)


# 10. Encapsulation with private variable
class Customer:
    def __init__(self):
        self.__balance = 0

    def set_balance(self, amount):
        self.__balance = amount

    def get_balance(self):
        return self.__balance

cust = Customer()
cust.set_balance(500)
print("Balance:", cust.get_balance())


# 11. Class variable vs Instance variable
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Amit")
s2 = Student("Rahul")
print(s1.school, s1.name)
print(s2.school, s2.name)


# 12. Polymorphism using make_sound()
class Dog:
    def make_sound(self):
        print("Bark")

class Cat:
    def make_sound(self):
        print("Meow")

class Cow:
    def make_sound(self):
        print("Moo")

for animal in (Dog(), Cat(), Cow()):
    animal.make_sound()


# 13. Operator overloading (+)
class ComplexNumber:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return ComplexNumber(self.r + other.r, self.i + other.i)

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)
c3 = c1 + c2
print(c3.r, "+", c3.i, "i")


# 14. Multiple constructors using classmethod
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, data):
        return cls(data)

p = Person.from_string("Yash")
print(p.name)


# 15. Polymorphism Appliance
class Appliance:
    def run(self):
        pass

class WashingMachine(Appliance):
    def run(self):
        print("Washing clothes")

class Refrigerator(Appliance):
    def run(self):
        print("Cooling items")

WashingMachine().run()
Refrigerator().run()


# 16. super() usage
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")

Child().show()


# 17. Exception handling division by zero
class MathOperation:
    def divide(self, a, b):
        try:
            print(a / b)
        except ZeroDivisionError:
            print("Cannot divide by zero")

MathOperation().divide(10, 0)


# 18. Abstract Library system
class Item(ABC):
    @abstractmethod
    def info(self):
        pass

class Book(Item):
    def info(self):
        print("This is a Book")

class Magazine(Item):
    def info(self):
        print("This is a Magazine")

Book().info()
Magazine().info()


# 19. Destructor usage
class Demo:
    def __del__(self):
        print("Object destroyed")

d = Demo()
del d


# 20. Custom exception InsufficientFundsError
class InsufficientFundsError(Exception):
    pass

class Bank:
    def withdraw(self, balance, amount):
        if amount > balance:
            raise InsufficientFundsError("Not enough funds")
        return balance - amount

try:
    Bank().withdraw(500, 800)
except InsufficientFundsError as e:
    print(e)


# 21. Encapsulation in Car class
class Car:
    def __init__(self):
        self.__price = 0

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

car = Car()
car.set_price(800000)
print("Car Price:", car.get_price())


# 22. Polymorphism area()
class Shape:
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area of Square")

class Circle(Shape):
    def area(self):
        print("Area of Circle")

Square().area()
Circle().area()


# 23. Singleton Logger class
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

l1 = Logger()
l2 = Logger()
print(l1 is l2)


# 24. Hybrid inheritance
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.showA()
d.showB()
d.showC()


# 25. Duck typing
class Bird:
    def fly(self):
        print("Bird flies")

class Aeroplane:
    def fly(self):
        print("Aeroplane flies")

def make_it_fly(obj):
    obj.fly()

make_it_fly(Bird())
make_it_fly(Aeroplane())