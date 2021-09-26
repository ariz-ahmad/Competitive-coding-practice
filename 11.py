def binary_search(arr, key):
  start, end = 0, len(arr) - 1
  isAscending = arr[start] < arr[end]
  while start <= end:
    # calculate the middle of the current range
    mid = start + (end - start) // 2

    if key == arr[mid]:
      return mid

    if isAscending:  # ascending order
      if key < arr[mid]:
        end = mid - 1  # the 'key' can be in the first half
      else:  # key > arr[mid]
        start = mid + 1  # the 'key' can be in the second half
    else:  # descending order
      if key > arr[mid]:
        end = mid - 1  # the 'key' can be in the first half
      else:  # key < arr[mid]
        start = mid + 1  # the 'key' can be in the second half

  return -1  # element not found


def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()



def search_ceiling_of_a_number(arr, key):
  n = len(arr)
  if key > arr[n - 1]:  # if the 'key' is bigger than the biggest element
    return -1

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:  # found the key
      return mid

  # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
  # we are not able to find the element in the given array, so the next big number will be arr[start]
  return start


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()



def search_next_letter(letters, key):
  n = len(letters)

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < letters[mid]:
      end = mid - 1
    else: # key >= letters[mid]:
      start = mid + 1

  # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
  return letters[start % n]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()



def find_range(arr, key):
  result = [- 1, -1]
  result[0] = binary_search(arr, key, False)
  if result[0] != -1:  # no need to search, if 'key' is not present in the input array
    result[1] = binary_search(arr, key, True)
  return result


# modified Binary Search
def binary_search(arr, key, findMaxIndex):
  keyIndex = -1
  start, end = 0, len(arr) - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:  # key == arr[mid]
      keyIndex = mid
      if findMaxIndex:
        start = mid + 1  # search ahead to find the last index of 'key'
      else:
        end = mid - 1  # search behind to find the first index of 'key'

  return keyIndex


def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()



import math


class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


def search_in_infinite_array(reader, key):
  # find the proper bounds first
  start, end = 0, 1
  while reader.get(end) < key:
    newStart = end + 1
    end += (end - start + 1) * 2
    # increase to double the bounds size
    start = newStart

  return binary_search(reader, key, start, end)


def binary_search(reader, key, start, end):
  while start <= end:
    mid = start + (end - start) // 2
    if key < reader.get(mid):
      end = mid - 1
    elif key > reader.get(mid):
      start = mid + 1
    else:  # found the key
      return mid

  return -1


def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_in_infinite_array(reader, 16))
  print(search_in_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_in_infinite_array(reader, 15))
  print(search_in_infinite_array(reader, 200))


main()



def search_min_diff_element(arr, key):
  if key < arr[0]:
    return arr[0]
  n = len(arr)
  if key > arr[n - 1]:
    return arr[n - 1]

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:
      return arr[mid]

  # at the end of the while loop, 'start == end+1'
  # we are not able to find the element in the given array
  # return the element which is closest to the 'key'
  if (arr[start] - key) < (key - arr[end]):
    return arr[start]
  return arr[end]


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()



def find_max_in_bitonic_array(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2
    if arr[mid] > arr[mid + 1]:
      end = mid
    else:
      start = mid + 1

  # at the end of the while loop, 'start == end'
  return arr[start]


def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()



def search_bitonic_array(arr, key):
  maxIndex = find_max(arr)
  keyIndex = binary_search(arr, key, 0, maxIndex)
  if keyIndex != -1:
    return keyIndex
  return binary_search(arr, key, maxIndex + 1, len(arr) - 1)


# find index of the maximum value in a bitonic array
def find_max(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2
    if arr[mid] > arr[mid + 1]:
      end = mid
    else:
      start = mid + 1

  # at the end of the while loop, 'start == end'
  return start


# order-agnostic binary search
def binary_search(arr, key, start, end):
  while start <= end:
    mid = int(start + (end - start) / 2)

    if key == arr[mid]:
      return mid

    if arr[start] < arr[end]:  # ascending order
      if key < arr[mid]:
        end = mid - 1
      else:  # key > arr[mid]
        start = mid + 1
    else:  # descending order
      if key > arr[mid]:
        end = mid - 1
      else:  # key < arr[mid]
        start = mid + 1

  return -1  # element is not found


def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()



def search_rotated_with_duplicates(arr, key):
  start, end = 0, len(arr) - 1
  while start <= end:
    mid = start + (end - start) // 2
    if arr[mid] == key:
      return mid

    # the only difference from the previous solution,
    # if numbers at indexes start, mid, and end are same, we can't choose a side
    # the best we can do, is to skip one number from both ends as key != arr[mid]
    if arr[start] == arr[mid] and arr[end] == arr[mid]:
      start += 1
      end -= 1
    elif arr[start] <= arr[mid]:  # left side is sorted in ascending order
      if key >= arr[start] and key < arr[mid]:
        end = mid - 1
      else:  # key > arr[mid]
        start = mid + 1

    else:  # right side is sorted in ascending order
      if key > arr[mid] and key <= arr[end]:
        start = mid + 1
      else:
        end = mid - 1

  # we are not able to find the element in the given array
  return -1


def main():
  print(search_rotated_with_duplicates([3, 7, 3, 3, 3], 7))


main()



def count_rotations(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2

    # if mid is greater than the next element
    if mid < end and arr[mid] > arr[mid + 1]:
      return mid + 1

    # if mid is smaller than the previous element
    if mid > start and arr[mid - 1] > arr[mid]:
      return mid

    if arr[start] < arr[mid]:  # left side is sorted, so the pivot is on right side
      start = mid + 1
    else:  # right side is sorted, so the pivot is on the left side
      end = mid - 1

  return 0  # the array has not been rotated


def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()