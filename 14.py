from __future__ import print_function
from heapq import *


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  # used for the min-heap
  def __lt__(self, other):
    return self.value < other.value


def merge_lists(lists):
  minHeap = []

  # put the root of each list in the min heap
  for root in lists:
    if root is not None:
      heappush(minHeap, root)

  # take the smallest(top) element form the min-heap and add it to the result
  # if the top element has a next element add it to the heap
  resultHead, resultTail = None, None
  while minHeap:
    node = heappop(minHeap)
    if resultHead is None:
      resultHead = resultTail = node
    else:
      resultTail.next = node
      resultTail = resultTail.next

    if node.next is not None:
      heappush(minHeap, node.next)

  return resultHead


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result is not None:
    print(str(result.value) + " ", end='')
    result = result.next


main()



from heapq import *


def find_Kth_smallest(lists, k):
  minHeap = []

  # put the 1st element of each list in the min heap
  for i in range(len(lists)):
    heappush(minHeap, (lists[i][0], 0, lists[i]))

  # take the smallest(top) element form the min heap, if the running count is equal to k return the number
  numberCount, number = 0, 0
  while minHeap:
    number, i, list = heappop(minHeap)
    numberCount += 1
    if numberCount == k:
      break
    # if the array of the top element has more elements, add the next element to the heap
    if len(list) > i+1:
      heappush(minHeap, (list[i+1], i+1, list))

  return number


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()




from heapq import *


def find_Kth_smallest(matrix, k):
    minHeap = []

    # put the 1st element of each row in the min heap
    # we don't need to push more than 'k' elements in the heap
    for i in range(min(k, len(matrix))):
        heappush(minHeap, (matrix[i][0], 0, matrix[i]))

    # take the smallest(top) element form the min heap, if the running count is equal to k' return the number
    # if the row of the top element has more elements, add the next element to the heap
    numberCount, number = 0, 0
    while minHeap:
        number, i, row = heappop(minHeap)
        numberCount += 1
        if numberCount == k:
            break
        if len(row) > i+1:
            heappush(minHeap, (row[i+1], i+1, row))
    return number


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()





from heapq import *
import math


def find_smallest_range(lists):
  minHeap = []
  rangeStart, rangeEnd = 0, math.inf
  currentMaxNumber = -math.inf

  # put the 1st element of each array in the max heap
  for arr in lists:
    heappush(minHeap, (arr[0], 0, arr))
    currentMaxNumber = max(currentMaxNumber, arr[0])

  # take the smallest(top) element form the min heap, if it gives us smaller range, update the ranges
  # if the array of the top element has more elements, insert the next element in the heap
  while len(minHeap) == len(lists):
    num, i, arr = heappop(minHeap)
    if rangeEnd - rangeStart > currentMaxNumber - num:
      rangeStart = num
      rangeEnd = currentMaxNumber

    if len(arr) > i+1:
      # insert the next element in the heap
      heappush(minHeap, (arr[i+1], i+1, arr))
      currentMaxNumber = max(currentMaxNumber, arr[i+1])

  return [rangeStart, rangeEnd]


def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()





from __future__ import print_function
from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
  minHeap = []
  for i in range(0, min(k, len(nums1))):
    for j in range(min(k, len(nums2))):
      if len(minHeap) < k:
        heappush(minHeap, (nums1[i] + nums2[j], i, j))
      else:
        # if the sum of the two numbers from the two arrays is smaller than the smallest(top)
        # element of the heap, we can 'break' here. Since the arrays are sorted in the
        # descending order, we'll not be able to find a pair with a higher sum moving forward
        if nums1[i] + nums2[j] < minHeap[0][0]:
          break
        else:  # we have a pair with a larger sum, remove top and insert this pair in the heap
          heappop(minHeap)
          heappush(minHeap, (nums1[i] + nums2[j], i, j))

  result = []
  for (num, i, j) in minHeap:
    result.append([nums1[i], nums2[j]])

  return result


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()






