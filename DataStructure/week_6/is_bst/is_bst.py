#!/usr/bin/python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Data Structure

week 6-2 Is it a binary search tree

In this problem you are going to test whether a binary search tree data structure from some programming
language library was implemented correctly. There is already a program that plays with this data structure
by inserting, removing, searching integers in the data structure and outputs the state of the internal binary
tree after each operation. Now you need to test whether the given binary tree is indeed a correct binary
search tree. In other words, you want to ensure that you can search for integers in this binary tree using
binary search through the tree, and you will always get correct result: if the integer is in the tree, you will
find it, otherwise you will not.

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
  return is_bst_uti(tree, node.left, mini, node.key) and is_bst_uti(tree, node.right, node.key, maxi)


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


