class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        res = []
        
        while left <= right:
            
            if abs(nums[left]) < abs(nums(right)):
                res.append(nums[left]*nums[left])
                left += 1
            else:
                res.append(nums[right]*nums[right])
                right -= 1
            
        return res
              
a = Solution()
# print(a.sortedSquares([-4,-1,0,3,10]))    

a = [11,22,33,55,44]

l = [(i,j) for i,j in enumerate(sorted(a))]
print(l)
        
        