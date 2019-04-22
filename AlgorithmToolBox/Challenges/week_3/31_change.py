#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 3 - 1 Challenge: In this problem, you will design and implement an elementary greedy algorithm used by cashiers all over the world millions of times per day.  The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.

"""

def solve(n):
    deno = [10, 5, 1]
    result = 0
    for d in deno:
        if n < d:
            continue
        q = n // d
        result += q
        n %= d
    return result

if __name__ == '__main__':
    n = int(input())
    print(solve(n))