#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 5-2 Primitive Calculator

The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings. Edit distance has applications, for example, in computational biology, natural language processing, and spell checking. Your goal in this problem is to compute the edit distance between two strings.

"""
def solve_dp(str1, str2, n1, n2):
    memo = [[0 for y in range(n2+1)] for x in range(n1+1)]
    for i in range(n1+1):
        for j in range(n2+1):
            if i == 0:
                memo[i][j] = j
            elif j == 0:
                memo[i][j] = i
            elif str1[i-1] == str2[j-1]:
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = 1 + min(memo[i][j-1], memo[i-1][j], memo[i-1][j-1])
    return memo[n1][n2]

if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(solve_dp(str1, str2, len(str1), len(str2)))

