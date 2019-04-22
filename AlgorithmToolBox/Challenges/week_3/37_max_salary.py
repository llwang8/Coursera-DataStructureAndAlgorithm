#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 3-7 Challenge: As the last question of a successful interview, your boss gives you a few pieces of paper with numbers on it and asks you to compose a largest number from these numbers. The resulting number is going to be your salary, so you are very much interested in maximizing this number. How can you do this?

"""

def find_max(dlist):
    maxdigit = []
    alist, blist = [], []
    for d in dlist:
        if len(d) == 1:
            alist.append(d)
        else:
            blist.append(d)

    #for list with 1001, and 100 and 1 sort ascending, others descending
    if len(alist) == 0 and len(blist) == 0:
        return 0
    if blist:
        blist = sorted(blist, key=lambda x:x[1], reverse=True)
    if alist:
        if alist and alist[0][0] == 1:
            alist = sorted(alist)
        elif alist:
            alist = sorted(alist, reverse=True)

    if not alist:
        return ''.join(blist)
    if not blist:
        return ''.join(alist)

    a = alist.pop(0)
    b = blist.pop(0)

    while a and b:
        if a[0] >= b[1]:
            maxdigit.append(a)
            a = alist.pop(0) if len(alist) > 0 else ''
        else:
            maxdigit.append(b)
            b = blist.pop(0) if len(blist) > 0 else ''

    if a:
        maxdigit.append(a)
        maxdigit += alist
    if b:
        maxdigit.append(b)
        maxdigit += blist

    return ''.join(map(str, maxdigit))

def solve(digits):
    d_dict = {}
    result = ''

    for d in digits:
        if d[0] not in d_dict:
            d_dict[d[0]] = [d]
        else:
            d_dict[d[0]].append(d)
    sorted_keys = sorted(d_dict, reverse=True)

    for k in sorted_keys:
        cur = d_dict[k]
        cur_max = find_max(cur)
        result += cur_max

    return result

if __name__ == '__main__':
    n = int(input())
    digits = input().split()
    print(solve(digits))


