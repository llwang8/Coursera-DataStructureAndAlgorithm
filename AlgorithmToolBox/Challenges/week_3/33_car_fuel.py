#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 3-3 Challenge: You are going to travel to another city that is located 𝑑 miles away from your home city. Your can can travel at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at distances stop1, stop2, . . . , stop𝑛 from your home city. What is the minimum number of refills needed?

"""
def solve(d, m, n, stops):
    refills = 0
    start = 0
    stops.append(d)
    if stops[0] > m:
        return -1
    #print(stops)
    i = 0
    while i < n+1:
        #print("i, stops[i]: {} {}".format(i, stops[i]))
        #print("start: {}".format(start))
        if stops[i] - start > m:
            if start < stops[i-1]:
                start = stops[i-1]
                refills += 1
                i -= 1
                #print("i, start: {} {}".format(i, start))
            else:
                return -1
        i += 1
    return refills


if '__name__' == '__name__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))

    print(solve(d, m, n, stops))



