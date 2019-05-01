#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 5-2 Primitive Calculator

You are given a primitive calculator that can perform the following three operations with the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your goal is given a positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛 starting from the number 1.

"""

def make_div(n):
    def inner(x):
        return int(x/n)
    return inner

div2 = make_div(2)
div3 = make_div(3)


def solve(n):
    min_operations = [None] * (n+1)
    min_operations[0] = 0
    min_operations[1] = 0
    sequences = [[0], [1]]

    for i in range(2, n+1):
        temp = float('inf')
        temp2 = float('inf')
        temp3 = float('inf')
        if i % 3 == 0:
            temp3 = min_operations[div3(i)] + 1
        if i % 2 == 0:
            temp2 = min_operations[div2(i)] + 1
        temp1 = min_operations[i-1] + 1

        min_ops = min(temp1, temp2, temp3)
        min_operations[i] = min_ops

        if min_ops == temp3:
            sequences.append(sequences[div3(i)] + [i])
            continue
        if min_ops == temp2:
            sequences.append(sequences[div2(i)] + [i])
            continue
        if min_ops == temp1:
            sequences.append(sequences[i-1] + [i])
    #print(sequences)
    return (min_operations[n], sequences[n])


if __name__ == '__main__':
    n = int(input())
    result = solve(n)
    print(result[0])
    for x in result[1]:
        print(x, end=' ')


