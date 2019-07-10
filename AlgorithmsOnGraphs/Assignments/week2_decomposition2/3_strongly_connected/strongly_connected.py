#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm on Graphs

week 2 - 3 Whether any intersection is recheachable from any other

Problem Introduction
The police department of a city has made all streets one-way. You would like to check whether it is still possible to drive legally from any intersection to any other intersection. For this, you construct a directed graph: vertices are intersections, there is an edge (𝑢, 𝑣) whenever there is a (one-way) street from 𝑢 to 𝑣 in the city. Then, it suffices to check whether all the vertices in the graph lie in the same strongly connected component.
Problem Description
Task. Compute the number of strongly connected components of a given directed graph with 𝑛 vertices and 𝑚 edges.
"""

import sys

sys.setrecursionlimit(200000)

def reverseEdges(adj):
    rev_adj = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            rev_adj[adj[i][j]].append(i)
    return rev_adj

def dfs(adj, visited, stacking, x):
    visited[x] = 1
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            visited[adj[x][i]] = 1
            dfs(adj, visited, stacking, adj[x][i])
    stacking.append(x)


def number_of_strongly_connected_components(adj):
    result = 0
    stacking = []
    visited = [0] * len(adj)
    for i in range(len(adj)):
        if not visited[i]:
            dfs(adj, visited, stacking, i)

    rev_adj = reverseEdges(adj)
    visited = [0] * len(adj)
    while stacking:
        x = stacking.pop()
        if not visited[x]:
            dfs(rev_adj, visited, [], x)
            result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))


