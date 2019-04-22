#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 2-5 Challenge: You are responsible for collecting signatures from all tenants of a certain build- ing. For each tenant, you know a period of time when he or she is at home. You would like to collect all signatures by visiting the building as few times as possible.
The mathematical model for this problem is the following. You are given a set of segments on a line and your goal is to mark as few points on a line as possible so that each segment contains at least one marked point.rue in general: for any integer 𝑚 ≥ 2, the sequence 𝐹𝑛 mod 𝑚 is periodic. The period always starts with 0 1 and is known as Pisano period.

"""

def overlap(a1, b1, a2, b2):
    #print(a1, b1, a2, b2)
    if a2 <= b1:
        return [a2, min(b1, b2)]
    else:
        return -1

def solve1(n, segments):
    result = []
    #print(segments)
    segments = sorted(segments, key=lambda x:(x[0]))
    #print(segments)
    a = segments[0][0]
    b = segments[0][1]
    for i in range(1, n):
        an = segments[i][0]
        bn = segments[i][1]
        over = overlap(a, b, an, bn)
        #print(over)
        if over == -1:
            result.append(b)
            #print(result)
            a, b = an, bn
        else:
            a, b = over
    if over:
        result.append(b)
    return result

def solve(n, segments):
    segments = sorted(segments, key=lambda x:(x[0]))
    #print(segments)
    result = []
    max_right = segments[0][1]
    result.append(max_right)
    i = 1
    while i < n:
        if max_right < segments[i][0]:
            max_right = segments[i][1]
            result.append(max_right)
        i += 1
    return result

if __name__ == '__main__':
    n = int(input())
    segments = []
    for _ in range(n):
        segments.append(list(map(int, input().split())))
    result = list(map(str, solve1(n, segments)))
    print(len(result))
    print(' '.join(result))






