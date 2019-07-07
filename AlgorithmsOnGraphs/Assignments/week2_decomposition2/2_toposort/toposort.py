#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm on Graphs

week 2 - 2 Determine the order of courses

Problem Introduction
Now, when you are sure that there are no cyclic dependencies in the given CS curriculum, you would like to find an order of all courses that is consistent with all dependencies. For this, you find a topological ordering of the corresponding directed graph.

Problem Description
Task. Compute a topological ordering of a given directed acyclic graph (DAG) with 𝑛 vertices and 𝑚 edges.
"""

import sys

def dfs(adj, used, order, x):
    used[x] = 1
    for i in range(len(adj[x])):
        if not used[adj[x][i]]:
            dfs(adj, used, order, adj[x][i])
    order.append(x)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for i in range(len(adj)):
        if not used[i]:
            dfs(adj, used, order, i)
        #print(order)
    order.reverse()
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

