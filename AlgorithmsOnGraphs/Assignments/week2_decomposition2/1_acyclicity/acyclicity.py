#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Algorithm on Graphs

week 2 - 1 Checking consistentancy of CS curriculum

Problem Introduction
A Computer Science curriculum specifies the prerequisites for each course as a list of courses that should be taken before taking this course. You would like to perform a consistency check of the curriculum, that is, to check that there are no cyclic dependencies. For this, you construct the following directed graph: vertices correspond to courses, there is a directed edge (𝑢,𝑣) is the course 𝑢 should be taken before the course 𝑣. Then, it is enough to check whether the resulting graph contains a cycle.
Problem Description
Task: Check whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle.

"""

import sys


def acyclic(adj):
    visited = [0] * len(adj)
    stacking = [0] * len(adj)

    for i in range(len(adj)):
        if not visited[i]:
            if dfs(adj, visited, stacking, i):
                return 1
    return 0

def dfs(adj, visited, stacking, x):
    visited[x] = 1
    stacking[x] = 1
    for i in range(len(adj[x])):
        if not visited[adj[x][i]] and dfs(adj, visited, stacking, adj[x][i]):
            return 1
        elif stacking[adj[x][i]]:
            return 1
    stacking[x] = 0
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))



