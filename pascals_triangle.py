# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li = []
        for i in range(numRows):
            if(i == 0):
                li.append([1])
            else:
                li2 = [1]
                for c in range(1,i):
                    li2.append(li[i-1][c-1]+li[i-1][c])
                li2.append(1)
                li.append(li2)
        return li
