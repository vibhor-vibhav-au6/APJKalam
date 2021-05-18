"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1 = []
        for i in range(k):
            nums1.append(nums.pop())
        
        op = nums1.extend(nums)

        return op

"""
66. Plus One
https://leetcode.com/problems/plus-one/
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(-1, -len(digits) - 1, -1): 
             if digits[i] == 9:
                  digits[i] = 0 
                  if i == -len(digits): 
                       digits.insert(0, 1) 
             else: 
                  digits[i] += 1 
                  break 

        return(digits)