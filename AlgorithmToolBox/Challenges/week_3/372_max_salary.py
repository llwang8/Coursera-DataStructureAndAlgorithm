#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 3-7 Challenge: As the last question of a successful interview, your boss gives you a few pieces of paper with numbers on it and asks you to compose a largest number from these numbers. The resulting number is going to be your salary, so you are very much interested in maximizing this number. How can you do this?

Use greedy Algorithm
"""

def solve(digits):
    result = ''
    while len(digits) != 0:
        max_d = '0'
        for d in digits:
            if d + max_d > max_d + d:
                max_d = d
        result += max_d
        digits.remove(max_d)
    return result

if __name__ == '__main__':
    n = int(input())
    digits = input().split()
    print(solve(digits))
