# ======================================
# A) SETS – 25 QUESTIONS (SOLUTIONS)
# ======================================

# 1. Elements present in two sets but not in third
A = {1, 2, 3, 4}
B = {3, 4, 5}
C = {4}
print("1.", (A & B) - C)


# 2. Remove duplicates from list and return sorted set
lst = [5, 2, 2, 8, 1]
print("2.", sorted(set(lst)))


# 3. Check subset without built-in
X = {1, 2}
Y = {1, 2, 3}
is_subset = True
for x in X:
    if x not in Y:
        is_subset = False
print("3.", is_subset)


# 4. Union without union()
U = A.copy()
for x in B:
    U.add(x)
print("4.", U)


# 5. Symmetric difference
print("5.", (A - B) | (B - A))


# 6. Count common elements between multiple sets
S1 = {1, 2, 3}
S2 = {2, 3, 4}
S3 = {2, 5}
print("6.", len(S1 & S2 & S3))


# 7. Check disjoint
D1 = {1, 2}
D2 = {3, 4}
print("7.", len(D1 & D2) == 0)


# 8. Remove elements divisible by 3
s = {3, 6, 7, 9, 10}
s = {x for x in s if x % 3 != 0}
print("8.", s)


# 9. Unique words from paragraph
para = "python is easy and python is powerful"
print("9.", set(para.split()))


# 10. Max and Min without max() or min()
s = {5, 2, 9, 1}
mx = mn = None
for x in s:
    if mx is None or x > mx:
        mx = x
    if mn is None or x < mn:
        mn = x
print("10.", mx, mn)


# 11. Merge multiple sets
A = {1, 2}
B = {2, 3}
C = {4}
print("11.", A | B | C)


# 12. Squares from 1 to 50
print("12.", {x*x for x in range(1, 51)})


# 13. Count vowels in set
chars = {'a', 'b', 'e', 'i', 'o', 'u'}
vowels = "aeiou"
count = 0
for ch in chars:
    if ch in vowels:
        count += 1
print("13.", count)


# 14. Check if set is empty
s = set()
print("14.", len(s) == 0)


# 15. Remove smallest element
s = {5, 1, 9}
smallest = min(s)
s.remove(smallest)
print("15.", s)


# 16. Elements in first set but not second
A = {1, 2, 3}
B = {2, 4}
print("16.", A - B)


# 17. List of tuples to set of tuples
lst = [(1, 2), (3, 4), (1, 2)]
print("17.", set(lst))


# 18. Elements appearing only once among sets
A = {1, 2, 3}
B = {3, 4}
print("18.", (A | B) - (A & B))


# 19. Numbers divisible by 5 up to 200
print("19.", {x for x in range(1, 201) if x % 5 == 0})


# 20. Intersection using loop
A = {1, 2, 3}
B = {2, 3, 4}
inter = set()
for x in A:
    if x in B:
        inter.add(x)
print("20.", inter)


# 21. Count elements greater than 10
s = {5, 12, 18, 3}
count = 0
for x in s:
    if x > 10:
        count += 1
print("21.", count)


# 22. Sum of all elements
s = {1, 2, 3, 4}
total = 0
for x in s:
    total += x
print("22.", total)


# 23. Identify duplicates in list using sets
lst = [1, 2, 2, 3, 3, 4]
duplicates = set()
seen = set()
for x in lst:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)
print("23.", duplicates)


# 24. Replace odd numbers with their square
s = {1, 2, 3, 4}
new_set = set()
for x in s:
    if x % 2 != 0:
        new_set.add(x*x)
    else:
        new_set.add(x)
print("24.", new_set)


# 25. Check if set contains any prime number
s = {4, 6, 7, 9}
has_prime = False
for n in s:
    if n > 1:
        prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            has_prime = True
print("25.", has_prime)

# ======================================
# B) TUPLES – 25 QUESTIONS (SOLUTIONS)
# ======================================

# 1. Reverse a tuple without slicing
t = (1, 2, 3, 4)
rev = ()
for x in t:
    rev = (x,) + rev
print("1.", rev)


# 2. Count occurrences of a specific element
print("2.", t.count(2))


# 3. Convert tuple of integers to tuple of strings
t_str = tuple(str(x) for x in t)
print("3.", t_str)


# 4. Find second largest number
unique = sorted(set(t))
print("4.", unique[-2])


# 5. Concatenate multiple tuples
t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)
print("5.", t1 + t2 + t3)


# 6. Slice tuple to get alternate elements
print("6.", t[::2])


# 7. Tuples of length 3 from list of tuples
lst = [(1, 2), (1, 2, 3), (4, 5, 6), (7,)]
result = []
for x in lst:
    if len(x) == 3:
        result.append(x)
print("7.", result)


# 8. Check if tuple has all unique elements
print("8.", len(t) == len(set(t)))


# 9. Swap first and last elements
swapped = (t[-1],) + t[1:-1] + (t[0],)
print("9.", swapped)


# 10. Sort tuple without converting to list
sorted_tuple = tuple(sorted(t))
print("10.", sorted_tuple)


# 11. Count tuples where first element > last
tuples = [(5, 2), (1, 3), (4, 1)]
count = 0
for x in tuples:
    if x[0] > x[-1]:
        count += 1
print("11.", count)


# 12. Common elements in two tuples
t1 = (1, 2, 3)
t2 = (2, 3, 4)
common = ()
for x in t1:
    if x in t2 and x not in common:
        common += (x,)
print("12.", common)


# 13. Tuple from user input until "stop"
inputs = []
while True:
    val = input("Enter value (stop to end): ")
    if val == "stop":
        break
    inputs.append(val)
user_tuple = tuple(inputs)
print("13.", user_tuple)


# 14. Sum of elements in tuple
nums = (1, 2, 3, 4)
total = 0
for x in nums:
    total += x
print("14.", total)


# 15. Flatten tuple of tuples
tup = ((1, 2), (3, 4), (5,))
flat = ()
for x in tup:
    flat += x
print("15.", flat)


# 16. Replace specific value in tuple
t = (1, 2, 3, 2, 4)
new = ()
for x in t:
    if x == 2:
        new += (99,)
    else:
        new += (x,)
print("16.", new)


# 17. Tuples whose sum is even
tuples = [(1, 2), (2, 2), (3, 4)]
even_sum = []
for x in tuples:
    if sum(x) % 2 == 0:
        even_sum.append(x)
print("17.", even_sum)


# 18. Group tuple elements into pairs
t = (1, 2, 3, 4, 5, 6)
pairs = []
for i in range(0, len(t), 2):
    pairs.append((t[i], t[i+1]))
print("18.", pairs)


# 19. Tuple to dictionary (index as key)
t = ('a', 'b', 'c')
d = {}
for i in range(len(t)):
    d[i] = t[i]
print("19.", d)


# 20. Remove duplicates from tuple
t = (1, 2, 2, 3, 1)
unique = ()
for x in t:
    if x not in unique:
        unique += (x,)
print("20.", unique)


# 21. Count vowels in tuple of characters
chars = ('a', 'b', 'e', 'i', 'o', 'u')
vowels = "aeiou"
count = 0
for ch in chars:
    if ch in vowels:
        count += 1
print("21.", count)


# 22. Tuple with maximum sum
tuples = [(1, 2), (3, 4), (0, 10)]
max_tuple = tuples[0]
for x in tuples:
    if sum(x) > sum(max_tuple):
        max_tuple = x
print("22.", max_tuple)


# 23. Rotate tuple n places to the right
t = (1, 2, 3, 4, 5)
n = 2
n = n % len(t)
rotated = t[-n:] + t[:-n]
print("23.", rotated)


# 24. Tuple of key-value pairs to dictionary
pairs = (('a', 1), ('b', 2))
d = {}
for k, v in pairs:
    d[k] = v
print("24.", d)


# 25. Tuples with odd sum
tuples = [(1, 2), (2, 3), (3, 3)]
odd_sum = []
for x in tuples:
    if sum(x) % 2 != 0:
        odd_sum.append(x)
print("25.", odd_sum)

# ======================================
# C) DICTIONARIES – 25 QUESTIONS
# ======================================

# 1. Merge two dictionaries and sum duplicate keys
d1 = {'a': 10, 'b': 20}
d2 = {'b': 30, 'c': 40}
d = d1.copy()
for k, v in d2.items():
    d[k] = d.get(k, 0) + v
print("C1:", d)

# 2. Sort dictionary by keys
print("C2:", dict(sorted(d.items())))

# 3. Sort dictionary by values
print("C3:", dict(sorted(d.items(), key=lambda x: x[1])))

# 4. Key with maximum value
print("C4:", max(d, key=d.get))

# 5. Swap keys and values
print("C5:", {v: k for k, v in d.items()})

# 6. Character frequency in string
s = "python"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print("C6:", freq)

# 7. Combine two lists into dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print("C7:", dict(zip(keys, values)))

# 8. Remove items with value < 10
print("C8:", {k: v for k, v in d.items() if v >= 10})

# 9. Check key exists without 'in'
print("C9:", d.get('a') is not None)

# 10. Sum of dictionary values
print("C10:", sum(d.values()))

# 11. Difference between dictionaries
d3 = {'a': 10, 'd': 50}
print("C11:", set(d.items()) - set(d3.items()))

# 12. Nested dictionary for student marks
students = {
    "Yash": {"Math": 85, "Science": 90},
    "Amit": {"Math": 78, "Science": 88}
}
print("C12:", students)

# 13. Duplicate values in dictionary
vals = list(d.values())
duplicates = set(x for x in vals if vals.count(x) > 1)
print("C13:", duplicates)

# 14. Count vowels in dictionary keys
vowels = "aeiou"
count = 0
for k in d:
    for ch in k:
        if ch in vowels:
            count += 1
print("C14:", count)

# 15. Increment each value by 1
print("C15:", {k: v + 1 for k, v in d.items()})

# 16. Merge multiple dictionaries
d4 = {'x': 1}
d5 = {'y': 2}
merged = {}
for dic in (d, d4, d5):
    merged.update(dic)
print("C16:", merged)

# 17. Keys having even values
print("C17:", [k for k, v in d.items() if v % 2 == 0])

# 18. Reverse dictionary order
print("C18:", dict(reversed(list(d.items()))))

# 19. Dictionary from string (char count)
text = "hello"
char_count = {}
for ch in text:
    char_count[ch] = char_count.get(ch, 0) + 1
print("C19:", char_count)

# 20. Remove key only if exists
key = 'b'
if d.get(key) is not None:
    del d[key]
print("C20:", d)

# 21. Filter dictionary with prime values
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_dict = {k: v for k, v in d.items() if is_prime(v)}
print("C21:", prime_dict)

# 22. Key with minimum value
print("C22:", min(d, key=d.get))

# 23. Multiply all numeric values by 2
print("C23:", {k: v * 2 for k, v in d.items()})

# 24. Check if two dictionaries are equal
d_copy = d.copy()
print("C24:", d == d_copy)

# 25. List of dictionaries → single dictionary
lst_dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
final_dict = {}
for dic in lst_dicts:
    for k, v in dic.items():
        final_dict.setdefault(k, []).append(v)
print("C25:", final_dict)


# ======================================
# D) LISTS – 25 QUESTIONS
# ======================================

# 1. Pairs with sum equal to target
lst = [1, 2, 3, 4]
target = 5
pairs = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.append((lst[i], lst[j]))
print("D1:", pairs)

# 2. Remove duplicates without set
unique = []
for x in lst:
    if x not in unique:
        unique.append(x)
print("D2:", unique)

# 3. Flatten nested list
nested = [[1, 2], [3, 4]]
flat = []
for sub in nested:
    for x in sub:
        flat.append(x)
print("D3:", flat)

# 4. Rotate list left
n = 1
print("D4:", lst[n:] + lst[:n])

# 5. Longest increasing subsequence (simple)
lis = [lst[0]]
for x in lst[1:]:
    if x > lis[-1]:
        lis.append(x)
print("D5:", lis)

# 6. Frequency of elements
freq = {}
for x in lst:
    freq[x] = freq.get(x, 0) + 1
print("D6:", freq)

# 7. Merge two sorted lists
a = [1, 3, 5]
b = [2, 4, 6]
print("D7:", sorted(a + b))

# 8. Kadane’s algorithm
nums = [-2, 1, -3, 4, -1, 2, 1]
max_sum = curr = nums[0]
for x in nums[1:]:
    curr = max(x, curr + x)
    max_sum = max(max_sum, curr)
print("D8:", max_sum)

# 9. Split list into chunks
lst = [1, 2, 3, 4, 5, 6]
size = 2
chunks = [lst[i:i + size] for i in range(0, len(lst), size)]
print("D9:", chunks)

# 10. Common elements
print("D10:", list(set([1, 2, 3]) & set([2, 3, 4])))

# 11. Prime numbers in list
nums = [2, 3, 4, 5, 6]
primes = []
for n in nums:
    if is_prime(n):
        primes.append(n)
print("D11:", primes)

# 12. Replace negatives with zero
lst = [-1, 2, -3, 4]
print("D12:", [0 if x < 0 else x for x in lst])

# 13. Move zeros to end
lst = [0, 1, 0, 3, 0, 5]
print("D13:", [x for x in lst if x != 0] + [0] * lst.count(0))

# 14. Sort list of tuples by second element
lst = [(1, 3), (2, 1), (4, 2)]
print("D14:", sorted(lst, key=lambda x: x[1]))

# 15. Missing numbers in sequence
lst = [1, 2, 4, 6]
missing = []
for i in range(min(lst), max(lst)):
    if i not in lst:
        missing.append(i)
print("D15:", missing)

# 16. Reverse list without reverse()
rev = []
for x in lst:
    rev = [x] + rev
print("D16:", rev)

# 17. Second largest element
print("D17:", sorted(set(lst))[-2])

# 18. Squares of even numbers
print("D18:", [x * x for x in lst if x % 2 == 0])

# 19. Count elements greater than given number
num = 2
count = 0
for x in lst:
    if x > num:
        count += 1
print("D19:", count)

# 20. Merge multiple lists sorted
print("D20:", sorted([1, 4, 2] + [6, 5]))

# 21. Remove elements at odd indices
print("D21:", [lst[i] for i in range(len(lst)) if i % 2 == 0])

# 22. Pair with smallest difference
lst = [1, 3, 6, 10]
lst.sort()
min_diff = lst[1] - lst[0]
pair = (lst[0], lst[1])
for i in range(len(lst) - 1):
    if lst[i + 1] - lst[i] < min_diff:
        min_diff = lst[i + 1] - lst[i]
        pair = (lst[i], lst[i + 1])
print("D22:", pair)

# 23. Stack using list
stack = []
stack.append(10)
stack.append(20)
print("D23 pop:", stack.pop())

# 24. Queue using list
queue = []
queue.append(10)
queue.append(20)
print("D24 dequeue:", queue.pop(0))

# 25. Duplicate elements with indices
lst = [1, 2, 2, 3]
dup = {}
for i, x in enumerate(lst):
    dup.setdefault(x, []).append(i)
print("D25:", {k: v for k, v in dup.items() if len(v) > 1})