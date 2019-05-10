#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 2-5 Challenge: Find reminder of nth Fib mod by m
This is true in general: for any integer 𝑚 ≥ 2, the sequence 𝐹𝑛 mod 𝑚 is periodic. The period always starts with 0 1 and is known as Pisano period.

"""

def get_pisano_period(m):
    if m == 2:
        return 3
    a, b, c = 0, 1, 1
    i = 3
    while True:
        a, b, c = b, c, (b+c)%m
        if a == 0 and b == 1:
            #print(i-2)
            return i-2
        i += 1


def solve(n, m):
    fib_mod = [0, 1, 1]
    if m <= 2:
        fib_len = 3
    else:
        for i in range(3, n+1):
            fib_mod.append(calc_fib(i)%m)
            if fib_mod[-1] == 1 and fib_mod[-2] == 0:
                break
        #print(fib_mod)
        fib_len = len(fib_mod)-2
    r = n % fib_len
    return fib_mod[r]


def solve2(n, m):
    reminder = n % get_pisano_period(m)
    #print('reminde: {}'.format(reminder))
    if reminder == 0:
        return 0
    a, b = 0, 1
    for i in range(1, reminder):
        a, b = b, (a+b)%m
    return b%m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve2(n, m))

