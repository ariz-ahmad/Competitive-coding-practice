def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1 # j is the index where nums[i] should be, we make a minus 1 becuse numbers are in [1,n]
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1
  return nums


def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()



def find_missing_number(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] # here we don't do minus 1 because numbers are in [0,n]
    if nums[i] < n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  # find the first number missing from its index, that will be our required number
  for i in range(n):
    if nums[i] != i:
      return i

  return n


def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()



def find_missing_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  missingNumbers = []

  for i in range(len(nums)):
    if nums[i] != i + 1:
      missingNumbers.append(i + 1)

  return missingNumbers


def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()



def find_duplicate(arr):
  slow, fast = arr[0], arr[arr[0]]
  while slow != fast:
    slow = arr[slow]
    fast = arr[arr[fast]]

  # find cycle length
  current = arr[arr[slow]]
  cycleLength = 1
  while current != arr[slow]:
    current = arr[current]
    cycleLength += 1

  return find_start(arr, cycleLength)


def find_start(arr, cycleLength):
  pointer1, pointer2 = arr[0], arr[0]
  # move pointer2 ahead 'cycleLength' steps
  while cycleLength > 0:
    pointer2 = arr[pointer2]
    cycleLength -= 1

  # increment both pointers until they meet at the start of the cycle
  while pointer1 != pointer2:
    pointer1 = arr[pointer1]
    pointer2 = arr[pointer2]

  return pointer1


def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()



def find_all_duplicates(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  duplicateNumbers = []
  for i in range(len(nums)):
    if nums[i] != i + 1:
      duplicateNumbers.append(nums[i])

  return duplicateNumbers


def main():
  print(find_all_duplicates([3, 4, 4, 5, 5]))
  print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()



def find_corrupt_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  for i in range(len(nums)):
    if nums[i] != i + 1:
      return [nums[i], i + 1]

  return [-1, -1]


def main():
  print(find_corrupt_numbers([3, 1, 2, 5, 2]))
  print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()



def find_first_smallest_missing_positive(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  for i in range(n):
    if nums[i] != i + 1:
      return i + 1

  return len(nums) + 1


def main():
  print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
  print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
  print(find_first_smallest_missing_positive([3, 2, 5, 1]))


main()




def find_first_k_missing_positive(nums, k):
  n = len(nums)
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  missingNumbers = []
  extraNumbers = set()
  for i in range(n):
    if len(missingNumbers) < k:
      if nums[i] != i + 1:
        missingNumbers.append(i + 1)
        extraNumbers.add(nums[i])

  # add the remaining missing numbers
  i = 1
  while len(missingNumbers) < k:
    candidateNumber = i + n
    # ignore if the array contains the candidate number
    if candidateNumber not in extraNumbers:
      missingNumbers.append(candidateNumber)
    i += 1

  return missingNumbers


def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))


main()