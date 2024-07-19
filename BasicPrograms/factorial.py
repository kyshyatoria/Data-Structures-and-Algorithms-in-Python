def factorialRecursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorialRecursive(n-1)


def factorialIterative(n):
    if (n < 0):
        return 0
    if (n == 0 or n == 1):
        return 1
    
    result = 1
    while (n > 0):
        result = result * n
        n-=1
    return result


def factorialUsingBuiltIn(n):
    import math
    return math.factorial(n)

