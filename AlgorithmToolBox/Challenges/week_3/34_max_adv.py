#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 3-4 Challenge: You have 𝑛 ads to place on a popular Internet page. For each ad, you know how much is the advertiser willing to pay for one click on this ad. You have set up 𝑛 slots on your page and estimated the expected number of clicks per day for each slot. Now, your goal is to distribute the ads among the slots to maximize the total revenue.

Given two sequences 𝑎1,𝑎2,...,𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1,𝑏2,...,𝑏𝑛 (𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot), we need to partition them into 𝑛 pairs (𝑎𝑖,𝑏𝑗) such that the sum of their products is maximized.

"""
def solve(n, vals, clicks):
    vals = sorted(vals)
    clicks = sorted(clicks)
    result = [vals[i]*clicks[i] for i in range(n)]
    return sum(result)


if __name__ == "__main__":
    n = int(input())
    vals = list(map(int, input().split()))
    clicks = list(map(int, input().split()))

    print(solve(n, vals, clicks))