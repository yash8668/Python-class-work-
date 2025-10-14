# Q1
# input() is used to take user input as a string.
# print() is used to display output to the console.

# Q2
x = int(input("Enter an integer: "))

# Q3
# input() returns str, so arithmetic causes error unless converted:
# Example: int(input()) + int(input())

# Q4
a, b = map(int, input("Enter two numbers: ").split())

# Q5
name, age = "Alice", 25
print(f"My name is {name}, I am {age} years old.")

# Q6
# f-string: fast, concise → f"{var}"
# % formatting: "Hello %s" % name
# .format(): "Hello {}".format(name)

# Q7
print("Hello", end=" ")
print("World")

# Q8
with open("out.txt", "w") as f:
    print("Hello File", file=f)

# Q9
# sep: separates multiple arguments
# end: defines what to print at the end (default newline)

# Q10
with open("data.txt", "r") as f:
    content = f.read()

# ---------------- 2. Variables and Data Types (10 Questions) ----------------
# Q11
# Dynamic typing → variable type decided at runtime

# Q12
x = 10

# Q13
# int, float, complex, str, bool, list, tuple, dict, set, NoneType

# Q14
# Mutable: list, dict, set
# Immutable: int, str, tuple

# Q15
a = 5
b = a
# Both refer to same object until reassigned

# Q16
type(x)

# Q17
# int: whole numbers, float: decimals, complex: a+bj

# Q18
x = None  # NoneType

# Q19
# Python uses reference counting + garbage collector

# Q20
# No, keywords like if, while, for cannot be variable names

# ---------------- 3. Operators (10 Questions) ----------------
# Q21
# Arithmetic, Relational, Logical, Assignment, Bitwise, Identity, Membership

# Q22
# == compares values, is compares object identity

# Q23
print(7 // 2)  # 3
print(7 % 2)   # 1

# Q24
a, b = 5, 3
print(a & b, a | b, a ^ b, ~a, a << 1, a >> 1)

# Q25
print(True + True)  # 2 (True = 1)

# Q26
print(2 + 3 * 4)  # Multiplication first → 14

# Q27
print(5 > 3, 3 <= 3, 4 == 5)

# Q28
# Identity: is, is not
# Membership: in, not in

# Q29
# Short-circuit → evaluation stops once result is decided
print(False and print("no"))  # Skips second

# Q30
# Yes, operator overloading possible using magic methods

# ---------------- 4. Control Structures (10 Questions) ----------------
# Q31
if True:
    print("Yes")

# Q32
x = 10
if x > 0:
    print("Positive")
else:
    print("Non-positive")

# Q33
# elif provides cleaner multi-condition branching

# Q34
age = 20
if age >= 18:
    if age >= 60:
        print("Senior")
    else:
        print("Adult")

# Q35
x = 5
print(3 < x < 7)  # True

# Q36
# Wrong indentation → IndentationError

# Q37
# else is optional

# Q38
if 0:
    print("Yes")
# No output because 0 is False

# Q39
if True: pass

# Q40
if x > 0 and x % 2 == 0:
    print("Positive even")

# ---------------- 5. Strings (15 Questions) ----------------
# Q41
s1 = 'hello'
s2 = "hello"
s3 = '''multi-line'''

# Q42
# Strings are stored as sequences of Unicode characters

# Q43
# Single/Double → same
# Triple → multiline / docstring

# Q44
print("Hi" + "There", "Hi"*3)

# Q45
s = "Python"
print(s[0], s[-1], s[1:4])

# Q46
print(s[::-1])

# Q47
# Strings are immutable

# Q48
print("-".join(["a","b","c"]))
print("a-b-c".split("-"))

# Q49
print(" hello ".strip(), " hello ".lstrip(), " hello ".rstrip())

# Q50
print("py" in "python")

# Q51
print("banana".count("a"))

# Q52
print("banana".find("na"), "banana".index("na"))

# Q53
print("hello world".replace("world", "Python"))

# Q54
print("My name is {} and I am {}".format("Alice", 25))

# Q55
print("Line1\nLine2\tTabbed")

# ---------------- 6. Escape Sequences (5 Questions) ----------------
# Q56
# \n, \t, \', \", \\, \r

# Q57
# \n newline, \r carriage return, \t tab

# Q58
print("This is a backslash: \\")

# Q59
print("hello\bworld")

# Q60
print(r"Raw string \n no newline")

# ---------------- 7. Dictionary (10 Questions) ----------------
# Q61
# Dictionary = key-value pairs

# Q62
d = {"a": 1, "b": 2}

# Q63
print(d["a"])
d["c"] = 3

# Q64
# KeyError if key doesn’t exist

# Q65
print(d.get("x"))  # None
# safer than d["x"]

# Q66
for k, v in d.items():
    print(k, v)

# Q67
d1, d2 = {"a":1}, {"b":2}
d1.update(d2)

# Q68
squares = {x: x*x for x in range(5)}

# Q69
del d["a"]

# Q70
# Keys must be immutable (int, str, tuple)

# ---------------- 8. Set (10 Questions) ----------------
# Q71
# Set = unordered unique collection

# Q72
s = {1,2,3}

# Q73
# Set unordered, no duplicates; list ordered, allows duplicates

# Q74
s.add(4)
s.remove(2)

# Q75
a, b = {1,2,3}, {3,4,5}
print(a|b, a&b, a-b, a^b)

# Q76
print({1,1,2,2})  # {1,2}

# Q77
print({1,2}.issubset({1,2,3}))
print({1,2,3}.issuperset({1,2}))

# Q78
fs = frozenset([1,2,3])

# Q79
# Yes, since frozenset is immutable

# Q80
for i in s: print(i)

# ---------------- 9. Tuple (10 Questions) ----------------
# Q81
t = (1,2,3)  # Immutable list

# Q82
t = (5,)  # single element tuple

# Q83
# Tuples are immutable

# Q84
tuple([1,2,3])

# Q85
print(t[0])

# Q86
a, b = (10,20)
print(a, b)

# Q87
t = ([1,2], 3)  # Yes, mutable elements possible inside

# Q88
for i in t: print(i)

# Q89
# Tuples are used when immutability required

# Q90
print((1,2)+(3,4), (1,)*3)

# ---------------- 10. Type Casting (5 Questions) ----------------
# Q91
# Converting one type to another

# Q92
int("10"), float("3.14")

# Q93
# int("3.14") → error
# float("3.14") → 3.14

# Q94
try:
    x = int("abc")
except ValueError:
    x = 0

# Q95
tuple([1,2,3]), list((4,5,6))

# ---------------- 11. Mixed & Scenario-Based (5 Questions) ----------------
# Q96
a = "5"
b = 2
print(a * b)  # "55"

# Q97
s = "banana"
count = {ch: s.count(ch) for ch in set(s)}

# Q98
n = int(input("Enter number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Q99
x = None
if x:
    print("True")
else:
    print("False")

# Q100
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
