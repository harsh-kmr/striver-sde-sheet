# https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, permutation: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(permutation)
        if n in [0,1]:
            return
        largest_from_back = -1
        for i in range(n-1, -1, -1):
            if permutation[i] < permutation[largest_from_back]:
                for j in range(n-1, i, -1):
                    if permutation[j] > permutation[i]:
                        permutation[i], permutation[j] = permutation[j], permutation[i]
                        permutation[i+1:] = sorted(permutation[i+1:])
                        return
            else:
                largest_from_back = i
        permutation.sort()
