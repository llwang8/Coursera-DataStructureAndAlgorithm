#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm on Graphs

week 3 - 2 check if a graph is bipartite


Problem Introduction
An undirected graph is called bipartite if its vertices can be split into two parts such that each edge of the graph joins to vertices from different parts. Bipartite graphs arise naturally in applications where a graph is used to model connections between objects of two different types (say, boys and girls; or students and dormitories).
An alternative definition is the following: a graph is bipartite if its vertices can be colored with two colors (say, black and white) such that the endpoints of each edge have different colors.
Problem Description
Task. Given an undirected graph with 𝑛 vertices and 𝑚 edges, check whether it is bipartite.

"""

import sys
import queue

def bipartite(adj):
    colors = [-1] * len(adj)
    colors[0] = 0
    queue = [0]
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if colors[v] == -1:
                colors[v] = 1 - colors[u]
                queue.append(v)
            elif colors[v] == colors[u]:
                return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
