
# 1. Armstrong Number
def is_armstrong(n):
    s = str(n)
    p = len(s)
    total = 0
    for d in s:
        total += int(d) ** p
    return total == n

print("1. Armstrong (153):", is_armstrong(153))


# 2. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("2. Factorial (5):", factorial(5))


# 3. Reverse a string
def reverse_string(s):
    return s[::-1]

print("3. Reverse:", reverse_string("Python"))


# 4. Prime number check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("4. Prime (17):", is_prime(17))


# 5. Count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

print("5. Vowels:", count_vowels("Education"))


# 6. Compound Interest
def compound_interest(p, r, t):
    return p * (1 + r / 100) ** t

print("6. Compound Interest:", compound_interest(1000, 10, 2))


# 7. Palindrome string
def is_palindrome(s):
    return s == s[::-1]

print("7. Palindrome:", is_palindrome("madam"))


# 8. GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("8. GCD:", gcd(48, 18))


# 9. Fibonacci series
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print("9. Fibonacci Series:", fibonacci_series(7))


# 10. Leap Year
def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

print("10. Leap Year:", is_leap_year(2024))


# 11. Maximum of three numbers
def max_of_three(a, b, c):
    return a if a > b and a > c else (b if b > c else c)

print("11. Max of Three:", max_of_three(10, 25, 15))


# 12. Remove punctuation
def remove_punctuation(s):
    punc = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/"
    result = ""
    for ch in s:
        if ch not in punc:
            result += ch
    return result

print("12. Remove Punctuation:", remove_punctuation("Hello!!! World."))


# 13. Largest word in sentence
def largest_word(sentence):
    words = sentence.split()
    largest = words[0]
    for w in words:
        if len(w) > len(largest):
            largest = w
    return largest

print("13. Largest Word:", largest_word("Python programming language"))


# 14. Sum of digits (recursion)
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print("14. Sum of Digits:", sum_of_digits(1234))


# 15. Even numbers from list
def even_numbers(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x)
    return result

print("15. Even Numbers:", even_numbers([1,2,3,4,5,6]))


# 16. Word frequency
def word_frequency(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    return freq

print("16. Word Frequency:", word_frequency("python is easy python"))


# 17. Anagram check
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print("17. Anagram:", is_anagram("listen", "silent"))


# 18. Area of circle
def area_circle(r):
    pi = 3.14159
    return pi * r * r

print("18. Area of Circle:", area_circle(5))


# 19. nth Fibonacci number
def nth_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print("19. nth Fibonacci:", nth_fibonacci(7))


# 20. Decimal to binary
def decimal_to_binary(n):
    return bin(n)[2:]

print("20. Decimal to Binary:", decimal_to_binary(10))


# 21. Smallest element in list
def smallest_element(lst):
    small = lst[0]
    for x in lst:
        if x < small:
            small = x
    return small

print("21. Smallest Element:", smallest_element([8,3,6,2,9]))


# 22. Remove duplicate characters
def remove_duplicates(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result

print("22. Remove Duplicates:", remove_duplicates("programming"))


# 23. Power using recursion
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print("23. Power:", power(2, 5))


# 24. Sum of list elements
def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total

print("24. Sum of List:", sum_list([10,20,30]))


# 25. Generate 6-digit OTP
def generate_otp():
    otp = id(object()) % 1000000
    if otp < 100000:
        otp += 100000
    return otp

print("25. OTP:", generate_otp())