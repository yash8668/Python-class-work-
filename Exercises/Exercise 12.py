# Exercise-12: OOPs Concepts Part-1
# Basics of OOPs – Classes, Objects, Constructors, Methods


# 1. Create a Car class with attributes and discount method
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(self.brand, self.model, self.price)

    def apply_discount(self, percent):
        self.price -= self.price * percent / 100

car = Car("Tata", "Nexon", 1200000)
car.apply_discount(10)
car.display()


# 2. BankAccount class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt

    def check_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(5000)
acc.deposit(2000)
acc.withdraw(1000)
acc.check_balance()


# 3. Student class with grade
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def grade(self):
        if self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"

s = Student("Yash", 1, 78)
print("Grade:", s.grade())


# 4. Book class with discount
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def discount(self):
        if self.price > 500:
            self.price -= 50

b = Book("Python", "Guido", 600)
b.discount()
print(b.price)


# 5. Employee class
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def bonus(self):
        return self.salary * 0.10

e = Employee(30000)
print(e.annual_salary(), e.bonus())


# 6. ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_cart(self):
        print(self.items)

cart = ShoppingCart()
cart.add_item("Shoes")
cart.add_item("Bag")
cart.display_cart()


# 7. Restaurant class
class Restaurant:
    def __init__(self):
        self.menu = {}

    def add_dish(self, dish, price):
        self.menu[dish] = price

    def remove_dish(self, dish):
        self.menu.pop(dish, None)

    def show_menu(self):
        print(self.menu)

r = Restaurant()
r.add_dish("Pizza", 250)
r.show_menu()


# 8. Flight class
class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1

    def cancel_ticket(self):
        self.seats += 1

    def available_seats(self):
        print(self.seats)

f = Flight(100)
f.book_ticket()
f.available_seats()


# 9. Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_book(self, book):
        print(book in self.books)

lib = Library()
lib.add_book("Python")
lib.search_book("Python")


# 10. Laptop class
class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def upgrade_ram(self, extra):
        self.ram += extra

l = Laptop("HP", 8, 512)
l.upgrade_ram(8)
print(l.ram)


# 11. Movie class
class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def is_long(self):
        return self.duration > 120

m = Movie("RRR", 180)
print(m.is_long())


# 12. Mobile class
class Mobile:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def display(self):
        print(self.brand, self.battery)

mob = Mobile("Samsung", 80)
mob.display()


# 13. Hospital class
class Hospital:
    def __init__(self):
        self.patients = []

    def admit(self, name):
        self.patients.append(name)

    def discharge(self, name):
        if name in self.patients:
            self.patients.remove(name)

    def show(self):
        print(self.patients)

h = Hospital()
h.admit("Ram")
h.show()


# 14. Hotel class
class Hotel:
    def __init__(self, rooms):
        self.rooms = rooms

    def book_room(self):
        if self.rooms > 0:
            self.rooms -= 1

    def show_rooms(self):
        print(self.rooms)

hotel = Hotel(10)
hotel.book_room()
hotel.show_rooms()


# 15. Bus class
class Bus:
    def __init__(self, capacity):
        self.capacity = capacity

    def available_seats(self):
        print(self.capacity)

bus = Bus(50)
bus.available_seats()


# 16. Game class
class Game:
    def __init__(self):
        self.score = 0

    def update_score(self, points):
        self.score += points

g = Game()
g.update_score(10)
print(g.score)


# 17. University class
class University:
    def __init__(self):
        self.departments = []

    def add_dept(self, dept):
        self.departments.append(dept)

u = University()
u.add_dept("CS")
print(u.departments)


# 18. Bank class
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, bal):
        self.accounts[name] = bal

b = Bank()
b.add_account("Yash", 5000)
print(b.accounts)


# 19. Teacher class
class Teacher:
    def __init__(self):
        self.subjects = []

    def add_subject(self, sub):
        self.subjects.append(sub)

t = Teacher()
t.add_subject("Math")
print(t.subjects)


# 20. ShoppingMall class
class ShoppingMall:
    def __init__(self):
        self.shops = []

    def add_shop(self, shop):
        self.shops.append(shop)

mall = ShoppingMall()
mall.add_shop("Reliance")
print(mall.shops)


# 21. Cafe class
class Cafe:
    def __init__(self):
        self.menu = {}

    def add_item(self, item, price):
        self.menu[item] = price

    def bill(self):
        print(sum(self.menu.values()))

c = Cafe()
c.add_item("Coffee", 50)
c.bill()


# 22. Train class
class Train:
    def __init__(self, no, src, dest):
        self.no = no
        self.src = src
        self.dest = dest

    def route(self):
        print(self.src, "to", self.dest)

t = Train(123, "Pune", "Mumbai")
t.route()


# 23. Doctor class
class Doctor:
    def __init__(self):
        self.patients = 0

    def visit(self):
        self.patients += 1

    def fees(self):
        return self.patients * 300

d = Doctor()
d.visit()
print(d.fees())


# 24. MusicPlayer class
class MusicPlayer:
    def play(self):
        print("Playing song")

    def pause(self):
        print("Paused")

mp = MusicPlayer()
mp.play()


# 25. Zoo class
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, a):
        self.animals.append(a)

    def list_animals(self):
        print(self.animals)

z = Zoo()
z.add_animal("Lion")
z.list_animals()