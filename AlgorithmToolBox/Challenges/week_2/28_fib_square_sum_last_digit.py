#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 2-8 Challenge: Find the last digit of the sum of n Fibonacci number square

"""

def solve(n):
    if n < 1:
        return 0
    fib_lastD = [0, 1]
    for i in range(2, 60):
        fib_lastD.append((fib_lastD[i-1] + fib_lastD[i-2]) % 10)

    rn = n % 60
    result = 0
    for j in range(rn+1):
        result += fib_lastD[j] **2 % 10
    return result%10

n = int(input())
print(solve(n))

