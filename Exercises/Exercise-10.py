# Functions  part-( Builtin Functions)
# 1. Write a program to find the longest word in a given sentence using built-in functions.
def find_longest_word(sentence):
    words = sentence.split()  # Split the sentence into words
    longest_word = max(words, key=len)  # Find the longest word using max with key=len
    return longest_word
# Example usage
sentence = "The quicks brown fox jumps over the lazy dog"
longest_word = find_longest_word(sentence)
print("The longest word is:", longest_word)

# 2. Find the maximum occurring element in a list using Python’s built-in functions.
def find_max_occurring_element(lst):
    max_element = max(set(lst), key=lst.count)  # Use max with set and count to find the max occurring element
    return max_element
# Example usage
lst = [1, 3, 2, 1, 4, 1, 3, 2, 1]
max_occurring_element = find_max_occurring_element(lst)
print("The maximum occurring element is:", max_occurring_element)

# 3. Use map() to convert a list of temperatures from Celsius to Fahrenheit.  use the build in function map()
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Conversion formula

celsius_temperatures = [0, 20, 30, 40]
fahrenheit_temperatures = list(map(celsius_to_fahrenheit, celsius_temperatures))
print("Temperatures in Fahrenheit:", fahrenheit_temperatures)

# 4.Count how many unique vowels are present in a given string using set() and len().
def count_unique_vowels(input_string):
    vowels = set('aeiouAEIOU')  # Define a set of vowels
    unique_vowels = set(char for char in input_string if char in vowels)  # Use set comprehension to find unique vowels
    return len(unique_vowels)  # Return the count of unique vowels
# Example usage
input_string = "Hello World, this is a sample string."
unique_vowel_count = count_unique_vowels(input_string)
print("Number of unique vowels:", unique_vowel_count)
print("Show the vowels:", set(char for char in input_string if char in set('aeiouAEIOU')))

# 5. Write a program to convert a dictionary into a list of tuples and back to a dictionary.
def dict_to_tuples_and_back(input_dict):
    # Convert dictionary to list of tuples
    tuples_list = list(input_dict.items())
    # Convert list of tuples back to dictionary
    converted_dict = dict(tuples_list)
    return tuples_list, converted_dict
# Example usage
input_dict = {'a': 1, 'b': 2, 'c': 3}
tuples_list, converted_dict = dict_to_tuples_and_back(input_dict)
print("List of tuples:", tuples_list)
print("Converted back to dictionary:", converted_dict)

# 6. Sort a list of tuples by the second value using sorted().
def sort_tuples_by_second_value(tuple_list):
    return sorted(tuple_list, key=lambda x: x[1])
# Example usage
tuple_list = [('a', 3), ('b', 1), ('c', 2)]
sorted_tuples = sort_tuples_by_second_value(tuple_list)
print("Sorted tuples by second value:", sorted_tuples)

# 7. Merge two lists into a dictionary using zip().
def merge_lists_to_dict(keys, values):
    return dict(zip(keys, values))  # Use zip to merge lists into a dictionary
# Example usage
keys = ['a', 'b', 'c']
values = [1, 2, 3]
merged_dict = merge_lists_to_dict(keys, values)
print("Merged dictionary:", merged_dict)

# 8. Find the second largest number in a list using built-in functions.
def find_second_largest_number(num_list):
    unique_numbers = set(num_list)  # Remove duplicates by converting to a set
    unique_numbers.remove(max(unique_numbers))  # Remove the largest number
    second_largest = max(unique_numbers)  # The next max is the second largest
    return second_largest 
# Example usage
num_list = [4, 1, 7, 3, 9,7, 9, 2]
second_largest = find_second_largest_number(num_list)
print("The second largest number is:", second_largest)

# 9. Use filter() to get all prime numbers from a given list.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def get_prime_numbers(num_list):
    return list(filter(is_prime, num_list))  # Use filter with is_prime function
# Example usage
num_list = [10, 15, 3, 7, 8, 11, 13]
prime_numbers = get_prime_numbers(num_list)
print("Prime numbers in the list:", prime_numbers)

# 10. Write a program to remove all duplicates from a list using set().
def remove_duplicates(input_list):
    return list(set(input_list))  # Convert to set and back to list to remove duplicates    
# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(input_list)
print("List after removing duplicates:", unique_list)

# 11. Use enumerate() to display index and value of each character in a string.
def display_index_and_value(input_string):
    for index, value in enumerate(input_string):
        print(f"Index: {index}, Value: {value}") 
# Example Usage
input_string = "Hello"
display_index_and_value(input_string)

# 12. Find the average salary from a list of employee salaries using sum() and len().
def calculate_average_salary(salary_list):
    return sum(salary_list) / len(salary_list)  # Calculate average using sum and len
# Example usage
salary_list = [50000, 60000, 55000, 70000]
average_salary = calculate_average_salary(salary_list)
print("The average salary is:", average_salary)

# 13.Sort dictionary items by values in descending order using sorted().
def sort_dict_by_values_desc(input_dict):
    return dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))
# Example usage
input_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = sort_dict_by_values_desc(input_dict)
print("Dictionary sorted by values in descending order:", sorted_dict)

# 14. Use all() and any() to check if all students passed in a given list of marks.
def check_students_passed(marks_list, passing_mark):
    all_passed = all(mark >= passing_mark for mark in marks_list)
    any_passed = any(mark >= passing_mark for mark in marks_list)
    return all_passed, any_passed
# Example usage
marks_list = [45, 67, 89, 34, 56]
passing_mark = 40
all_passed, any_passed = check_students_passed(marks_list, passing_mark)
print("All students passed:", all_passed)
print("Any student passed:", any_passed)

#15. Write a program to flatten a 2D list using built-in functions.
def flatten_2d_list(two_d_list):
    return [item for sublist in two_d_list for item in sublist]  # List comprehension to flatten the list 
# Example usage
two_d_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = flatten_2d_list(two_d_list)
print("Flattened list:", flattened_list)

# 16. Find the total marks of students using map() and sum().
def total_marks(marks_list):
    return sum(map(int, marks_list))  # Use map to convert to int and sum to get total
# Example usage
marks_list = ['45', '67', '89', '34', '56']
total = total_marks(marks_list)
print("Total marks of students:", total)

# 17. Write a program to find the intersection of two lists using built-in functions
def find_intersection(list1, list2):
    return list(set(list1) & set(list2))  # Use set intersection to find common elements    
# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = find_intersection(list1, list2)
print("Intersection of the two lists:", intersection)

# 18. Find the most frequent character in a given string using built-in functions.
def most_frequent_character(input_string):
    return max(set(input_string), key=input_string.count)  # Use max with set and count to find the most frequent character
# Example usage
input_string = "hello world"
most_frequent_char = most_frequent_character(input_string)
print("The most frequent character is:", most_frequent_char)

# 19. Use max() with key function to find the longest word in a list.
def find_longest_word(word_list):
    return max(word_list, key=len)  # Use max with key=len to find the longest word
# Example usage
word_list = ["apple", "banana", "cherry", "watermelon"]
longest_word = find_longest_word(word_list)
print("The longest word is:", longest_word)

# 20. Write a program to group students based on marks using dict() and zip().
def group_students_by_marks(names, marks):
    return dict(zip(names, marks))  # Use zip to group names and marks into a dictionary
# Example usage
names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]
grouped_students = group_students_by_marks(names, marks)
print("Grouped students by marks:", grouped_students)


# 21. Use filter() to remove all words shorter than 4 letters from a list.
def remove_short_words(word_list):
    return list(filter(lambda word: len(word) >= 4, word_list))  # Use filter with lambda to remove short words 
# Example usage
word_list = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
filtered_words = remove_short_words(word_list)
print("Words with 4 or more letters:", filtered_words)

# 22. Write a program to rotate elements of a list using slicing and built-in functions.
def rotate_list(lst, n):
    n = n % len(lst)  # Handle rotation greater than list length
    return lst[-n:] + lst[:-n]  # Use slicing to rotate the list
# Example usage 
lst = [1, 2, 3, 4, 5]
n = 2
rotated_list = rotate_list(lst, n)
print("Rotated list:", rotated_list)

# 23. Find the median of a list using built-in functions.
def find_median(num_list):
    sorted_list = sorted(num_list)  # Sort the list
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2  # Average of two middle numbers for even length
    else:
        median = sorted_list[mid]  # Middle number for odd length
    return median
# Example usage
num_list = [3, 1, 4, 2, 5]
median = find_median(num_list)
print("The median is:", median)

# 24. Write a program to find employees with salary above 50,000 using filter().
def filter_high_salary(employees):
    return list(filter(lambda emp: emp['salary'] > 50000, employees))  # Use filter with lambda to find high salary employees
# Example usage
employees = [
    {'name': 'Alice', 'salary': 60000},
    {'name': 'Bob', 'salary': 45000},
    {'name': 'Charlie', 'salary': 52000}
]
high_salary_employees = filter_high_salary(employees)
print("Employees with salary above 50,000:", high_salary_employees)

# 25. Use map() and lambda to square each element in a list.

def square_elements(num_list):
    return list(map(lambda x: x**2, num_list))  # Use map with lambda to square each element
# Example usage
num_list = [1, 2, 3, 4, 5]  
squared_list = square_elements(num_list)
print("Squared elements:", squared_list)










