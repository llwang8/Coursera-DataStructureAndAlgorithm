#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 4-1 Challenge: In this problem, you will implement the binary search algorithm that allows searching very efficiently (even huge) lists, provided that the list is sorted.

"""
def binarySearch(N, ai, k):
    #m = N // 2
    low = 0
    high = N - 1

    while low <= high:
        m = (low + high) // 2

        if k == ai[m]:
            return str(m)
        elif k < ai[m]:
            high = m - 1
        else:
            low = m + 1
        #print('l, m, h, k {} {} {} {}'.format(low, m, high, k))
    return str(-1)

if __name__ == '__main__':
    readline = input().split()
    N = int(readline[0])
    ai = list(map(int, readline[1:]))

    readline = input().split()
    K = int(readline[0])
    ki = list(map(int, readline[1:]))

    result = []
    for k in ki:
        result.append(binarySearch(N, ai, k))
    print(' '.join(result))



