#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 4-5 organizing a lottery

You are organizing an online lottery. To participate, a person bets on a single integer. You then draw several ranges of consecutive integers at random. A participant’s payoff then is proportional to the number of ranges that contain the participant’s number minus the number of ranges that does not contain it. You need an efficient algorithm for computing the payoffs for all participants. A naive way to do this is to simply scan, for all participants, the list of all ranges. However, you lottery is very popular: you have thousands of participants and thousands of ranges. For this reason, you cannot afford a slow naive algorithm.
Problem Description
Task. You are given a set of points on a line and a set of segments on a line. The goal is to compute, for each point, the number of segments that contain this point.

"""
import sys



if __name__ == '__main__':
    s, p = list(map(int, sys.stdin.read().split()))
    segments = []
    for _ in range(s):
        segments.append(list(map(int, sys.stdin.read().split())))
    points = list(map(int, sys.stdin.read().split()))

    result = lottery(s, p, segments, points)
    for x in result:
        print(x, end='')



