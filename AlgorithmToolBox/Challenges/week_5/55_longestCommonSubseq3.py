#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 5-5 Longest Common Subsequence of 3 sequences

Compute the length of a longest common subsequence of three sequences.

"""
def longest_comm_subseq_of2(n, m, p, a, b, c):
    if p == 0:
        for i in range(n+1):
            for j in range(m+1):
                if i == 0:
                    memo[i][j][0] = 0
                    elif j == 0:
                    memo[i][j][0] = 0
                elif a[i-1] == b[j-1]:
                    memo[i][j][0] = 1 + memo[i-1][j-1][0]
                else:
                    memo[i][j][0] = max(memo[i-1][j][0], memo[i][j-1][0], memo[i-1][j-1][0])
    if m == 0:
        for i in range(n+1):
            for j in range(p+1):
                if i == 0:
                    memo[i][0][j] = 0
                    elif j == 0:
                    memo[i][0][j] = 0
                elif a[i-1] == c[j-1]:
                    memo[i][0][j] = 1 + memo[i-1][0][j-1]
                else:
                    memo[i][0][j] = max(memo[i-1][0][j], memo[i][0][j-1], memo[i-1][0][j-1])

    if n == 0:
        for i in range(m+1):
            for j in range(p+1):
                if i == 0:
                    memo[0][i][j] = 0
                    elif j == 0:
                    memo[0][i][j] = 0
                elif b[i-1] == c[j-1]:
                    memo[0][i][j] = 1 + memo[0][i-1][j-1]
                else:
                    memo[0][i][j] = max(memo[0][i-1][j], memo[0][i][j-1], memo[0][i-1][j-1])


def longest_comm_subseq_of3(n, m, p, a, b, c):
    for i in range(n+1):
        for j in range(m+1):
            for k  in range(p+1)
                if k == 0:
                    if i == 0:
                        memo[i][j][0] = 0
                        elif j == 0:
                        memo[i][j][0] = 0
                    elif a[i-1] == b[j-1]:
                        memo[i][j][0] = 1 + memo[i-1][j-1][0]
                    else:
                        memo[i][j][0] = max(memo[i-1][j][0], memo[i][j-1][0], memo[i-1][j-1][0])
    return memo[i][j][]

if __name__ == '__main__':
    n = int(input())
    a = input().split()
    m = int(input())
    b = input().split()
    p = int(input())
    c = input().split(0)
    memo = [[[0 for h in range(p+1)] for c in range(m+1)] for r in range(n+1)]

    print(longest_comm_subseq3(n, m, p, a, b, c))
