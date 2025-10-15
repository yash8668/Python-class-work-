# 1. Check whether a number is divisible by 7.
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")


# 2. Check whether a given number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Check whether a given number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 4. Check whether the character 'a' is present in the string "Python".
if 'a' in "Python":
    print("'a' is present")
else:
    print("'a' is not present")


# 5. Accept three numbers and find the largest number.
a, b, c = map(int, input("Enter three numbers: ").split())
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# 6. Check whether a given year is a leap year or not.
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


# 7. Attendance eligibility check.
total = int(input("Enter total working days: "))
present = int(input("Enter present days: "))
attendance = (present / total) * 100
print("Attendance % =", attendance)
if attendance >= 75:
    print("Eligible for exam")
else:
    print("Not eligible for exam")


# 8. Check vowel or not.
ch = input("Enter a character: ").lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Not a vowel")


# 9. Print day of week (1=Sunday, 2=Monday...).
day = int(input("Enter number (1-7): "))
if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Invalid input")


# 10. City → Monument
city = input("Enter city name: ").lower()
if city == "delhi":
    print("Red Fort")
elif city == "agra":
    print("Taj Mahal")
elif city == "jaipur":
    print("Jal Mahal")
else:
    print("Monument not found")


# 11. Eligible to vote?
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


# 12. Simple calculator
a, b = map(int, input("Enter two numbers: ").split())
op = input("Enter operation (+, -, *, /): ")
if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    print("Result =", a / b)
else:
    print("Invalid operation")


# 13. Check square or not.
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
if l == b:
    print("Square")
else:
    print("Not square")


# 14. Display grade by percentage.
per = float(input("Enter percentage: "))
if per < 25:
    print("Grade: D")
elif per < 45:
    print("Grade: C")
elif per < 50:
    print("Grade: B")
elif per < 60:
    print("Grade: B+")
elif per < 80:
    print("Grade: A")
else:
    print("Grade: A+")


# 15. Triangle type.
a, b, c = map(int, input("Enter three sides: ").split())
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


# 16. Triangle validity.
a, b, c = map(int, input("Enter three sides: ").split())
if a+b > c and a+c > b and b+c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")


# 17. Key exists in dictionary?
d = {"a": 1, "b": 2, "c": 3}
key = input("Enter key to check: ")
if key in d:
    print("Key exists")
else:
    print("Key does not exist")


# 18. Three-digit number or not.
num = int(input("Enter number: "))
if 100 <= num <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")


# 19. Electricity bill calculation.
units = int(input("Enter units: "))
if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 2
else:
    bill = (200 * 2) + (units - 300) * 5
print("Bill =", bill)


# 20. Wages/day calculation.
age = int(input("Enter age: "))
sex = input("Enter sex (M/F): ").upper()
if 18 <= age <= 30:
    if sex == "M":
        print("Wage: 700/day")
    else:
        print("Wage: 750/day")
elif 30 < age <= 40:
    if sex == "M":
        print("Wage: 800/day")
    else:
        print("Wage: 850/day")
else:
    print("Enter appropriate age")


# 21. Second largest of three numbers.
a, b, c = map(int, input("Enter three numbers: ").split())
nums = [a, b, c]
nums.sort()
print("Second largest:", nums[1])


# 22. Library fine.
days = int(input("Enter days late: "))
if days <= 5:
    fine = days * 2
elif days <= 10:
    fine = (5*2) + (days-5)*3
elif days <= 15:
    fine = (5*2) + (5*3) + (days-10)*4
else:
    fine = (5*2) + (5*3) + (5*4) + (days-15)*5
print("Fine =", fine)


# 23. Prime number check.
num = int(input("Enter number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


# 24. Palindrome number.
num = int(input("Enter number: "))
if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 25. Check whether two strings are anagrams.
str1 = input("Enter first string: ").lower().replace(" ", "")
str2 = input("Enter second string: ").lower().replace(" ", "")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not an Anagram")
