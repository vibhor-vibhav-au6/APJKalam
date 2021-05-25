'''
Given a sorted array with Duplicates . Write a program to find LOWER BOUND of a TARGET using Binary search Method. Return Index corresponding the element of lower bound element.
Example :
Input : - arr = [1,1,1,2,2,3,3,5,5,5,7,7] , Target = 4
Output : - 6
'''
def Lower_Bound(arr, target):
  leftPointer = 0
  rightPointer = len(arr)-1
  result = -1
 
  while leftPointer <= rightPointer:

      midPointer = leftPointer + (rightPointer - leftPointer) // 2;
        
      # Check if target is present at midPointer
      if arr[midPointer] == target:
          result = midPointer
          rightPointer = midPointer-1
          

      # If target is greater, ignore left half
      elif arr[midPointer] < target:
          leftPointer = midPointer + 1

      # If target is smaller, ignore right half
      else:
          rightPointer = midPointer - 1

  # If we reach here, then the element
  # was not present
  return result


'''
Given a sorted array with Duplicates . Write a program to find UPPER BOUND of a TARGET using Binary search Method. Return Index corresponding to the element of the upper bound element.
Example :
Input : - arr = [1,1,1,2,2,3,3,5,5,5,7,7] , Target = 4
Output : - 7
'''
def Upper_Bound(arr, target):
  leftPointer = 0
  rightPointer = len(arr)-1
  result = -1
 
  while leftPointer <= rightPointer:

      midPointer = leftPointer + (rightPointer - leftPointer) // 2;
        
      # Check if target is present at midPointer
      if arr[midPointer] == target:
          result = midPointer
          leftPointer = midPointer+1
          

      # If target is greater, ignore left half
      elif arr[midPointer] < target:
          leftPointer = midPointer + 1

      # If target is smaller, ignore right half
      else:
          rightPointer = midPointer - 1

  # If we reach here, then the element
  # was not present
  return result

'''
Given an array with NO Duplicates . Write a program to find PEAK ELEMENT Return value corresponding to the element of the peak element.
Example :
Input : - arr = [2,5,3,7,9,13,8]
Output : - 5 or 13 (anyone)
HINT : - Peak element is the element which is greater than both
neighhbours.
'''
def FindPeak(arr ):
  if arr == []:
    return
  if len(arr) == 1:
    return arr[0]
  
  if arr[0] > arr[1]:
    return(arr[0])
  if arr[-1] > arr[-2]:
    return (arr[-1])
  
  for i in range(1,len(arr)-1):
    if arr[i] > arr[i-1]:
      if arr[i] > arr[i+1]
      return arr[i]

