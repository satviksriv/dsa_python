from jovian.pythondsa import evaluate_test_cases

test_cases = []

test_cases.append({
    "input": {
        "n": 153
    },
    "output": "Yes"
})

test_cases.append({
    "input": {
        "n": 372
    },
    "output": "No"
})

def check_armstrong(n):
    digit_count = len(str(n))
    armstrong = 0
    temp = n
    while(digit_count!=0):
        last_digit = temp%10
        print("Last digit = ", last_digit)
        armstrong = armstrong + (last_digit*last_digit*last_digit)
        print("Sum of cubes of digits = ", armstrong)
        temp = temp//10
        digit_count -= 1
    if armstrong == n:
        return "Yes"
    else:
        return "No"
    
evaluate_test_cases(check_armstrong, test_cases)