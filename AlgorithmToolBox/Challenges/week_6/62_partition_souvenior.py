# python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 6-2 Partitionin Souvenirs

You and two of your friends have just returned back home after visiting various countries. Now you would like to evenly split all the souvenirs that all three of you bought.

"""
def partition(n, souvenirs):
    if n < 3:
        return 0
    total = sum(souvenirs)
    if total % 3 != 0:
        return 0

    m = int(total / 3)
    memo = [[0 for j in range(m+1)] for s in souvenirs]
    for i in range(n):
        for j in range(m+1):
            if j == 0:
                memo[i][j] = 1
            elif souvenirs[i] > j:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = memo[i-1][j] or memo[i-1][j-souvenirs[i]]

    return memo[n-1][m]


if __name__ == '__main__':
    n = int(input())
    souvenirs = list(map(int, input().split()))
    print(partition(n, souvenirs))


