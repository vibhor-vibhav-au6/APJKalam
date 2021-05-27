'''
Recursive implementation of atoi() function:(5 marks)'''

def myAtoiRecursive(st):
  if st == '':
    return
  if len(st) == 1:
    return ord(st)-48
  
  return ((ord(st[0])-48)*10**(len(st)-1)) + myAtoiRecursive(st[1:])

# print(chr(48))
# print(myAtoiRecursive('1239'))

'''
Write a function that prints digits of a number from left to right , using
recursion
'''

def printRecursive(num):
    if num < 10:
        print(num)
    else:
        printRecursive(num // 10)
        print(num % 10)
  
# printRecursive(1234)


'''Reverse a string using recursion'''
def reverseString(st):
  if st == '':
    return st
  
  return st[-1]+ reverseString(st[:-1])

# print(reverseString('abcd'))

  
'''Recursive implementation of binary search'''

def binarySearch(array, target):
  return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
  if left > right:
    return -1

  middle = (left + right) // 2
  potentialMatch = array[middle]
  
  if target == potentialMatch:
    return middle
  elif target < potentialMatch:
    return binarySearchHelper(array, target, left, middle - 1)
  else:
    return binarySearchHelper(array, target, middle + 1, right)

print(binarySearch([1,2,3,4,5,6], 4))
