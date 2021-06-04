'''349. Intersection of Two Arrays'''
class Solution:
    def intersection(self, nums1, nums2):
         
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
        
#         res = []
#         for i in nums1:
#             if i in nums2:
#                 if i not in res:
#                     res.append(i)
        
#         return res

'''88. Merge Sorted Array'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        pt1 = m-1
        pt2 = n-1
        insertIndex = m + n - 1

        while pt2 >= 0:
            if pt1 >= 0 and nums1[pt1] > nums2[pt2]:
                nums1[insertIndex] = nums1[pt1]
                pt1 -= 1
            else:
                nums1[insertIndex] = nums2[pt2]
                pt2 -= 1

            insertIndex -= 1
            
        return nums1


'''75. Sort Colors'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, curr, right = 0, 0, len(nums)-1
        
        while curr <= right:
            
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left] 
                left += 1 
                curr += 1
                
               
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
                
            elif nums[curr] == 1:
                curr += 1