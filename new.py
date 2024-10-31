
Input: list1 = [2, 7, 5, 64, 14]
Output: [7, 5]

Input: list2 = [12, 14, 95, 3, 73]
Output: [95, 3, 73]
# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 != 0:
       print(num, end=" ")
