#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Data Structure

week 1-2 Get tree height

In this problem, your goal is to get used to trees. You will need to read a description of a tree from the
input, implement the tree data structure, store the tree and compute its height.

You are given a description of a rooted tree. Your task is to compute and output its height. Recall
that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.

"""


import sys
import threading

class Node():
    def __init__(self, idx):
        self.index = idx
        self.children = []

    def add_child(self, child_node):
        self.child.append(child_node)

class Node():
    def __init__(self, idx):
        self.index = idx
        self.children = []

    def add_child(self, child_node):
        self.child.append(child_node)

def get_height_node(nodes, root):
    max_height = 0
    if len(nodes[root].children) == 0:
        return 1

    for c in nodes[root].children:
        new_height = 1 + get_height(nodes, c)
        if new_height > max_height:
            max_height = new_height

    return max_height


def get_height(nodes, root):
    max_height = 0
    if len(nodes[root]) == 0:
        return 1

    for c in nodes[root]:
        new_height = 1 + get_height(nodes, c)
        if new_height > max_height:
            max_height = new_height
    #print(root, max_height)
    return max_height

def compute_height(n, parents):
    nodes = {}
    for i in range(n):
        if i not in nodes:
            nodes[i] = []
        p_idx = parents[i]
        if p_idx == -1:
            root = i
        else:
            #print('p_idx: {}'.format(p_idx))
            #print(nodes)
            if p_idx not in nodes:
                nodes[p_idx] = []
            nodes[p_idx].append(i)
    #print(nodes, root)
    return get_height(nodes, root)



def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
