#Factorial_calculator.py

def factorial(n):
    """Calculate factorial using recursion."""
    if n<0:
        return"Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
            return 1
    else:
            return n * factorial(n-1)

#sample call
number = 5
result = factorial(number)
print(f"the factorial of {number} is: {result}")