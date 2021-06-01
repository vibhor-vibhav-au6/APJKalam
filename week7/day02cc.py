"""
Recoreded video link: 
https://drive.google.com/file/d/1yIaPZHwAWYGQUASMWgvD0lg7LP6Ou0Dy/view?usp=sharing
"""


"""
Write a Program to search the target
element using Binary Search, If target element is found return the index otherwise return -1 """

def binarySearch(arr, target):
  leftPointer = 0
  rightPointer = len(arr)-1
 
  while leftPointer <= rightPointer:

      midPointer = leftPointer + (rightPointer - leftPointer) // 2;
        
      # Check if target is present at midPointer
      if arr[midPointer] == target:
          return midPointer

      # If target is greater, ignore left half
      elif arr[midPointer] < target:
          leftPointer = midPointer + 1
       

      # If target is smaller, ignore right half
      else:
          rightPointer = midPointer - 1
    
  # If we reach here, then the element
  # was not present
  return -1

# print(binarySearch( [1,2,3,15,16,19,23,55,1000], 18))

"""
Given an sorted integer array . Write a program to find Lower Bound of
target number, return the index of the element
"""

def Lower_Bound(arr, target):
  leftPointer = 0
  rightPointer = len(arr)-1
 
  while leftPointer <= rightPointer:

      midPointer = leftPointer + (rightPointer - leftPointer) // 2;
        
      # Check if target is present at midPointer
      if arr[midPointer] == target:
          while(midPointer-1 >= 0) and (arr[midPointer] == arr[midPointer-1]):
            midPointer -= 1
          return midPointer
          

      # If target is greater, ignore left half
      elif arr[midPointer] < target:
          leftPointer = midPointer + 1

      # If target is smaller, ignore right half
      else:
          rightPointer = midPointer - 1

  # If we reach here, then the element
  # was not present
  return -1

"""
Given an sorted integer array . Write a program to find UPPER Bound of target number , return the index of the element .
"""

def Upper_Bound(arr, target):
  leftPointer = 0
  rightPointer = len(arr)-1
 
  while leftPointer <= rightPointer:

      midPointer = leftPointer + (rightPointer - leftPointer) // 2;
        
      # Check if target is present at midPointer
      if arr[midPointer] == target:
          while(midPointer+1 <len(arr)) and (arr[midPointer] == arr[midPointer+1]):
            midPointer += 1
          return midPointer

      # If target is greater, ignore left half
      elif arr[midPointer] < target:
          leftPointer = midPointer + 1

      # If target is smaller, ignore right half
      else:
          rightPointer = midPointer - 1
    
  # If we reach here, then the element
  # was not present
  return -1


# driver
# print(binarySearch( [1,2,3,15,16,19,23,55,1000], 18))
print (Lower_Bound([1,1,1,2,2,2,3,3,5,5,5,6,6,7,7], 1))
print (Upper_Bound([1,1,1,2,2,2,3,3,5,5,5,6,6,7,7], 1))

