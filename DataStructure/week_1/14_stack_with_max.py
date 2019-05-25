#python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Data Structure

week 1-4 Extending Stack Interface

Stack is an abstract data type supporting the operations Push() and Pop(). It is not difficult to implement
it in a way that both these operations work in constant time. In this problem, you goal will be to implement
a stack that also supports finding the maximum value and to ensure that all operations still work in constant
time.

"""


import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)


class Stack():
    def __init__(self):
        self.__stack = []
        self.max = []

    def push(self, a):
        self.__stack.append(a)
        self.add_max(a)

    def pop(self):
        if len(self.__stack) > 0:
            self.__stack.pop()
            self.max.pop()

    def add_max(self, m):
        if len(self.max) > 0:
            last_max = self.max[-1]
            self.max.append(max(m, last_max))
        else:
            self.max.append(m)
        #print(self.max)


if __name__ == '__main__':
    stack = Stack()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            num = int(query[1])
            stack.push(num)
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max[-1])
        else:
            assert(0)




