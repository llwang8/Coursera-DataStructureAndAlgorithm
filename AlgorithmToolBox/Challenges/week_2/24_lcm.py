#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 2-4 Challenge: Find LCM of two integers

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

def solve(a, b):
    return (a * b) // gcd(a, b)

a, b = map(int, input().split())
print(solve(a, b))
