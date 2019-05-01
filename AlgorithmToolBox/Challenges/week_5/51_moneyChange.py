#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 5-1 Money Change

As we already know, a natural greedy strategy for the change problem does not work correctly for any set of denominations. For example, if the available denominations are 1, 3, and 4, the greedy algorithm will change 6 cents using three coins (4 + 1 + 1) while it can be changed using just two coins (3 + 3). Your goal now is to apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4.

"""

def solve(n):
    coins = [1, 3, 4]
    min_changes = [None] * (n+1)
    min_changes[0] = 0

    for i in range(1, n+1):
        min_changes[i] = float('inf')
        for c in coins:
            if i >= c:
                temp = min_changes[i-c] + 1
                if temp < min_changes[i]:
                    min_changes[i] = temp
    return min_changes[n]


if __name__ == '__main__':
    n = int(input())
    print(solve(n))

