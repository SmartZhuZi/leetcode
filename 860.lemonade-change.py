#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        nums_5 = 0
        nums_10 = 0
        nums_20 = 0
        for i in range(len(bills)):
            if bills[i] == 5: 
                nums_5 += 1
            if bills[i] == 10: 
                if nums_5 < 1:
                    return False
                else: 
                    nums_10 += 1
                    nums_5 -= 1
            if bills[i] == 20: 
                if nums_5 > 0 and nums_10>0:
                    nums_5 -= 1
                    nums_10 -= 1
                    nums_20+=1
                elif nums_5 >= 3:
                    nums_5 -=3
                    nums_20 +=1
                else:return False

        return True
            
# @lc code=end

