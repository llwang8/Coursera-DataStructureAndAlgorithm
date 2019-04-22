#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 4-2 Challenge: Majority rule is a decision rule that selects the alternative which has a majority, that is, more than half the votes.
Given a sequence of elements 𝑎1, 𝑎2, . . . , 𝑎𝑛, you would like to check whether it contains an element that appears more than 𝑛/2 times.

"""
def solve(n, votes):
    tally = {}
    for vote in votes:
        if vote not in tally:
            tally[vote] = 1
        else:
            tally[vote] += 1
    vcounts = tally.values()
    #print(vcounts)
    for v in vcounts:
        if v > n/2:
            return 1
    return 0

def majority_element(a, l, r):
    if l == r:
        return -1
    if l + 1 == r:
        return a[l]

    m = (l + r) // 2
    leftM = majority_element(a, l, m)
    rightM = majority_element(a, m, r)
    print('leftM, rightM: {} {}'.format(leftM, rightM))

    left_count = 0
    for i in range(l, r):
        if a[i] == leftM:
            left_count += 1
    if left_count > (r-l) // 2:
        return leftM

    right_count = 0
    for i in range(l, r):
        if a[i] == rightM:
            right_count += 1
    if right_count > (r - l) // 2:
        return rightM

    print('left_count, right_count: {} {}'.format(left_count, right_count))

    return -1

if __name__ == '__main__':
    n = int(input())
    votes = input().split()

    print(solve(n, votes))
    #if majority_element(votes, 0, n) != -1:
    #    print(1)
    #else:
    #    print(0)


