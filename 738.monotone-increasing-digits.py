#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = str(n)
        result = [0] * len(n)
        for i in range(len(n)-1,-1,-1):
            print(i)
            if n[i] > n[i-1]:
                result[i] = 9
            else:
                result[i] = n[i]
        print(result)
        return int(str(result))
# @lc code=end

