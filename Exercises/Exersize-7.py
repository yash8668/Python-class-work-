# Python Loop & Logic Questions Solutions

# Q1. First 10 even numbers
for i in range(2, 21, 2):
    print(i, end=' ')
print()

# Q2. First 10 odd numbers
for i in range(1, 20, 2):
    print(i, end=' ')
print()

# Q3. First 10 even numbers in reverse order
for i in range(20, 1, -2):
    print(i, end=' ')
print()

# Q4. Factorial using for loop
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"Factorial of {n} is {fact}")

# Q5. Check prime number
num = 7
is_prime = True
for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        is_prime = False
        break
print(f"{num} is prime: {is_prime}")

# Q6. Print numbers 1–20 except multiples of 2 & 3
for i in range(1, 21):
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=' ')
print()

# Q7. Average of 10 numbers
nums = [1,2,3,4,5,6,7,8,9,10]
avg = sum(nums) / len(nums)
print(f"Average = {avg}")

# Q8. Largest and smallest
largest, smallest = max(nums), min(nums)
print(f"Largest = {largest}, Smallest = {smallest}")

# Q9. Odd numbers from list
L = [23, 45, 32, 25, 46, 33, 71, 90]
for i in L:
    if i % 2 != 0:
        print(i, end=' ')
print()

# Q10. Reverse word using loop
word = "develearn"
rev = ""
for ch in word:
    rev = ch + rev
print(rev)

# Q11. Count vowels in "education"
vowels = "aeiou"
count = 0
for ch in "education":
    if ch in vowels:
        count += 1
print(f"Number of vowels: {count}")

# Q12. Print primes up to n
n = 20
for num in range(2, n+1):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
print()

# Q13. Odd numbers using while
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1
print()

# Q14. Factorial using while
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(f"Factorial = {fact}")

# Q15. Extract domains
emails = {'aman@xmail.com','devesh@gmail.com','diya@ymail.com','jeba@zmail.com'}
domains = {email.split('@')[1] for email in emails}
print(domains)

# Q16. Pattern
for i in range(5, 0, -1):
    print((str(i) + ' ') * i)

# Q17. Predict the output:
    x=5
    while(x<15):
        print(x**2)
        x+=3

# Q18. Predict the output:
    a=7
    b=5
    while(a<9):
        print(a+b)
        a+=1

# Q19. Predict the output:
    b=15
    while(b>9):
        print("Hello")
        b=b-2

# Q20. Convert the following while loop into a for loop:
    x = 4
    while(x<=8):
        print(x*10)
        x+=2

# Q21. Predict the output:
    x=3
    if x>2 or x<5 and x==6:
        print("Bye")
    else:
        print("Thankyou")

# Q22. Predict the output:
    x,y=2,4
    if(x+y==10):
        print("Thankyou")
    else:
        print("Bye")

# Q23. Trace the output:
    x=10
    y=1
    while x>y:
        x=x-4
        y=y+3
        print(x)

# Q24. Trace the output:
    i=9
    while True:
        if i%3==0:
            break
        print("A")

# Q25. Trace the output:
    n=20
    for i in range(2, n//4):
        if n%i == 0:
            print("Python output based questions")
        else:
            print("Bye")