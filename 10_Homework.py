############################################ Task 1
def series_resistance(resistances):
    total_resistance = sum(resistances)
    return str(round(total_resistance)) + " ohms"
print(series_resistance([1,2.345454,3,4,5,6]))
############################################ /Task 1


############################################ Task 2
def number_split(num):
    half = num // 2
    return [half, num - half] if num % 2 == 0 else [half, half + 1]
print(number_split(6))
############################################ /Task 2


############################################ Task 3
def jazz(list):
    if not list:
        return []
    else:
        isjazz = []
        for word in list:
            if word.endswith("7"):
                isjazz.append(word)
            else:
                isjazz.append(word + "7")
    return isjazz
print(jazz(["G", "F", "FTV"]))
############################################ /Task 3


############################################ Task 4
def find_odd(list):
    out = 0
    for num in list:
        out **= num
    return out
print(find_odd([1,2,3,4,6,7,8,8,7,4,5,3,5,5,5]))
############################################ /Task 4


############################################ Task 5
def sum_odd_and_even(list):
    sum_even = 0
    sum_odd = 0
    for num in list:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    return(["Even", sum_even, "Odd", sum_odd])
print(sum_odd_and_even([1,2,3,4,5,6,7,8,9,10]))
############################################ /Task 5







