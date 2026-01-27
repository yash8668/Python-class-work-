#Q1. Number Increasing Triangle
from tkinter import Grid


from tkinter import Grid


n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

#Instructions:

#a. Outer loop for rows (1 to n).
#b. Inner loop prints numbers from 1 to row number.

#Q2. Number Decreasing Triangle
n = 5 
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()



#Instructions:

#a. Outer loop decreases row size each time.
#b. Inner loop prints numbers in decreasing order.


#Q3. Constant Number Triangle
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(i, end=' ')
    print()



#Instructions:

#a. Outer loop runs from n down to 1.
#b. Inner loop prints same number as row value.


#Q4. Left Aligned Decreasing Numbers
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


#Instructions:

#a. Outer loop decreases length each row.
#b. Inner loop prints numbers starting from 1.


#Q5. Repeating Number Pyramid
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=' ')
    print()


#Instructions:

#a. Outer loop for rows.
#b. Inner loop prints row number repeatedly.


#Q6. Reverse Repeating Numbers
n = 5
for i in range(n, 0, -1):
    for j in range(1, n - i + 2):
        print(i, end=' ')
    print()


#Instructions:

#a. Outer loop from n down to 1.
#b. Inner loop prints row number repeatedly.


#Q7. Reverse Counting Pyramid
n = 5
for i in range(1, n + 1):
    for j in range(n, n - i, -1):
        print(j, end=' ')
    print()

#Instructions:

#a. Outer loop for rows.
#b. Inner loop prints decreasing numbers starting from 5.


#Q8. Centered Number Pyramid
n = 5
for i in range(1, n + 1):
    print("  " * (n - i), end='')  # Print leading spaces
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

#nstructions:

#a. Manage spaces before numbers.
#b. Print increasing sequence on each row.


#Q9. Centered Repeating Number Pyramid
n = 5  
for i in range(1, n + 1):
    print("  " * (n - i), end='')  # Print leading spaces
    for j in range(1, i + 1):
        print(i, end=' ')
    print()

#Instructions:

#a. Outer loop for rows.
#b. Print spaces for alignment then repeat row number.


#Q10. Reverse Number Triangle (Centered)
n = 5
for i in range(1, n + 1):
    print("  " * (n - i), end='')  # Print leading spaces
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

#Instructions:

#a. Spaces before numbers.
#b. Print numbers in reverse order per row.


#Q11. Number Triangle with Reverse Order
n = 5
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()



#Instructions:

#a. Outer loop for rows.
#b. Inner loop counts down from row number to 1.


#Q12. Continuous Numbers
n = 4
counter = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(counter, end=' ')
        counter += 1
    print()

#Instructions:

#a. Maintain a counter variable.
#b. Print sequential numbers row-wise.


#Q13. Continuous Numbers (Odd Row Expansion)
n = 3
counter = 1
for i in range(1, n + 1):
    for j in range(1, 2*i):
        print(counter, end=' ')
        counter += 1
    print()

#Instructions:

#a. Counter variable increases continuously.
#b. Row size grows in odd numbers.


#Q14. Multiplication Table Pattern

n = 5
for i in range(n):
    for j in range(i + 1):
        print(i * j, end=' ')
    print()

#Instructions:

#a. Outer loop for rows.
#b. Inner loop prints row*col value.


#15. Square Numbers Pattern

n = 5
for i in range(n):
    for j in range(i + 1):
        print(j * j, end=' ')
    print()

#Instructions:

#a. Outer loop for rows.
#b. Inner loop prints squares of column index.


#Q16. Repeated Square Numbers

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i * i, end=' ')
    print() 

#Instructions:

#a. Outer loop row number squared.
#b. Repeat the value as per row index.


#Q17. Odd Numbers Triangle

n = 5
odd_num = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(odd_num, end=' ')
    print()
    odd_num += 2

#Instructions:

#a. Generate odd numbers.
#b. Repeat number equal to row count.


#Q18. Star Right Triangle

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('*', end=' ')
    print()

#Instructions:

#a. Outer loop rows.
#b. Inner loop prints '*' as per row count.


#Q19. Star Inverted Triangle

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

#Instructions:

#a. Outer loop rows decreasing.
#b. Inner loop prints '*' count decreasing.


#Q20. Star Pyramid

n = 5
for i in range(1, n + 1):   
    print("  " * (n - i), end='')  # Print leading spaces
    for j in range(1, i + 1):
        print('*', end=' ')
    print()

#Instructions:

#a. Print spaces for alignment.
#b. Print stars equal to row index.


#Q21. Square Numbers Grid

n = 5
for i in range(1, n + 1):   
    for j in range(1, n + 1):
        print(j, end=' ')
    print()

#Instructions:

#a. Outer loop rows.
#b. Inner loop prints 1 to n each row.


#Q22. Square Repeated Numbers

n = 5
for i in range(1, n + 1):   
    for j in range(1, n + 1):
        print(i, end=' ')
    print()

#Instructions:

#a. Outer loop rows.
#b. Inner loop prints row number repeatedly.


#Q23. Alphabet Pyramid (Increasing)

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=' ')
    print()

#Instructions:

#a. Use ASCII values with chr().
#b. Print increasing letters each row.


#Q24. Alphabet Pyramid (Repeating Letters)

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + i), end=' ')
    print()

#Instructions:

#a. Row number determines letter.
#b. Repeat letter as per row index.


#Q25. Butterfly Pattern

# Number of rows for half pattern
n = 5

# ---------- Upper Half ----------
for i in range(1, n + 1):
    stars = "*" * i
    spaces = " " * (2 * (n - i) - 1)
    print(stars + spaces + stars)

# ---------- Lower Half ----------
for i in range(n - 1, 0, -1):
    stars = "*" * i
    spaces = " " * (2 * (n - i) - 1)
    print(stars + spaces + stars)

#Instructions:

#a. Print stars on both sides with spaces in between.
#b. Maintain symmetry in upper and lower half.