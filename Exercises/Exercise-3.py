# 1
a = 10
b = 20
a, b = b, a
print(a)
print(b)

# 2
x = 15
y = 25
y, x = x, y
print(x)
print(y)

# 3
a = 10
b = 15
a, b = b+5, a
print(a)
print(b)

# 4
a = 20
b = 30 + a
a, b = b, a
print(a)
print(b)

# 5
x = 20
y = 70 + x
x, y = y, x + y
print(x)
print(y)

# 6
x = 20
y = 70 - x
x, y = y, y + x
print(x)
print(y)

# 7
a, b = 2, 10
c, b = a * 5, a / 2
print(a, b, c)

# 8
a = 20
b = 5
a, b = a // 20, a ** b
print(a, b)

# 9
print(print(20))

# 10
print(print(int(50.50)))

# 11
print(print("shalini"))

# 12
a, b, c = 5, 10, 15
a, b, c = c, a, b
print(a, b, c)

# 13
x, y = 7, 14
x, y = x*y, x+y
print(x, y)

# 14
a, b = 100, 50
a, b = b-10, a+20
print(a, b)

# 15
a, b, c = 1, 2, 3
a, b, c = b+c, a+b, a
print(a, b, c)

# 16
x = 40
y = x // 10
x, y = y, x % 7
print(x, y)

# 17
a, b = 8, 4
a, b = a**b, b**a
print(a, b)

# 18
p, q = 3, 6
p, q = q//p, q%p
print(p, q)

# 19
x, y, z = 2, 4, 6
x, y, z = y*z, x*z, x+y
print(x, y, z)

# 20
m, n = 12, 18
m, n = n-m, m+n
print(m, n)

# 21
a = 5
a, b = a*2, a+10
print(a, b)

# 22
x, y = 2, 3
x, y = x**y, y**x
print(x, y)

# 23
a, b = 4, 9
a, b = (a+b)//2, (a*b)
print(a, b)

# 24
num1, num2 = 15, 25
num1, num2 = num2%num1, num1%num2
print(num1, num2)

# 25
x = 7
y = 3
x, y = (x+y)//y, (x*y)//y
print(x, y)
