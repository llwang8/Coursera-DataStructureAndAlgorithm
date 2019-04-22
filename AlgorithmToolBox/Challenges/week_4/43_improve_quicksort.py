#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 4-3 Improving Quick Sort

The goal in this problem is to redesign a given implementation of the random- ized quick sort algorithm so that it works fast even on sequences containing many equal elements.

"""
import sys
import random


def partition3(a, l, r):
    x = a[l]
    j = l
    s = l
    for i in range(l+1, r+1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    x = a[j]
    s = j
    for i in range(j+2, r+1):
        if a[i] == x:
            s += 1
            a[i], a[s] = a[s], a[i]
    a[j], a[s] = a[s], a[j]
    return j, s


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    j, s = partition3(a, l, r)
    randomized_quick_sort(a, l, j - 1);
    randomized_quick_sort(a, s, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n-1)
    for x in a:
        print(x, end=' ')





