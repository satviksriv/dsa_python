'''
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].
'''

'''
Input:
    list
Output:
    number of rotations
'''

from jovian.pythondsa import evaluate_test_cases

# Function to calculate no of required rotations
def count_rotations(list):
    sorted_list = sorted(list)
    print("Given list = {}, Sorted list = {}".format(list, sorted_list))
    size = len(sorted_list)
    count = 0
    for i in range(size):
        if list == sorted_list:
            return count
        temp = list[0]
        list.append(temp)
        list.pop(0)
        print(list)
        count += 1
    return count

# List of test cases
test_cases = []

# Random list
test_cases.append({
    "input": {
        "list": [5, 6, 9, 0, 2, 3, 4]
    },
    "output": 3
})

# If given list == original list
test_cases.append({
    "input": {
        "list": [1, 2, 3, 4, 5, 6]
    },
    "output": 0
})

test_cases.append({
    "input": {
        "list": [4, 1, 2, 3]
    },
    "output": 1
})

evaluate_test_cases(count_rotations, test_cases)