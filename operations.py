def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    if (b!=0):
        return a/b
    else:
       raise ValueError("Cannot divide by zero!")

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def power(base, exponent):
    if exponent < 0:
        raise ValueError("Negative exponents are not supported")
    elif exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)