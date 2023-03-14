                        # Four examples for Functions
# 1. 
num = -5
abs_num = abs(num)
print(abs_num)  # Output: 5

# 2. 
my_list = [10, 20, 30, 40, 50]
length = len(my_list)
print(length)  # Output: 5 

# 3 
my_tuple = (5, 10, 15, 20)
total = sum(my_tuple)
print(total)  # Output: 50

# 4 
my_list = [10, 30, 34, 56, 45]
sorted_list = sorted(my_list)
print(sorted_list)  # Output: 10, 30, 34, 45, 56

                        # Four examples for Functions
# 1 
def add_numbers(a, b):
    sum = a + b
    return sum
result = add_numbers(4, 45)
print("The sum of 5 and 7 is:", result)

# 2 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(4)
print("The factorial of 5 is:", result)

# 3 
def is_palindrome(s):
    return s == s[::-1]

result = is_palindrome("racecar")
print("Is this palindrome?:", result)

# 4
def rectangle_area_perimeter(lenght, width):
    area = lenght * width
    perimeter = 2 * (lenght + width)
    return (area, perimeter)
result = rectangle_area_perimeter(3, 4)
print("The area and perimeter of a 5 by 3 rectangle are:", result)

                        ################### Task 1
def text(Assalom):
    return Assalom[::-1]

result = text("Assalom")
print(result)

                        ################### Task 2
def extract_numbers(text):
    numbers = "".join(filter(str. isdigit, text))
    return numbers
input_text = "uzgfh45kjjdj345jjg5"
output_text = extract_numbers(input_text)
print(output_text)

                        ################### Task 3
def replace_python_with_java(text):
    return text.replace("Python", "JavaScript")
input_text = "Python is most popular programming language"
output_text = replace_python_with_java(input_text)
print(output_text)
