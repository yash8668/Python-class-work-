# Q1. Concatenate number and character
name = input("Enter your name: ")
birthyear = input("Enter your birth year: ")
print(name + birthyear)


# Q2. Email ID from username, domain, extension
username = input("Enter username: ")
domain = input("Enter domain: ")
extension = input("Enter extension: ")
print(username + "@" + domain + "." + extension)


# Q3. Full name
fname = input("Enter first name: ")
mname = input("Enter middle name: ")
lname = input("Enter last name: ")
print(fname, mname, lname)


# Q4. Percentage of student (5 subjects, total=500)
marks = []
for i in range(1, 6):
    marks.append(int(input(f"Enter marks of subject {i}: ")))
percentage = (sum(marks) / 500) * 100
print("Percentage =", percentage)


# Q5. Area of rectangle
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
print("Area of Rectangle =", l * b)


# Q6. Area of square
side = float(input("Enter side: "))
print("Area of Square =", side * side)


# Q7. Area of circle
import math
r = float(input("Enter radius: "))
print("Area of Circle =", math.pi * r * r)


# Q8. Perimeter of rectangle
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
print("Perimeter of Rectangle =", 2*l + 2*b)


# Q9. Perimeter of square
side = float(input("Enter side: "))
print("Perimeter of Square =", 4*side)


# Q10. Circumference of circle
r = float(input("Enter radius: "))
print("Circumference of Circle =", 2*math.pi*r)


# Q11. Volume of cube
side = float(input("Enter side: "))
print("Volume of Cube =", side**3)


# Q12. Volume of cuboid
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))
print("Volume of Cuboid =", l*b*h)


# Q13. Total Surface Area of Cube
side = float(input("Enter side: "))
print("TSA of Cube =", 6*side*side)


# Q14. Total Surface Area of Cuboid
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))
print("TSA of Cuboid =", 2*((l*b) + (b*h) + (l*h)))


# Q15. Even or Odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q16. Positive, Negative, or Zero
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Q17. Average of 3 subjects
m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
m3 = int(input("Enter marks3: "))
avg = (m1 + m2 + m3) / 3
print("Average =", avg)


# Q18. Celsius → Fahrenheit
c = float(input("Enter Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit =", f)


# Q19. Fahrenheit → Celsius
f = float(input("Enter Fahrenheit: "))
c = (f - 32) * 5/9
print("Celsius =", c)


# Q20. Simple Interest
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)


# Q21. Area of triangle
b = float(input("Enter base: "))
h = float(input("Enter height: "))
print("Area of Triangle =", 0.5 * b * h)


# Q22. Max and Min of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Maximum =", max(a, b))
print("Minimum =", min(a, b))


# Q23. Length of string
s = input("Enter string: ")
print("Length =", len(s))


# Q24. Reverse a string
s = input("Enter string: ")
print("Reverse =", s[::-1])


# Q25. Square and Cube of a number
num = int(input("Enter number: "))
print("Square =", num**2)
print("Cube =", num**3)
