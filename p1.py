print(" Hello Python ")

# to extecute , use code runner or  ( shift +  enter  by  selecting perticular code ) 

#  single line comment  

"""
This is  
is a 
multi- line 
comment 

"""

"""
1.  Comments  in python  are denoted by  the # symbol 
2.  Any text after the #  symbol  onn  the  same line is ignored  by  the interpreter 
3. Comments  are  used  to explain the code  and  make  it easier  to  understanad 
4. Comments can  be used to  disable  a block  of  code  temporarily 
5. Comments  can be used to dopcument the codee  and make  it easier to understand for other  developers  
"""

#--------------------------------------------- Sessioin - 2 ---------------------------------------------------------
"""
1. Whate is the Python  Prograamming  ? 
 Python is  a high- level ,   interpreted , general-purpose  programming  language.  
 It  was designed  to be easy to read and  write , making   it ideal for  beginners and professionals  a like . 
 Python is popular in  web development  , data science , automation ,  AI/ML , game  development , and much more.



 Real-life Example :
1.  Instagram and yoiutube  use python for backend 
2.  Python scrips  are used to automate  Exal reports .
3.  You  can create chatbots , alculators , games  , and apps . 

"""

# Using print() Function 
print("Hello , World !  ")

#print () used  for message  printing /  to  display  output 
print(" Hello  Students ! Welcome to Python  Session-2 ")

# print your Name 
print(" My Name is  Yash")

"""
Python is a case sensitive  language .
ex -  Name , name, NAME , NamE will  be treates as different  words  
"""

#----------------------------------- Variables  ---------------------------------------------
"""
Variables are used to store  data in Python  that can be used  latter , it works  as a container . 
In python ,  you don't   need to declare  the type . 
You can  asssign  a value  to a variable  using  the assignment operator  (=) .

Rule/Nameing Convention : 
1.  Must start with  a latter or underscore  (ex - name ,  _name)
2. Can't start with a number (ex- 1name )
3. Can include latters,  digits,  underscores 
4. Can't  include  spaces or special   characters 
5. Can't  be  a reserved keywords ( ex- if , else , for  while ) 
"""

Name = "Yash"
Age = 21
Height= 160.5

print("Name:", Name )
print("Age : ", Age)
print ("Height:", Height)

# add two numbers 
a= 1 
b= 1
sum = a+b
print(sum)
print("sum")
print("sum:", sum) # This  willprint the sum of  a and b 

# multiply two numbers 
c= 2 
d= 3
print("product : ",c*d)

# String Concatenation
first_Name = "Yash"
last_Name = "More"
full_Name = first_Name + last_Name
full_Name = first_Name +" "+ last_Name
print(full_Name)

# print information of a Employee
Name = "Riya Agrawal"
Age = 20
Gender = "Female"
Position = "Software Engineer"
Salary = 60000

print("information of a Employee : ")
print("Name : ",Name)
print("Age : ",Age)
print("Gender : ",Gender)
print("Position : ",Position)
print("Salary : ",Salary)

# print information of Yourself


# Print with Multiple Arguments
name = "Yash"
age = 21
print("Name:", name, "Age:", age)

# Using String Concatenation (+)
first = "Hello"
second = "World"
print(first + " " + second)

# print multiple sentences together (\n escape sequence used for new line)
print("Hello Students, Welcome to python session-2\nThis is my first python program\n")

#String Concatenation
print("Hello Students, Welcome to python session-2" + "This is my first python program")

"""
Keywords -->

Keywords are reserved words that have a special meaning in Python. 
They cannot be used as variable names.

Examples:
False, True, None, if, else, elif, while, 
for, break, continue, def, return, import, 
as, class, try, except

"""

# Using   some keywords in  a program
is_Married = True 
print(is_Married)

"""
 Statements &  Comments --> 
 
 Statements --> 
Instructions  that Python can execute. 

Comments --> 
 Used to  Explain the code . They  are ignored by the Python interpreter.

 Signle-line : starts with # 

 Multi-line :  enclosed in ''' or """ 


# This is a signle-line comment 
name = " Yash "  # Shorting  name 
print(name)


"""
7.   Python Character Set

Charecter set refers to all  the valide characheters  Python  Understanding , including: 

1. Letters - A  to Z , a to z 
2. Digiits - 0 to 9 
3. Special Symbols -  + - * / () {} [] etc.
4. whitespace  -  space , tab ,  newline  
5.  other Characters -  Unicode  characters
"""
 
 # to excute  a selected   part in python  file  -->   select code  -- >   Shift +  Enter 

 # Using  letters ,  Digits , Special Charaters 
a = 10     # Digit
b = 20  
sum = a+b    # Using + Operator
print("sum: ",sum)

# Usimg  Whitespace  for indentation 
if  a < b :
 print (" a is smaller than  b ")  #  whitespace used  before print 


#------------------------------------------------------------------------------------------


# Example 1:  Simple Input
 name = input(" Enter your name :")
 print ("Hello,", name )


 # Example 2: Input two numbers  and ADD  them  
 num1 = input("Enter first number:" )
 num2 = input("Enter second  number:" )

 # Convert to  integers
num1 = int(num1)
num2 = int(num2)

print("Sum =" , num1 + num2)


#Example 3 : Inpute and Multiply Two Decimal Numbers 
x = float (input("Enter first number: "))
y = float (input("Enter Second number : "))
print("Product =",x*y)


# Example 4 : Input Age and print Eligibility
age = int ( input("Enter your age : "))

if  age >= 18: 
 print(" You are eligible to vote.")
else:
 print("You are  not eligible yet.")


# Example 5: Calculate Area of a rectangle

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of rectangle =", area)

