#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 5-4 Longest Common Subsequence of 2 sequences

Compute the length of a longest common subsequence of three sequences.

"""

def longest_comm_subseq_of2(n, m, a, b):
    memo = [[0 for c in range(m+1)] for r in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                memo[i][j] = 0
            elif j == 0:
                memo[i][j] = 0
            elif a[i-1] == b[j-1]:
                memo[i][j] = 1 + memo[i-1][j-1]
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])
    return memo[n][m]

if __name__ == '__main__':
    n = int(input())
    a = input().split()
    m = int(input())
    b = input().split()

    print(longest_comm_subseq2(n, m, a, b))

