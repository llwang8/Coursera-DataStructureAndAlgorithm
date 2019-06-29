#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm on Graphs

week 1 - 1 Adding an Exit to a maze

Problem Introduction
Now you decide to make sure that there are no dead zones in a maze, that is, that at least one exit is reachable from each cell. For this, you find connected components of the corresponding undirected graph and ensure that each component contains an exit cell.

Problem Description
Task: Given an undirected graph with 𝑛 vertices and 𝑚 edges, compute the number of connected components in it.
"""

import sys


def number_of_components(adj):
    result = 0
    visited = [0] * len(adj)
    for i in range(len(adj)):
        if not visited[i]:
            result += 1
            explore(adj, visited, i)

    return result

def explore(adj, visited, x):
    visited[x] = 1
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            explore(adj, visited, adj[x][i])



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
    print(number_of_components(adj))
