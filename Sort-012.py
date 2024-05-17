# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = c1 = c2 = 0
        for i in nums:
            if i == 0:
                c0 += 1
            elif i == 1:
                c1 += 1
            else:
                c2 += 1
        i = 0
        while i < c0:
            nums[i] = 0
            i += 1
        while i < c0+c1:
            nums[i] = 1
            i += 1
        while i < c0+c1+c2:
            nums[i] = 2
            i += 1
