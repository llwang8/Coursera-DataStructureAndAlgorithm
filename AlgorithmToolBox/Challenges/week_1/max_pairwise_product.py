#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 1 Challenge: Max of pairwise product

"""


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max_num = numbers[0]
    sec_num = float('-inf')
    for i in range(1, n):
        if numbers[i] > max_num:
            sec_num = max_num
            max_num = numbers[i]
        elif numbers[i] > sec_num:
            sec_num = numbers[i]
    return max_num * sec_num


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
