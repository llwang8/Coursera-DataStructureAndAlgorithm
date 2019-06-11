# python3

"""
Coursera Specialization: Data Structure and Algorithm
Course: Data Structure

week 3-1 Convert array to heap

In this problem you will convert an array of integers into a heap. This is the crucial step of the sorting
algorithm called HeapSort. It has guaranteed worst-case running time of 𝑂(𝑛 log 𝑛) as opposed to QuickSort’s
average running time of 𝑂(𝑛 log 𝑛). QuickSort is usually used in practice, because typically it is faster, but
HeapSort is used for external sort when you need to sort huge files that don’t fit into memory of your
computer.

"""

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps_1(self):
    # The following naive implementation just sorts
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap,
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]


  def GenerateSwaps(self):
    n = len(self._data)
    for i in range(n//2-1, -1, -1):
        #print('i: {}'.format(i))
        self.siftdown(i)

  def siftdown(self, i):
      #print('inside i: {}'.format(i))
      left_child = 2*i + 1
      right_child = 2*i +2
      min_index = i
      if left_child < len(self._data) and self._data[left_child] < self._data[min_index]:
          min_index = left_child
      if right_child < len(self._data) and self._data[right_child] < self._data[min_index]:
          min_index = right_child
      if i != min_index:
        self._swaps.append((i, min_index))
        self._data[min_index], self._data[i] = self._data[i], self._data[min_index]
        #print(self._data)
        self.siftdown(min_index)


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()



