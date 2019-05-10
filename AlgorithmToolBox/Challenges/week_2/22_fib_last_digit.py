#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 2-2 Challenge: Find the last digit of nth Fibonacci number

"""

def memoize(func):
    memo = {}
    def inner(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return inner

@memoize
def fib_lastDigit(n):
    if n <= 1:
        return n
    return (fib_lastDigit(n-1) + fib_lastDigit(n-2))%10

def solve(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append((f[i-1] + f[i-2]) % 10)
    return f[n]

n = int(input())
print(solve(n))
#print(fib_lastDigit(n))
