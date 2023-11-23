#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        squence_Matrix = [[0]*n for _ in range(n)]
        x,y = 0, 0
        loop = n//2
        mid = n//2
        count = 1
        for offset in range(1,1+loop):
            for i in range(y,n - offset):
                squence_Matrix[x][i] = count
                count += 1
            for i in range(x,n-offset):
                squence_Matrix[i][n-offset] = count
                count += 1
            for i in range(n-offset,y,-1):
                squence_Matrix[n-offset][i] = count
                count += 1
            for i in range(n-offset,x,-1):
                squence_Matrix[i][y] = count
                count += 1
            x += 1
            y += 1

        if n % 2 != 0:
            squence_Matrix[mid][mid] = n * n 
        return squence_Matrix
# @lc code=end

