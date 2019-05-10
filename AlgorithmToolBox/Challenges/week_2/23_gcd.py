#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 2-3 Challenge: Find GCD of two non-negative integers a, and b

Note: implement Euclidean Algorithm to find the GCD

"""

def gcd(a, b):
    """
    Implement Euclidean Algorithm to find the GCD
    """
    while (b > 0):
        if a > b:
            r = a%b
            a = b
            b = r
        else:
            r = b%a
            b = r
    return a

a, b = map(int, input().split())
print(gcd(a, b))


