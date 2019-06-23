# python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Data Structure

week 6-1 Tree Order

You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.
"""

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    self.inOrderTraversal(0)
    return self.result

  def inOrderTraversal(self, idx):
    if self.left[idx] != -1:
      self.inOrderTraversal(self.left[idx])
    self.result.append(self.key[idx])
    if self.right[idx] != -1:
      self.inOrderTraversal(self.right[idx])
    return self.result

  def preOrder(self):
    self.result = []
    self.preOrderTraversal(0)
    return self.result

  def preOrderTraversal(self, idx):
    self.result.append(self.key[idx])
    if self.left[idx] != -1:
      self.preOrderTraversal(self.left[idx])
    if self.right[idx] != -1:
      self.preOrderTraversal(self.right[idx])

  def postOrder(self):
    self.result = []
    self.postOrderTraversal(0)
    return self.result

  def postOrderTraversal(self, idx):
    if self.left[idx] != -1:
      self.postOrderTraversal(self.left[idx])
    if self.right[idx] != -1:
      self.postOrderTraversal(self.right[idx])
    self.result.append(self.key[idx])

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
