#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 4-4 An inversion of a sequence 𝑎0,𝑎1,...,𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such that 𝑎𝑖 > 𝑎𝑗. The number of inversions of a sequence in some sense measures how close the sequence is to being sorted. For example, a sorted (in non-descending order) sequence contains no inversions at all, while in a sequence sorted in de- scending order any two elements constitute an inversion (for a total of 𝑛(𝑛 − 1)/2 inversions).

The goal in this problem is to count the number of inversions of a given sequence.


"""
import sys

def count_inversion(n, arr):
    counts = 0
    target = arr[-1]
    for i in range(n-1):
        #print(i)
        if arr[i] > target:
            counts += 1
        #print('i, counts: {} {}'.format(i, counts))
    return counts

def inversions(n, a):
    result = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            result += count_inversion(i+2, a[:i+2])
    return result


def merge(a, b, left, m, right):
    number_of_inversions = 0
    i = left
    j = m
    k = left
    #print('i, j, k: {} {} {}'.format(i, j, k))
    while i <= m-1 and j <= right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
            number_of_inversions += m - i
        k += 1

    while i <= m-1:
        b[k] = a[i]
        i += 1
        k += 1
    while j <= right:
        b[k] = a[j]
        j += 1
        k += 1
    for i in range(left, right+1):
        a[i] = b[i]
    return number_of_inversions

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right <= left:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave+1, right)
    #write your code here
    number_of_inversions += merge(a, b, left, ave+1, right)
    return number_of_inversions

if __name__ == '__main__':
    inputlines = sys.stdin.read().split()
    n, *a = list(map(int, inputlines))
    b = [0] * n
    #print(inversions(n, a))
    print(get_number_of_inversions(a, b, 0, len(a)-1))


