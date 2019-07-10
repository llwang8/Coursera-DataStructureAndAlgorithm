#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm on Graphs

week 3 - 1 Compute mininum number of flight segments

Problem Introduction
You would like to compute the minimum number of flight segments to get from one city to another one. For this, you construct the following undirected graph: vertices represent cities, there is an edge between two vertices whenever there is a flight between the corresponding two cities. Then, it suffices to find a shortest path from one of the given cities to the other one.

Problem Description
Task. Given an undirected graph with 𝑛 vertices and 𝑚 edges and two vertices 𝑢 and 𝑣, compute the length of a shortest path between 𝑢 and 𝑣 (that is, the minimum number of edges in a path from 𝑢 to 𝑣).
"""

import sys
import queue

def distance(adj, s, t):
    dist = [len(adj)] * len(adj)
    dist[s] = 0
    queue =  [s]
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if dist[v] == len(adj):
                queue.append(v)
                dist[v] = dist[u] + 1
    if dist[t] != len(adj):
        return dist[t]
    return -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
