#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        maxDiff = 0
        high = 0
        low = 0
        for i in range(len(arr)):
            if(arr[high]<arr[i]):
                high = i
            if(arr[low]>arr[i]):
                high = i
                low = i
            maxDiff = max(maxDiff,arr[high] -arr[low])
        return maxDiff
