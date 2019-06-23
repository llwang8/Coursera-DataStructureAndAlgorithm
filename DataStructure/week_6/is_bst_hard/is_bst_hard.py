#!/usr/bin/python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Data Structure

week 6-3 Is it a binary search tree - hard version

You are given a binary tree with integers as its keys. You need to test whether it is a correct binary
search tree. Note that there can be duplicate integers in the tree, and this is allowed. The definition of
the binary search tree in such case is the following: for any node of the tree, if its key is 𝑥, then for any
node in its left subtree its key must be strictly less than 𝑥, and for any node in its right subtree its key
must be greater than or equal to 𝑥. In other words, smaller elements are to the left, bigger elements
are to the right, and duplicates are always to the right. You need to check whether the given binary
tree structure satisfies this condition. You are guaranteed that the input contains a valid binary tree.
That is, it is a tree, and each node has at most two children.

"""

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size
init_min = -4294967296
init_max = 4294967296

class Node:
  def __init__(self, data, l_index, r_index):
    self.key = data
    self.left = l_index
    self.right = r_index


def is_bst(tree):
  if len(tree) == 0:
      return True
  return is_bst_uti(tree, 0, init_min, init_max)


def is_bst_uti(tree, node_index, mini, maxi):
  if node_index < 0:
      return True
  node = tree[node_index]

  #print(node.key, mini, maxi)
  if node.key <= mini or node.key >= maxi:
    return False
  return is_bst_uti(tree, node.left, mini, node.key) and is_bst_uti(tree, node.right, node.key-1, maxi)


def main():
  num_nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(num_nodes):
    #tree.append(list(map(int, sys.stdin.readline().strip().split())))
    [a, b, c] = list(map(int, input().strip().split()))
    tree.append(Node(a, b, c))

  if is_bst(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
