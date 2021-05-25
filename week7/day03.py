# https://leetcode.com/problems/binary-sea

class Solution:
    def search(self, nums, target):
        leftPtr, rightPtr = 0, len(nums) - 1
        
        while leftPtr <= rightPtr:
            
            midPtr = leftPtr + (rightPtr - leftPtr) // 2
            
            if nums[midPtr] == target:
                return midPtr
            
            if target < nums[midPtr]:
                rightPtr = midPtr - 1
            else:
                leftPtr = midPtr + 1
                
        return -1


'''
Given an sorted integer array . Write a program to find Lower Bound of target number, return the index of the element 
Input: arr = [1,2,3,3,3,4,4,5,5,7,7,7] 
target = 6
Output: 8
'''

def Lower_Bound_helper(arr, target):
  # previous = -1
  for i in range(len(arr)):
    if arr[i] == target:
      return i
    if arr[i] > target:
      return (i-1)
    else:
      return len(arr)

    # previous += 1

print(Lower_Bound_helper([1,2,3,3,3,4,4,5,5,7,7,7], 8))