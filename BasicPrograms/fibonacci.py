"""
Approach 1
Recursion.
Time: O(2^n)
Space: O(n)

Approach 2:
A form of dynamic programming. 
Time O(n)
Space O(1) for returning nth item of fibonacci series.
Space O(n) if we want to store the series. 
"""


# Approach 1: Recursion.
def fibonacci_using_recursion(n):
    # step2: define breaking conditions.

    if n <= 0:
        return "invalid input"
    if n == 1:
        return 0
    if n == 2:
        return 1
    # step 1: recursion series. 
    return fibonacci_using_recursion(n-1) + fibonacci_using_recursion(n-2)


def fibonacci_number_using_dynamic_programming(n):
    a, b = 0, 1

    if n == 0:
        return -1
    for i in range(0, n-1): # coz range returns 0 - n. so keeping last index to be n-1 so that loop runs n no of times.
        temp = b
        b = a + b
        a = temp
    return b


def fibonacci_series_using_dynamic_programming(n):
    fib_series = [0]
    a, b = 0, 1
    if n == 0:
        return -1
    for i in range (0, n-1):
        temp = b
        b = a + b
        a = temp
        fib_series.append(a)

    for item in fib_series:
        print(item, end=" ")

# recursive approach can also be optimized using memoization.
def fibonacci_series_using_recursion_with_memoization(n, mem = {}):
    if n in mem:
        return mem[n]
    elif n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        mem[n] = fibonacci_series_using_recursion_with_memoization(n-1, mem) + fibonacci_series_using_recursion_with_memoization(n-2, mem)
        return mem[n]

def fibonacci_series(n):
    def helper(n, series, current):
        if current < n:
            if current == 0:
                series.append(0)
            elif current == 1:
                series.append(1)
            else:
                series.append(series[-1] + series[-2])
            helper(n, series, current + 1)
        return series

    return helper(n, [], 0)

# Test

"""
while (True):
    n = int(input("Enter item:"))
    if (n == -1):
        break
    else:
        nth_item_in_series = fibonacci_number_using_dynamic_programming(n)
        print(nth_item_in_series)
# nth_item_in_series = fibonacci_using_recursion(5)

"""
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
#fibonacci_series_using_dynamic_programming(10)
fibonacci_series_using_recursion_with_memoization(10)
"""
Details of time complexity for recursive approach

Let's visualize the recursion tree for fibonacci_recursive(5):
                        F(5)
                       /    \
                    F(4)   F(3)
                   /   \    /   \
                F(3)  F(2) F(2) F(1)
               /   \   / \  / \
            F(2)  F(1) F(1) F(0) F(1) F(0)
           /   \
        F(1)  F(0)

Counting the Nodes
To understand why the time complexity is  𝑂(2^𝑛) consider the number of nodes (function calls) at each level of the recursion tree:

Level 0 (root level): 1 call (F(n))
Level 1: 2 calls (F(n-1) and F(n-2))
Level 2: 4 calls (two calls each for F(n-2) and F(n-3))
Level 3: 8 calls (each call from level 2 generates two more calls)
In general, at level 𝑘 there are 2^k calls. 

The depth of the tree (number of levels) is approximately 𝑛
leading to:

Total number of calls:  1 + 2 + 4 + 8 + …....2^(n−1)

This is a geometric series with the sum:

∑𝑘=0
𝑛−1 2^𝑘 = 2^𝑛 - 1

so time complexity is O(2^n)

"""