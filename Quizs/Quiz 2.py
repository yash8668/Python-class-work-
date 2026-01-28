#  Section A :  Datatypes  And Operators
#1. Ticket Fare Validation
#task: 
# #1identify the datatype of the fare
#2 convert it into integer
#3. calaculate 18% GST on fare 
fare ="1500"

print("Datatype of fare before conversion:", type(fare))
fare_int = int(fare)
print("Datatype of fare after conversion:", type(fare_int))
gst = fare_int * 0.18
print("GST on fare is:", gst)   

#2. Concession Eligibility check
#task:
#1. Use  comparison operators 
#2. Print "Concession Applied" or "No Concession"
ticket_amount = 4800
if ticket_amount >= 5000:
    print("Concession Applied")
else:
    print("No Concession")

#3. Seat Availability Status
#Task:
#Use logical operator
#Print "No Seats Available" or "Seats Available"
available_seats = 10
if available_seats <= 0:
    print("No Seats Available")
else:
    print("Seats Available")
# 4. Railway Wallet Deduction
wallet_balance = 2000
ticket_cost = 1500

#Task:
#Use assignment operator
#Update wallet balance after booking
wallet_balance -= ticket_cost
print("Updated wallet balance after booking:", wallet_balance)

#5. Monthly Season Ticket EMI
ticket_price = 12000
months = 6

#Task:
#Calculate monthly EMI using division operator
monthly_emi = ticket_price / months
print("Monthly EMI:", monthly_emi)

#  Section B :  Control Structures & Loops
#6. Ticket Booking Status Checker
status = "confirmed"

#Task:
#Use if-elif-else
#Print proper booking message
if status == "confirmed":
    print("Your ticket is confirmed.")
elif status == "waiting":
    print("Your ticket is on the waiting list.")
else:
    print("Your ticket booking failed.")

#7. Multiple Ticket Processing
#You have 5 ticket bookings.

#Task:
#Use for loop
#Print "Ticket Processed" for each booking
for i in range(5):
    print("Ticket Processed")

#8. Payment Retry System
#Retry payment 3 times if failed.

#Task:
#Use while loop
#Print attempt number
attempt = 1
while attempt <= 3:
    print("Attempt number:", attempt)
    attempt += 1

#9. Login Attempt Lock
#Passenger account locks after 3 wrong attempts.

#Task:
#Use break
#Stop loop when limit exceeds
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    attempts += 1
    print("Login attempt:", attempts)
    if attempts == max_attempts:
        print("Account locked due to too many failed attempts.")
        break

#10. Skip Cancelled Tickets
#Ticket list contains cancelled tickets.

#Task:
#Use continue
#Skip cancelled ticket IDs
ticket_ids = [101, 102, 'cancelled', 104, 'cancelled', 106]
for ticket in ticket_ids:
    if ticket == 'cancelled':
        continue
    print("Processing ticket ID:", ticket)

# Section C : Jump Statements & Logic Building

#11. Stop Tatkal Booking
#Tatkal booking stops when seats become 0.

#Task:
#Use break
tatkal_seats = 5
while tatkal_seats > 0:
    print("Tatkal seat booked. Seats Left:", tatkal_seats - 1)
    tatkal_seats -= 1       
    if tatkal_seats == 0:
        print("No Tatkal seats available. Booking stopped.")
        break

#12. Skip Invalid Station Code
#Station List contains invalid code "XXX".

#Task:
#Use continue
#Skip invalid station 
station_codes = ["NDLS", "XXX", "BCT", "XXX", "HWH"]
for code in station_codes:
    if code == "XXX":
        continue
    print("Processing station code:", code)

#13. placeholder for Refund Logic
# Refund logic not implemented yet.

#Task : 
#Use pass
def process_refund(ticket_id):
    pass 
print("Refund processing function defined.")

#14. Prime Ticket Number Check
#Check if ticket number is prime.

#Task:
#Use Loop + Logic building
ticket_number = 29
is_prime = True
for i in range(2, int(ticket_number**0.5) + 1):
    if ticket_number % i == 0:
        is_prime = False
        break
if is_prime:
    print("Ticket number is prime.")
else:
    print("Ticket number is not prime.")    

#15. Even-Odd Coach Numbers
#Coach numbers from 1 to 20

#Task:
#separate even and odd coach numbers
even_coaches = []
odd_coaches = []
for coach in range(1, 21):
    if coach % 2 == 0:
        even_coaches.append(coach)
    else:
        odd_coaches.append(coach)

print("Even Coach Numbers:", even_coaches)
print("Odd Coach Numbers:", odd_coaches)

# Section D : Patterns 

#16. Passenger rating Stars

passenger_rating = 5
for i in range(1, passenger_rating + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# 17. railway Sales Banner
# print inverted strar pattern for festive sales
sales_rating = 5
for i in range(sales_rating, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# 18. Booking Count Pyramid
#print Numeric pyramid for festive ticket sales.
levels = 5
for i in range(1, levels + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Section E : Strings 

# 19. Passenger Username Validation
# Username Must Be  Minimum 6 characters.

#Task:
# use string length 
# print valid / invalid massage

username = "traveler"
if len(username) >= 6:
    print("Valid Username")
else:
    print("Invalid Username")   

# 20. Email Domain Checker
# Passenger email must be end with "@gmail.com"
#Task:
# use string methods

email = "passenger@gmail.com"
if email.endswith("@gmail.com"):
    print("Valid Email Domain") 
else:
    print("Invalid Email Domain") 

# 21. Train name  Formating
# train name given by user
# Task:
# convert to uppercase
# convet to title case

train_name = "express train"
train_name_upper = train_name.upper()
train_name_title = train_name.title()
print("Train Name in Uppercase:", train_name_upper)
print("Train Name in Title Case:", train_name_title)      

# Section F : Lists , Tuples & Collections

# 22. Passenger Cart items 

# Task:
# Add New  Item  
# Remove an  item
# Display cart  Size 
cart = ["Sleeper Ticket", "AC Ticket", "Meal"]
cart.append("Blanket")  # Add New Item
cart.remove("Meal")     # Remove an item    
print("Cart Size:", len(cart))
print("Cart Items:", cart)

# 23. Ticket fare List 
# list of ticket fares
# Task:
# Find Maximum fare
# Find Minimum fare
# Calaculate Total fare
fares = [1500, 2500, 1200, 3000, 1800]
max_fare = max(fares)
min_fare = min(fares)
total_fare = sum(fares)
print("Maximum Fare:", max_fare)
print("Minimum Fare:", min_fare)
print("Total Fare:", total_fare)

# 24. Immutable Ticket Details(Tuple)

# Task:
# try modifying a tuple
# Observe and note the error 

ticket_details = ("PNR12345", "Express Train", "2024-07-15")
try:
    ticket_details[1] = "Superfast Train"  # Attempt to modify tuple    
except TypeError as e:
    print("Error:", e)
# Note: Tuples are immutable and cannot be modified.

# 25. Top 3  Most  Booked trains  
# Given List of  train bookings.

# Task: 
# Use List slicing
# isplay top  3  trains
train_bookings = ["Express Train", "Superfast Train", "Local Train", "Intercity Train", "Rajdhani Express"]
top_3_trains = train_bookings[:3]
print("Top 3 Most Booked Trains:", top_3_trains)