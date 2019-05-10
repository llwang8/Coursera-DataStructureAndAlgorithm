#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 2-6 Challenge: Find the last digit of the sum of 0 to nth Fibonacci number

"""

def solve(n):
    if n < 1:
        return 0
    a, b = 0, 1
    result = 1
    for i in range(n-1):
        a, b = b, (a + b) % 10
        result += b
        result %= 10
        #print(result)
    return result

n = int(input())
print(solve(n%60))


