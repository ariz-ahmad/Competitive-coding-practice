from heapq import *


def find_k_largest_numbers(nums, k):
  minHeap = []
  # put first 'K' numbers in the min heap
  for i in range(k):
    heappush(minHeap, nums[i])

  # go through the remaining numbers of the array, if the number from the array is bigger than the
  # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if nums[i] > minHeap[0]:
      heappop(minHeap)
      heappush(minHeap, nums[i])

  # the heap has the top 'K' numbers, return them in a list
  return list(minHeap)


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()



from heapq import *


def find_Kth_smallest_number(nums, k):
  maxHeap = []
  # put first k numbers in the max heap
  for i in range(k):
    heappush(maxHeap, -nums[i])

  # go through the remaining numbers of the array, if the number from the array is smaller than the
  # top(biggest) number of the heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if -nums[i] > maxHeap[0]:
      heappop(maxHeap)
      heappush(maxHeap, -nums[i])

  # the root of the heap has the Kth smallest number
  return -maxHeap[0]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()



from __future__ import print_function
from heapq import *


class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  # used for max-heap
  def __lt__(self, other):
    return self.distance_from_origin() > other.distance_from_origin()

  def distance_from_origin(self):
    # ignoring sqrt to calculate the distance
    return (self.x * self.x) + (self.y * self.y)

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
  maxHeap = []
  # put first 'k' points in the max heap
  for i in range(k):
    heappush(maxHeap, points[i])

  # go through the remaining points of the input array, if a point is closer to the origin than the top point
  # of the max-heap, remove the top point from heap and add the point from the input array
  for i in range(k, len(points)):
    if points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
      heappop(maxHeap)
      heappush(maxHeap, points[i])

  # the heap has 'k' points closest to the origin, return them in a list
  return list(maxHeap)


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()



from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
  minHeap = []
  # add all ropes to the min heap
  for i in ropeLengths:
    heappush(minHeap, i)

  # go through the values of the heap, in each step take top (lowest) rope lengths from the min heap
  # connect them and push the result back to the min heap.
  # keep doing this until the heap is left with only one rope
  result, temp = 0, 0
  while len(minHeap) > 1:
    temp = heappop(minHeap) + heappop(minHeap)
    result += temp
    heappush(minHeap, temp)

  return result


def main():

  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))

main()



from heapq import *


def find_k_frequent_numbers(nums, k):

  # find the frequency of each number
  numFrequencyMap = {}
  for num in nums:
    numFrequencyMap[num] = numFrequencyMap.get(num, 0) + 1

  minHeap = []

  # go through all numbers of the numFrequencyMap and push them in the minHeap, which will have
  # top k frequent numbers. If the heap size is more than k, we remove the smallest(top) number
  for num, frequency in numFrequencyMap.items():
    heappush(minHeap, (frequency, num))
    if len(minHeap) > k:
      heappop(minHeap)

  # create a list of top k numbers
  topNumbers = []
  while minHeap:
    topNumbers.append(heappop(minHeap)[1])

  return topNumbers


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()



from heapq import *


def sort_character_by_frequency(str):

  # find the frequency of each character
  charFrequencyMap = {}
  for char in str:
    charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

  maxHeap = []
  # add all characters to the max heap
  for char, frequency in charFrequencyMap.items():
    heappush(maxHeap, (-frequency, char))

  # build a string, appending the most occurring characters first
  sortedString = []
  while maxHeap:
    frequency, char = heappop(maxHeap)
    for _ in range(-frequency):
      sortedString.append(char)

  return ''.join(sortedString)


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()



from heapq import *


class KthLargestNumberInStream:
  minHeap = []

  def __init__(self, nums, k):
    self.k = k
    # add the numbers in the min heap
    for num in nums:
      self.add(num)

  def add(self, num):
    # add the new number in the min heap
    heappush(self.minHeap, num)

    # if heap has more than 'k' numbers, remove one number
    if len(self.minHeap) > self.k:
      heappop(self.minHeap)

    # return the 'Kth largest number
    return self.minHeap[0]


def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()




from heapq import *


def find_closest_elements(arr, K, X):
  index = binary_search(arr, X)
  low, high = index - K, index + K

  low = max(low, 0)  # 'low' should not be less than zero
  # 'high' should not be greater the size of the array
  high = min(high, len(arr) - 1)

  minHeap = []
  # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
  for i in range(low, high+1):
    heappush(minHeap, (abs(arr[i] - X), arr[i]))

  # we need the top 'K' elements having smallest difference from 'X'
  result = []
  for _ in range(K):
    result.append(heappop(minHeap)[1])

  result.sort()
  return result


def binary_search(arr,  target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = int(low + (high - low) / 2)
    if arr[mid] == target:
      return mid
    if arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  if low > 0:
    return low - 1
  return low


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()



from heapq import *


def find_maximum_distinct_elements(nums, k):
  distinctElementsCount = 0
  if len(nums) <= k:
    return distinctElementsCount

  # find the frequency of each number
  numFrequencyMap = {}
  for i in nums:
    numFrequencyMap[i] = numFrequencyMap.get(i, 0) + 1

  minHeap = []
  # insert all numbers with frequency greater than '1' into the min-heap
  for num, frequency in numFrequencyMap.items():
    if frequency == 1:
      distinctElementsCount += 1
    else:
      heappush(minHeap, (frequency, num))

  # following a greedy approach, try removing the least frequent numbers first from the min-heap
  while k > 0 and minHeap:
    frequency, num = heappop(minHeap)
    # to make an element distinct, we need to remove all of its occurrences except one
    k -= frequency - 1
    if k >= 0:
      distinctElementsCount += 1

  # if k > 0, this means we have to remove some distinct numbers
  if k > 0:
    distinctElementsCount -= k

  return distinctElementsCount


def main():

  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()




from heapq import *


def find_sum_of_elements(nums, k1, k2):
  minHeap = []
  # insert all numbers to the min heap
  for num in nums:
    heappush(minHeap, num)

  # remove k1 small numbers from the min heap
  for _ in range(k1):
    heappop(minHeap)

  elementSum = 0
  # sum next k2-k1-1 numbers
  for _ in range(k2 - k1 - 1):
    elementSum += heappop(minHeap)

  return elementSum


def main():

  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()







from heapq import *


def rearrange_string(str):
  charFrequencyMap = {}
  for char in str:
    charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

  maxHeap = []
  # add all characters to the max heap
  for char, frequency in charFrequencyMap.items():
    heappush(maxHeap, (-frequency, char))

  previousChar, previousFrequency = None, 0
  resultString = []
  while maxHeap:
    frequency, char = heappop(maxHeap)
    # add the previous entry back in the heap if its frequency is greater than zero
    if previousChar and -previousFrequency > 0:
      heappush(maxHeap, (previousFrequency, previousChar))
    # append the current character to the result string and decrement its count
    resultString.append(char)
    previousChar = char
    previousFrequency = frequency+1  # decrement the frequency

  # if we were successful in appending all the characters to the result string, return it
  return ''.join(resultString) if len(resultString) == len(str) else ""


def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()




from heapq import *
from collections import deque


def reorganize_string(str, k):
  if k <= 1: 
    return str

  charFrequencyMap = {}
  for char in str:
    charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

  maxHeap = []
  # add all characters to the max heap
  for char, frequency in charFrequencyMap.items():
    heappush(maxHeap, (-frequency, char))

  queue = deque()
  resultString = []
  while maxHeap:
    frequency, char = heappop(maxHeap)
    # append the current character to the result string and decrement its count
    resultString.append(char)
    # decrement the frequency and append to the queue
    queue.append((char, frequency+1))
    if len(queue) == k:
      char, frequency = queue.popleft()
      if -frequency > 0:
        heappush(maxHeap, (frequency, char))

  # if we were successful in appending all the characters to the result string, return it
  return ''.join(resultString) if len(resultString) == len(str) else ""


def main():
  print("Reorganized string: " + reorganize_string("Programming", 3))
  print("Reorganized string: " + reorganize_string("mmpp", 2))
  print("Reorganized string: " + reorganize_string("aab", 2))
  print("Reorganized string: " + reorganize_string("aapa", 3))


main()




from heapq import *


def schedule_tasks(tasks, k):
  intervalCount = 0
  taskFrequencyMap = {}
  for char in tasks:
    taskFrequencyMap[char] = taskFrequencyMap.get(char, 0) + 1

  maxHeap = []
  # add all tasks to the max heap
  for char, frequency in taskFrequencyMap.items():
    heappush(maxHeap, (-frequency, char))

  while maxHeap:
    waitList = []
    n = k + 1  # try to execute as many as 'k+1' tasks from the max-heap
    while n > 0 and maxHeap:
      intervalCount += 1
      frequency, char = heappop(maxHeap)
      if -frequency > 1:
        # decrement the frequency and add to the waitList
        waitList.append((frequency+1, char))
      n -= 1

    # put all the waiting list back on the heap
    for frequency, char in waitList:
      heappush(maxHeap, (frequency, char))

    if maxHeap:
      intervalCount += n  # we'll be having 'n' idle intervals for the next iteration

  return intervalCount


def main():
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()






from heapq import *


class Element:

  def __init__(self, number, frequency, sequenceNumber):
    self.number = number
    self.frequency = frequency
    self.sequenceNumber = sequenceNumber

  def __lt__(self, other):
    # higher frequency wins
    if self.frequency != other.frequency:
      return self.frequency > other.frequency
    # if both elements have same frequency, return the element that was pushed later
    return self.sequenceNumber > other.sequenceNumber


class FrequencyStack:
  sequenceNumber = 0
  maxHeap = []
  frequencyMap = {}

  def push(self, num):
    self.frequencyMap[num] = self.frequencyMap.get(num, 0) + 1
    heappush(self.maxHeap, Element(
      num, self.frequencyMap[num], self.sequenceNumber))
    self.sequenceNumber += 1

  def pop(self):
    num = heappop(self.maxHeap).number
    # decrement the frequency or remove if this is the last number
    if self.frequencyMap[num] > 1:
      self.frequencyMap[num] -= 1
    else:
      del self.frequencyMap[num]

    return num


def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()