#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 6-3 Partitionin Souvenirs

In this problem, your goal is to add parentheses to a given arithmetic expression to maximize its value.
: max(5−8+7×4−8+9) =?

"""
def max_arithmatic_expr(numbers, operations):
    length = len(numbers)
    maxm = [[None for j in range(length)] for i in range(length)]
    minm = [[None for j in range(length)] for i in range(length)]

    for i in range(length-1, -1, -1):
        for j in range(i, length-1):
            if numbers[i] == numbers[j]:
                maxm[i][j] = numbers[i]
                minm[i][j] = numbers[i]
            else:
                k = i
                max_r = float('-inf')
                min_r = float('inf')
                for k in range(i, j+1):
                    maxtemp = max(eval(maxm[i][k] + operations[i] + maxm[k][j]), eval(maxm[i][k] + operations[i] + minm[k][j]),
                        eval(minm[i][k] + operations[i] + maxm[k][j]),
                        eval(minm[i][k] + operations[i] + minm[k][j]),)
                    mintemp = min(eval(maxm[i][k] + operations[i] + maxm[k][j]), eval(maxm[i][k] + operations[i] + minm[k][j]),
                        eval(minm[i][k] + operations[i] + maxm[k][j]),
                        eval(minm[i][k] + operations[i] + minm[k][j]),)
                    if maxtemp > max_r:
                        max_r = maxtemp
                    if mintemp < min_r:
                        min_r = mintemp
                maxm[i][j] = max_r
                minm[i][j] = min_r

    return max_memo[0][length-1]


if __name__ == '__main__':
    expression = input()

    length = len(expression)
    numbers = [expression[i] for i in range(0, length, 2)]
    operations = [expression[j] for j in range(1, length, 2)]
    print(max_arithmatic_expr(numbers, operations))

