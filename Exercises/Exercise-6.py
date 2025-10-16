# -----------------------------
# 1. Accept marks of 5 subjects
# -----------------------------
marks = [int(input(f"Enter marks of subject {i+1}: ")) for i in range(5)]
total = sum(marks)
percentage = total / 5
if percentage >= 60:
    division = "First Division"
elif percentage >= 45:
    division = "Second Division"
elif percentage >= 33:
    division = "Third Division"
else:
    division = "Fail"
print("Total:", total, "Percentage:", percentage, "Division:", division)

# -----------------------------
# 2. Temperature category
# -----------------------------
temp = float(input("Enter temperature: "))
if temp > 35:
    print("Hot")
elif temp >= 15:
    print("Moderate")
else:
    print("Cold")

# -----------------------------
# 3. Armstrong number
# -----------------------------
num = int(input("Enter number: "))
s = sum(int(d)**len(str(num)) for d in str(num))
print("Armstrong" if s == num else "Not Armstrong")

# -----------------------------
# 4. Perfect number
# -----------------------------
num = int(input("Enter number: "))
div_sum = sum(i for i in range(1, num) if num % i == 0)
print("Perfect Number" if div_sum == num else "Not Perfect")

# -----------------------------
# 5. Character type
# -----------------------------
ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")

# -----------------------------
# 6. Palindrome string
# -----------------------------
s = input("Enter string: ")
print("Palindrome" if s == s[::-1] else "Not Palindrome")

# -----------------------------
# 7. Ticket price by age
# -----------------------------
age = int(input("Enter age: "))
if age < 5:
    print("Free")
elif age <= 12:
    print("Ticket = Rs 100")
elif age <= 59:
    print("Ticket = Rs 200")
else:
    print("Ticket = Rs 150")

# -----------------------------
# 8. Income Tax calculation
# -----------------------------
income = float(input("Enter income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = 0.05 * (income - 250000)
elif income <= 1000000:
    tax = 0.2 * (income - 500000) + 12500
else:
    tax = 0.3 * (income - 1000000) + 112500
print("Tax:", tax)

# -----------------------------
# 9. Harshad number
# -----------------------------
num = int(input("Enter number: "))
digit_sum = sum(int(d) for d in str(num))
print("Harshad Number" if num % digit_sum == 0 else "Not Harshad")

# -----------------------------
# 10. Pythagorean triplet
# -----------------------------
a, b, c = sorted([int(input("Enter number: ")) for _ in range(3)])
print("Pythagorean Triplet" if a*a + b*b == c*c else "Not Triplet")

# -----------------------------
# 11. Continue example
# -----------------------------
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# -----------------------------
# 12. Break example
# -----------------------------
for i in range(1, 11):
    if i == 7:
        break
    print(i)

# -----------------------------
# 13. Pass example
# -----------------------------
for i in range(1, 6):
    if i == 3:
        pass
    print(i)

# -----------------------------
# 14. Prime number with break
# -----------------------------
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

# -----------------------------
# 15. Positive numbers only
# -----------------------------
nums = [int(input("Enter number: ")) for _ in range(10)]
for n in nums:
    if n < 0:
        continue
    print(n)

# -----------------------------
# 16. Divisible by 5 and 11
# -----------------------------
num = int(input("Enter number: "))
print("Divisible by 5 and 11" if num % 5 == 0 and num % 11 == 0 else "Not Divisible")

# -----------------------------
# 17. String has alphabets & digits
# -----------------------------
s = input("Enter string: ")
if any(ch.isalpha() for ch in s) and any(ch.isdigit() for ch in s):
    print("Contains both alphabets and digits")
else:
    print("Does not contain both")

# -----------------------------
# 18. Prime and Odd
# -----------------------------
num = int(input("Enter number: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime and num % 2 == 1:
    print("Prime and Odd")
else:
    print("Not Both")

# -----------------------------
# 19. Century year
# -----------------------------
year = int(input("Enter year: "))
print("Century Year" if year % 100 == 0 else "Not Century")

# -----------------------------
# 20. First multiple of second
# -----------------------------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Multiple" if a % b == 0 else "Not Multiple")

# -----------------------------
# 21. ATM Program
# -----------------------------
balance = 10000
amount = int(input("Enter withdrawal amount: "))
if amount % 100 == 0 and balance - amount >= 500:
    balance -= amount
    print("Remaining Balance:", balance)
else:
    print("Transaction Failed")

# -----------------------------
# 22. Railway Ticket Discount
# -----------------------------
age = int(input("Enter age: "))
classtype = input("Enter class type (AC/General): ")
fare = 500
if age < 12:
    fare *= 0.5
elif age >= 60:
    fare *= 0.6
print("Fare:", fare)

# -----------------------------
# 23. Cinema Hall Program
# -----------------------------
movie = input("Enter movie type (Normal/3D/IMAX): ")
age = int(input("Enter age: "))
if movie.lower() == "normal":
    price = 150
elif movie.lower() == "3d":
    price = 250
else:
    price = 350
if age < 12:
    price *= 0.5
print("Ticket Price:", price)

# -----------------------------
# 24. Online Shopping Discount
# -----------------------------
purchase = float(input("Enter purchase amount: "))
if purchase >= 5000:
    discount = 0.2 * purchase
elif purchase >= 2000:
    discount = 0.1 * purchase
else:
    discount = 0
print("Final Amount:", purchase - discount)

# -----------------------------
# 25. Grading with Remark
# -----------------------------
marks = int(input("Enter marks: "))
if marks >= 90:
    grade, remark = "A", "Excellent"
elif marks >= 75:
    grade, remark = "B", "Good"
elif marks >= 50:
    grade, remark = "C", "Average"
elif marks >= 33:
    grade, remark = "D", "Pass"
else:
    grade, remark = "F", "Fail"
print("Grade:", grade, "| Remark:", remark)
