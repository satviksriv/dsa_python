from jovian.pythondsa import evaluate_test_cases, evaluate_test_case
'''
Question: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

Answer:
Todo:
    1. Find the index of the given element.
    2. Find it in the least number of ways.
Input:
    1. cards: List of numbers arranged in descending order.
    2. element: A number whose position or index is to be determined.
Output:
    1. position/index: Position of the given element.
'''

# Signature of our function
# Binary Search
def test_location(cards, element, middle_index):
    if cards[middle_index] == element:
        if middle_index-1 >= 0 and cards[middle_index-1] == element:
            return "left"
        else:
            return "found"
    elif cards[middle_index] < element:
        return "left"
    else:
        return "right"

def locate_card(cards, element):
    low, high = 0, len(cards) - 1

    while low <= high:
        middle_index = (low + high) // 2
        result = test_location(cards, element, middle_index)

        if result == "found":
            return middle_index
        elif result == "left":
            high = middle_index - 1
        elif result == "right":
            low = middle_index + 1

    return -1



'''
Test Cases:
    1. Element is in the middle of the list
    2. Element is somewhere in the middle of the list
    3. Element is the first element
    4. Element is the last element
    5. List contains only element
    6. List does not contain the element
    7. List is empty
    8. List contains repeating numbers
    9. List contains the element multiple number of times
'''

# List containing test cases
tests = []

# Element is in the middle
tests.append({
    "input": {
        "cards": [14, 13, 12, 7, 4, 3, 2],
        "element": 7
    },
    "output": 3
})

# Element is somewhere in the middle
tests.append({
    "input": {
        "cards": [14, 13, 7, 5, 4, 3, 1],
        "element": 7
    },
    "output": 2
})

# Element is first
tests.append({
    "input": {
        "cards": [7, 5, 4, 3, 1],
        "element": 7
    },
    "output": 0
})

# Element is last
tests.append({
    "input": {
        "cards": [14, 13, 7, 5, 4, 3, 1],
        "element": 1
    },
    "output": 6
})

# List contains only element
tests.append({
    "input": {
        "cards": [7],
        "element": 7
    },
    "output": 0
})

# List does not contain the element
tests.append({
    "input": {
        "cards": [14, 13, 5, 4, 3, 1],
        "element": 7
    },
    "output": -1
})

# List is empty
tests.append({
    "input": {
        "cards": [],
        "element": 7
    },
    "output": -1
})

# List contains repeating numbers
tests.append({
    "input": {
        "cards": [14, 13, 13, 7, 5, 5, 4, 3, 1],
        "element": 7
    },
    "output": 3
})

# List contains element multiple number of times
tests.append({
    "input": {
        "cards": [14, 13, 7, 7, 7, 5, 4, 3, 1],
        "element": 7
    },
    "output": 2
})

'''
Brute force solution (Linear Search):
    1. Create a variable position with value 0.
    2. Check whether cards[position] == element.
    3. If it does, return position.
    4. Else, position += 1, repeat step 2 to 4 until we reach the end of the list.
    5. Return -1
'''

'''
Binary Search:
    1. Find the middle element of the list.
    2. If middle element == element, return its position.
    3. If it is less than the required number, search in the first half.
    4. If it is greater than the required number, search in the second half.
    5. If no more elements remain, return -1
'''

evaluate_test_cases(locate_card, tests)

'''
Time complexity = O(log N)
Space complexity = O(1)
'''