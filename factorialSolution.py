def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
number = 25 #This will not result in an error
result = factorial(number)
print(f"The factorial of {number} is {result}") 