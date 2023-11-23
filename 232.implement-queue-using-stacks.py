#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)
        # print('in',self.stack_in)

    def pop(self) -> int:
        if self.empty():
            return None
        
        if len(self.stack_out) == 0:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
                # print('out after push',self.stack_out)
            return self.stack_out.pop()
        else:
            return self.stack_out.pop()
            
    def peek(self) -> int:
      
        temp = self.pop()
        # print(self.stack_out)
        self.stack_out.append(temp)
        # print(self.stack_out)
        return temp
    
    def empty(self) -> bool:
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return True
        else:return False         


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

