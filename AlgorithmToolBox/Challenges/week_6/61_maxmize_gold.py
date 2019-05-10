#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 6-1 Maximize Gold

You are given a set of bars of gold and your goal is to take as much gold as possible into your bag. There is just one copy of each bar and for each bar you can either take it or not (hence you cannot take a fraction of a bar).

"""
def maxmize_gold_gd(W, n, weights):
    memo = [0 for i in range(W+1)]
    j = 0
    for i in range(1, W+1):
        j = n - 1
        while j > 0:
            if weights[j] <= i - memo[i]:
                memo[i] += weights[i]
            j -= 1
    return memo[n]


def maxmize_gold_dp(Cap, n, weights):
    memo = [[0 for c in range(Cap+1)] for w in range(n+1)]
    #print(memo)

    for i in range(1, n+1):
        w = weights[i-1]
        #print(w)
        for c in range(0, Cap+1):
            if w > c:
                memo[i][c] = memo[i-1][c]
            else:
                p1 = memo[i-1][c]
                p2 = memo[i-1][c-w] + w
                memo[i][c] = max(p1, p2)
    return memo[n][Cap]



if __name__ == '__main__':
    Cap, n = map(int, input().split())
    weights = list(map(int, input().split()))

    print(maxmize_gold_dp(Cap, n, weights))


