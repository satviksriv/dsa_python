# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number.

from jovian.pythondsa import evaluate_test_cases

test_cases = []

test_cases.append({
    "input": {
        "nums": [5, 7, 7, 8, 8, 10],
        "target": 8
    },
    "output": [3, 4]
})

test_cases.append({
    "input": {
        "nums": [1, 2, 3, 4],
        "target": 3
    },
    "output": [2, 2]
})

def binary_search(low, high, condition):
    while low <= high:
        mid = (low + high) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            high = mid - 1
        elif result == "right":
            low = mid + 1
    return -1

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return "left"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return "right"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    output = []
    output.append(first_position(nums, target))
    output.append(last_position(nums, target))
    return output

evaluate_test_cases(first_and_last_position, test_cases)