# Section A  :  
# Question 1 : Sales  data  Clineanig (List / String / Control structers)

sales = ["200", " 340", "N/A", "500", "None", " 150 ", "800"]

clean_sales = []
for s in sales:
    s = s.strip()               
    if s != "N/A" and s != "None":
        clean_sales.append(int(s))

total_sales = sum(clean_sales)

print("Clean Sales List:", clean_sales)
print("Total Sales:", total_sales)

# Question 2 :  temperature analysis (List  Comprehension)

temp = [22.5, 25.1, 27.0, 30.5, 21.2, 33.1, 35.2]

#Create a list of temperatures in Fahrenheit using list comprehension.
#Formula: F = C * 9/5 + 32
temp_fahrenheit = [round((c * 9/5) + 32, 2) for c in temp]
print("Temperatures in Fahrenheit:", temp_fahrenheit)

# Question 3: Unique Customer IDs (Set Use-Case)

customer_ids = [101, 102, 103, 102, 101, 104, 105, 103]

unique_customer_ids = set(customer_ids)
print("Unique Customer IDs:", unique_customer_ids)

# Question 4: Product Price Lookup (Dictionary Comprehension)

products = ["Pen", "Book", "Bag"]
prices = [10, 100, 500]
product_price_dict = {products[i]: prices[i] for i in range(len(products))}
print("Product Price Dictionary:", product_price_dict)

# Question 5: Filter High Ratings (Tuples & Condition)

ratings = (4.5, 2.3, 3.8, 4.9, 1.8, 4.2)
high_ratings = tuple(r for r in ratings if r >= 4.0)
print("High Ratings (4.0 and above):", high_ratings)

# Section B :
# Question 6 : Student Attendance Analyzer

attendance = [1, 1, 0, 1, 1, 0, 1] 
# 1 = Present, 0 = Absent

total_present_days = sum(attendance)
print("Total Present Days:", total_present_days)

total_classes = len(attendance)
attendance_percentage = (total_present_days / total_classes) * 100    
print("Attendance Percentage:", attendance_percentage, "%")   

total_absent_days = total_classes - total_present_days
print("Total Absent Days:", total_absent_days)

# Question 7 : Social Media Comment Filter
comments = ["Great!", "bad product", "Excellent", "worst!", "Good", "awful experience"]

positive_comments = [comment for comment in comments if comment.lower() not in ["bad product", "worst!", "awful experience"]]
print("Positive Comments:", positive_comments)

# Question 8 : Revenue Classification (If-Else Logic)
revenue = 4500
if revenue < 1000:
    classification = "Low"
elif 1000 <= revenue <= 5000:
    classification = "Medium"   
else:
    classification = "High"
print("Revenue Classification:", classification)

# Section C :
# Question 9 : Create a Class Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    # Annual Salary Method
    def annual_salary(self):
        return self.salary * 12

emp = Employee("Yash more ", 3000)
print("Employee Name:", emp.name)
print("Monthly Salary:", emp.salary) 
print("Annual Salary:", emp.annual_salary()) 

# Question 10 : Bank Account Simulation (OOP + Logic)
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New Balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")


account = BankAccount("Yash more", 1000)
account.deposit(5000)
account.withdraw(2000)

print("Final Balance:", account.balance)
