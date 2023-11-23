#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result = []
        self.path = []
        self.backtracking(s,0,0)
        return self.result
    
    def backtracking(self,s,start_index,point_num):
        if point_num == 3:
            if self.isvalid_ip(s[start_index:]):
                # self.path.append(s[start_index:])
                temp = '.'.join(self.path) +'.'+ s[start_index:]
                self.result.append(temp)
                return
            return
        for i in range(start_index,len(s)):
            temp = s[start_index:i+1]
            # print(self.path)
            if self.isvalid_ip(temp):
                self.path.append(temp)
                point_num += 1
                self.backtracking(s,i+1,point_num)
                self.path.pop()
                point_num -= 1
                
    def isvalid_ip(self,s):
        if len(s) < 1:
            return False
        if s[0] == '0' and len(s) > 1:return False
        int_s = int(s)
        if 0 <= int_s <= 255 and len(s) == len(str(int_s)) and 1 <= len(s) <= 3:
            return True
        else:return False
# @lc code=end

