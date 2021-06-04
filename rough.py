class Solution(object):
    def merge(self, nums1, m, nums2, n):
        pt1, pt2, insertIndex = m-1, n-1, m + n - 1

        while pt2 >= 0:
            if pt1 >= 0 and nums1[pt1] > nums2[pt2]:
                nums1[insertIndex] = nums1[pt1]
                pt1 -= 1
            else:
                nums1[insertIndex] = nums2[pt2]
                pt2 -= 1

            insertIndex -= 1
        return nums1


