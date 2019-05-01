#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm Toolbox

week 4-5 Closest Points

In this problem, your goal is to find the closest pair of points among the given 𝑛 points. This is a basic primitive in computational geometry having applications in, for example, graphics, computer vision, traffic-control systems.

"""
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def find_closest(points):
    points_x_sorted = sorted(points, key=lambda x:(x[0], x[1]))
    d = filter_x_get_min(points_x_sorted)
    return d

def filter_x_get_min(points_x_sorted):
    if len(points_x_sorted) <= 3:
        return brute(points_x_sorted)

    mid = len(points_x_sorted) // 2
    points_x_l = points_x_sorted[:mid]
    points_x_r = points_x_sorted[mid:]

    d1 = filter_x_get_min(points_x_l)
    d2 = filter_x_get_min(points_x_r)

    d = min(d1,d2)

    mid_x = points_x_sorted[mid][0]
    filter_x_l = [x for x in points_x_l if mid_x-d <= x[0]]
    filter_x_r = [x for x in points_x_r if x[0] <= mid_x+d]
    filter_x_l = list(set(filter_x_l))
    filter_x_r = list(set(filter_x_r))

    #filter_x_l = sorted(filter_x_l, key=lambda x:x[])
    #filter_x_r = sorted(filter_x_r, key=lambda x:x[1])

    d3 = sort_y_get_min(filter_x_l, filter_x_r)

    return min(d, d3)

def sort_y_get_min(filter_x_l, filter_x_r):
    min_d = float('inf')
    for i in range(len(filter_x_l)):
        p = filter_x_l[i]
        for j in range(len(filter_x_r)):
            q = filter_x_r[j]
            dist = distance(p[0], p[1], q[0], q[1])
            if dist < min_d:
                min_d = dist
    return min_d

def brute(points_sorted):
    min_d = float('inf')
    m = len(points_sorted)
    for i in range(m):
        p = points_sorted[i]
        for j in range(i+1, m):
            q = points_sorted[j]
            dist = distance(p[0], p[1], q[0], q[1])
            if dist < min_d:
                min_d = dist
    return min_d


if __name__ == '__main__':
    n = int(input())
    points =[]
    for _ in range(n):
        points.append(tuple(map(int, input().split())))

    print("{0:.9f}".format(find_closest(points)))




