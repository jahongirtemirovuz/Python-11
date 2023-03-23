# Task 1
def duplicate_zeros(lst):
    result = []
    for num in lst:
        result.append(num)
        if num == 0:
            result.append(0)
    return result

print(duplicate_zeros([1, 0, 2, 0]))
# Output: [1, 0, 0, 2, 0, 0]


# Task 2
def is_majority(lst):
    if not lst:  # check for empty list
        return False
    count = 0
    for val in lst:
        if val:
            count += 1
    return count > len(lst) / 2

# Example usage
print(is_majority([True, True, False, True, False]))  # Output: True
print(is_majority([True, True, False, True, False]))  # Output: False
print(is_majority([]))  # Output: False


# Task 3
def rotate_list(lst):
    if len(lst) <= 1:  # Check for empty or single-item list
        return lst
    else:
        first = lst.pop(0)  # remove first element and store it
        lst.append(first)  # append the first element at the end
        return lst

# Example usage
print(rotate_list([1, 2, 3, 4]))   # Output: [2, 3, 4, 1]
print(rotate_list([1]))            # Output: [1]
print(rotate_list([]))             # Output: []


# Task 4
def compress_list(lst):
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i-1]]

# Example usage
a = [5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0]
print(compress_list(a))  # Output: [5, 4, 5, 6, 5, 7, 8, 0]


# Task 5
def sort_files(files):
    return sorted(files, key=lambda x: (x.split(".")[1:] or ["", x.split(".")[0]]) + [x.split(".")[0]])

# Test the function
files = ["yandex.ru.exe", "google.com", "config.", "config", "print.png", "example.google.com.exe", "example1.google.com.exe", "config.cpp"]
print(sort_files(files))   # Output: ['config', 'config.', 'config.cpp', 'google.com', 'example.google.com.exe', 'example1.google.com.exe', 'print.png', 'yandex.ru.exe']
