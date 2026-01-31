# =========================================================
# Exercise-14: NumPy Library – 50 Real-World Problems
# =========================================================

import numpy as np
import time

# =========================
# Part A: Array Creation, Indexing, Slicing
# =========================

# 1. Create array of 1000 random integers and find max & min
arr = np.random.randint(1, 10000, 1000)
print("1. Max:", arr.max(), "Min:", arr.min())

# 2. Extract even numbers
print("2. Even numbers:", arr[arr % 2 == 0][:10])

# 3. 50 evenly spaced numbers between 10 and 100
arr3 = np.linspace(10, 100, 50)
print("3.", arr3[:5])

# 4. Reshape 36 elements into 6x6
arr4 = np.arange(36).reshape(6, 6)
print("4.\n", arr4)

# 5. 5x5 Identity matrix
print("5.\n", np.eye(5))

# 6. 3x3 center slice from 10x10 array
arr6 = np.random.randint(1, 100, (10, 10))
print("6.\n", arr6[3:6, 3:6])

# 7. Replace negatives with 0
arr7 = np.array([-5, 3, -1, 7])
arr7[arr7 < 0] = 0
print("7.", arr7)

# 8. Reverse array without slicing
arr8 = np.arange(10)
print("8.", arr8[np.arange(len(arr8)-1, -1, -1)])

# 9. Prime numbers up to 100
primes = [x for x in range(2, 101) if all(x % y != 0 for y in range(2, int(x**0.5)+1))]
print("9.", np.array(primes))

# 10. Diagonal matrix
arr10 = np.array([1, 2, 3, 4])
print("10.\n", np.diag(arr10))


# =========================
# Part B: Aggregation & Statistics
# =========================

# 1. Mean, median, std
prices = np.random.randint(100, 500, 20)
print("B1 Mean:", np.mean(prices), "Median:", np.median(prices), "Std:", np.std(prices))

# 2. Cumulative sum
sales = np.array([100, 200, 150, 300])
print("B2.", np.cumsum(sales))

# 3. Correlation coefficient
height = np.array([150, 160, 170, 180])
weight = np.array([50, 60, 70, 80])
print("B3.", np.corrcoef(height, weight))

# 4. Percentiles
salary = np.random.randint(20000, 100000, 30)
print("B4.", np.percentile(salary, [25, 50, 75]))

# 5. Students above average
marks = np.random.randint(40, 100, 20)
print("B5.", np.sum(marks > np.mean(marks)))

# 6. Moving average
data = np.array([1, 2, 3, 4, 5])
print("B6.", np.convolve(data, np.ones(3)/3, mode='valid'))

# 7. Most frequent element
arr7b = np.array([1, 2, 2, 3, 3, 3])
print("B7.", np.bincount(arr7b).argmax())

# 8. Normalize array
arr8b = np.array([10, 20, 30])
print("B8.", (arr8b - arr8b.min()) / (arr8b.max() - arr8b.min()))

# 9. Standardize data
print("B9.", (arr8b - arr8b.mean()) / arr8b.std())

# 10. Variance
rain = np.array([100, 120, 80, 90])
print("B10.", np.var(rain))


# =========================
# Part C: Broadcasting & Vectorization
# =========================

# 1. Broadcasting addition
print("C1.\n", np.array([[1], [2], [3]]) + np.array([10, 20, 30]))

# 2. Celsius to Fahrenheit
c = np.array([0, 25, 37])
print("C2.", (c * 9/5) + 32)

# 3. Multiply columns by scalars
mat = np.array([[1, 2], [3, 4]])
print("C3.\n", mat * np.array([10, 100]))

# 4. BMI calculation
weight = np.random.randint(50, 90, 100)
height = np.random.uniform(1.5, 1.9, 100)
print("C4.", (weight / (height ** 2))[:5])

# 5. Element-wise multiplication
print("C5.\n", mat * mat)

# 6. Subtract row mean
print("C6.\n", mat - mat.mean(axis=1, keepdims=True))

# 7. Chessboard pattern
chess = np.indices((5, 5)).sum(axis=0) % 2
print("C7.\n", chess)

# 8. Min-max normalization
print("C8.", (salary - salary.min()) / (salary.max() - salary.min()))

# 9. Divide by column sum
print("C9.\n", mat / mat.sum(axis=0))

# 10. Euclidean distance
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("C10.", np.sqrt(np.sum((a - b) ** 2)))


# =========================
# Part D: Masking & Filtering
# =========================

# 1. Remove negative temperatures
temp = np.array([-5, 10, 20, -2])
print("D1.", temp[temp >= 0])

# 2. Salary above 50000
print("D2.", salary[salary > 50000])

# 3. Replace odd with -1
arrd = np.array([1, 2, 3, 4])
arrd[arrd % 2 != 0] = -1
print("D3.", arrd)

# 4. Days above 40°C
temps = np.array([35, 42, 45, 30])
print("D4.", np.sum(temps > 40))

# 5. Values between 100 and 200
data = np.array([50, 120, 180, 250])
print("D5.", data[(data >= 100) & (data <= 200)])

# 6. Students passed all subjects
marks = np.array([[60, 70, 80], [30, 50, 60]])
print("D6.", np.all(marks > 40, axis=1))

# 7. Index of max values
print("D7.", np.where(arr == arr.max()))

# 8. Replace NaN with mean
arr_nan = np.array([1, np.nan, 3])
arr_nan[np.isnan(arr_nan)] = np.nanmean(arr_nan)
print("D8.", arr_nan)

# 9. Outliers beyond 3 std
data = np.random.randn(100)
print("D9.", data[np.abs(data) > 3])

# 10. Split above & below median
median = np.median(salary)
print("D10 Above:", salary[salary > median])
print("Below:", salary[salary <= median])


# =========================
# Part E: Random, Linear Algebra, Performance
# =========================

# 1. Normal distribution
print("E1.", np.random.normal(0, 1, 1000)[:5])

# 2. Coin toss
toss = np.random.choice(['H', 'T'], 10)
print("E2.", np.unique(toss, return_counts=True))

# 3. Random walk
walk = np.cumsum(np.random.choice([-1, 1], 100))
print("E3.", walk[:10])

# 4. Dot product
print("E4.", np.dot(a, b))

# 5. Solve linear equations
A = np.array([[2, 3], [1, 2]])
B = np.array([5, 3])
print("E5.", np.linalg.solve(A, B))

# 6. Eigenvalues & vectors
vals, vecs = np.linalg.eig(A)
print("E6.", vals)

# 7. Matrix multiplication performance
m1 = np.random.rand(300, 300)
m2 = np.random.rand(300, 300)
start = time.time()
np.dot(m1, m2)
print("E7 Time:", time.time() - start)

# 8. Dice simulation
dice = np.random.randint(1, 7, (1000, 2))
sums = dice.sum(axis=1)
print("E8.", np.unique(sums, return_counts=True))

# 9. Student marks & average
marks = np.random.randint(40, 100, (100, 3))
print("E9.", marks.mean(axis=1)[:5])

# 10. NumPy vs List performance
lst = list(range(1_000_000))
start = time.time()
sum(lst)
print("List time:", time.time() - start)

arr_np = np.arange(1_000_000)
start = time.time()
arr_np.sum()
print("NumPy time:", time.time() - start)