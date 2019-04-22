#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 2-5 Challenge: Find reminder of nth Fib mod by m
This is true in general: for any integer 𝑚 ≥ 2, the sequence 𝐹𝑛 mod 𝑚 is periodic. The period always starts with 0 1 and is known as Pisano period.

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

def solve(n, m):
    fib_mod = [0, 1, 1]
    if n <= 3:
        return fib_mod[n]
    for i in range(3, n+1):
        fib_mod.append(calc_fib(i)%m)
        if fib_mod[-1] == 1 and fib_mod[-2] == 0:
            break
    #print(fib_mod)
    fib_len = len(fib_mod)-2
    r = n % fib_len
    return fib_mod[r]

n, m = map(int, input().split())
print(solve(n, m))


