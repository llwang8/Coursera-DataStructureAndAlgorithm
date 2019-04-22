#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 3-2 Challenge: A thief finds much more loot than his bag can fit. Help him to find the most valuable combination of items assuming that any fraction of a loot item can be put into his bag.


"""
def solve(n, W, vw):
    vw = sorted(vw, key=lambda x: x[0]/x[1], reverse=True)
    values = 0.0
    if W == 0:
        return values
    i = 0
    while W != 0 and i < n:
        v = vw[i][0]
        w = vw[i][1]
        if W <= w:
            values += v * W / w
            W = 0
        else:
            W -= w
            values += v
        i += 1
    return values


if __name__ == '__main__':
    n, W = map(int, input().split())
    vw = []
    for _ in range(n):
        vw.append(list(map(int, input().split())))
    print(solve(n, W, vw))


