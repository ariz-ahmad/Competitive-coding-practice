def find_single_number(arr):
  num = 0
  for i in arr:
      num ^= i
  return num

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()



def find_single_numbers(nums):
    # get the XOR of the all the numbers
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    # get the rightmost bit that is '1'
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    num1, num2 = 0, 0

    for num in nums:
        if (num & rightmost_set_bit) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num

    return [num1, num2]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()




def calculate_bitwise_complement(num):
  # count number of total bits in 'num'
  bit_count, n = 0, num
  while n > 0:
    bit_count += 1
    n = n >> 1

  # for a number which is a complete power of '2' i.e., it can be written as pow(2, n), if we
  # subtract '1' from such a number, we get a number which has 'n' least significant bits set to '1'.
  # For example, '4' which is a complete power of '2', and '3' (which is one less than 4) has a binary
  # representation of '11' i.e., it has '2' least significant bits set to '1'
  all_bits_set = pow(2, bit_count) - 1

  # from the solution description: complement = number ^ all_bits_set
  return num ^ all_bits_set


print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


main()





def flip_an_invert_image(matrix):
  C = len(matrix)
  for row in matrix:
    for i in range((C+1)//2):
      row[i], row[C - i - 1] = row[C - i - 1] ^ 1, row[i] ^ 1
      
  return matrix

def main():
    print(flip_an_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
    print(flip_an_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()