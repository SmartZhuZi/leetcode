#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_nums = []
        for i in tokens:
            # print(i)
            if i not in ['+','-','*','/']:
                stack_nums.append(int(i))
            else:
                num2 = int(stack_nums.pop())
                num1 = int(stack_nums.pop())
                # print(stack_nums)
                if i == '+':
                    result = num1 + num2
                elif i == '-':
                    result = num1 - num2
                elif i == '*':
                    result = num1 * num2
                elif i == '/':
                    result = num1 / num2
                # print(num1,num2,result)
                stack_nums.append(result)
        return int(stack_nums[-1])
# @lc code=end

