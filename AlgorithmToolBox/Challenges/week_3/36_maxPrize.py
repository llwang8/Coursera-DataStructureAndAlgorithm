#python3

"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 2-5 Challenge: You are organizing a funny competition for children. As a prize fund you have 𝑛 candies. You would like to use these candies for top 𝑘 places in a competition with a natural restriction that a higher place gets a larger number of candies. To make as many children happy as possible, you are going to find the largest value of 𝑘 for which it is possible.

"""

def solve(n):
    if n == 1:
        return ['1']
    prizes = []
    r = n
    p = 1
    while p < n:
        r = r - p
        if p < r:
            prizes.append(p)
            p += 1
            #print(p)
        else:
            if r == 0:
                prizes.append(p)
            else:
                prizes.append(r + p)
            break
    prizes = [str(x) for x in prizes]
    return prizes

if __name__ == '__main__':
    n = int(input())
    result = solve(n)
    print(len(result))
    print(' '.join(result))

