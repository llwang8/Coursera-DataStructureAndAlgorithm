#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 2-7 Challenge: Find the last digit of the sum of mth to nth Fibonacci number

The property that the last digit of the sum of 60 consecutive Fibonacci numbers is always 0.
"""

def solve(m, n):
    if n < 1:
        return 0
    fib_lastD = [0, 1]
    for i in range(2, 60):
        fib_lastD.append((fib_lastD[i-1] + fib_lastD[i-2]) % 10)

    rm = m % 60
    rn = n % 60
    if rm > rn:
        rn += 60
    result = 0
    for j in range(rm, rn+1):
        result += fib_lastD[j%60]
    return result%10

m, n = map(int, input().split())
print(solve(m, n))



