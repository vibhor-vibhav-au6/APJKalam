'''
Write a program to find the upper bound (first occurrence’s index) of
a target given by the user, that should be present in the list. Using linear
search.
'''
def linearSearchUpperBound(arr, target):
  upperBound = -1
  for i in range(len(arr)):
    if arr[i] == target:
      upperBound = i

  return upperBound

'''
Solve question 1 , but use binary search search.
'''

def binarySearchUpperBound(arr, target):
  left = 0
  right = len(arr)-1
  upperBound = -1

  while left <= right:
    mid = left + (right-left)//2

    if arr[mid] == target:
      upperBound = mid
      left = mid+1

      [1,2,3,3,3,4,5]
      
    
    elif arr[mid] < target:
      left = mid+1
    else:
      right = mid-1
  
  return upperBound

# print(binarySearchUpperBound([1,1,1,2,2,2,3,3,4], 2))

'''
Find largest number in a list, and second largest number (without using inbuilt functions).
'''

# def largest2numbers(arr):
#   for i in range(len(arr)):
#     minIndex = i
#     for j in range(i+1,len(arr)):
#       if arr[i] > arr[j]:
#         minIndex = j
    
#     arr[minIndex], arr[i] = arr[i], arr[minIndex]
#   print(*arr)
  
#   res = []
#   res.append(arr[-1])

  
  # for i in range(len(arr)-2,-1, -1):
  #   if res[0] != arr[i]:
  #     res.append(arr[i])
  #     return res

# def largest2numbers(arr):
#   largest = 0
#   largest2nd = 1

#   for i in range(len(arr)):

#     if arr[i] >= arr[largest]:
#       largest2nd = largest
#       largest = i
#   return (arr[largest], arr[largest2nd])

print(largest2numbers([9,3,4,5,8,1,2,3,4,9,6,9]))