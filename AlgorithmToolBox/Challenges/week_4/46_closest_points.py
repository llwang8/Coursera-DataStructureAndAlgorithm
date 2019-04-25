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
    #points_y_sorted = sorted(points, key=lambda x:x[1])
    #print(points_x_sorted)
    d = filter_x_get_min(points_x_sorted)
    return d

def filter_x_get_min(points_x_sorted):
    if len(points_x_sorted) <= 3:
        return brute(points_x_sorted)

    mid = len(points_x_sorted) // 2
    points_x_l = points_x_sorted[:mid]
    points_x_r = points_x_sorted[mid:]
    #print('1: {}'.format(points_x_l))
    #print('2: {}'.format(points_x_r))

    d1 = filter_x_get_min(points_x_l)
    d2 = filter_x_get_min(points_x_r)
    #print(d1, d2)

    d = min(d1,d2)

    mid_x = points_x_sorted[mid][0]
    filter_by_x = [x for x in points_x_sorted if mid_x-d <= x[0] <= mid_x+d]
    filter_by_x_sort_by_y = sorted(filter_by_x, key=lambda x:x[1])
    #print('3: {}'.format(filter_by_x_sort_by_y))

    d3 = brute(filter_by_x_sort_by_y)
    #print(d3)

    return min(d, d3)

def brute(points_sorted):
    min_d = float('inf')
    m = len(points_sorted)
    for i in range(m):
        for j in range(i+1, m):
            p = points_sorted[i]
            q = points_sorted[j]
            #print(p, q)
            dist = distance(p[0], p[1], q[0], q[1])
            if dist < min_d:
                min_d = dist
    return min_d


if __name__ == '__main__':
    n = int(input())
    points =[]
    for _ in range(n):
        points.append(list(map(int, input().split())))

    print("{0:.9f}".format(find_closest(points)))



