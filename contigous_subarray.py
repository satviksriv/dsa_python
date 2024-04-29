from jovian.pythondsa import evaluate_test_cases

test_cases = []

test_cases.append({
    "input": {
        "array": "2 3 5 1 4",
        "k": 2
    },
    "output": [3, 5, 5, 4]
})

test_cases.append({
    "input": {
        "array": "7 4 2 1 6 3",
        "k": 3
    },
    "output": [7, 4, 6, 6]
})

def contigous_subarray(array, k):
    # Converting string into integer list
    array = list(str.split(array, " "))
    for i in range(0, len(array)):
        array[i] = int(array[i])
    
    # Calculating size of list
    n = len(array)
    
    # Calculating max element of possible subarray of size k
    output = []
    for i in range(0, n-k+1):
        subarray = []
        temp = k
        while temp>0:
            subarray.append(array[i])
            i += 1
            temp -= 1
        largest = max(subarray)
        output.append(largest)
    
    # Returning output
    return output

evaluate_test_cases(contigous_subarray, test_cases)