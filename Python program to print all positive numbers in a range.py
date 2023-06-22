def print_positive_numbers(lst):
    positive_nums = [num for num in lst if num > 0]
    print("Output:", positive_nums)

# Test the function
list1 = [12, -7, 5, 64, -14]
print("Input:", list1)
print_positive_numbers(list1)

list2 = [12, 14, -95, 3]
print("Input:", list2)
print_positive_numbers(list2)
