#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 2-1 Challenge: Find nth Fibonacci number

"""

def memoize(func):
    memo = {}
    def inner(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return inner

@memoize
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
