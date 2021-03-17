class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack=[]
        for i in pushed:
            
            stack.append(i)
            print(stack)
            
            self.check(stack,popped)
            
            # print(stack)
            # print(popped)
            
        if stack:
            self.check(stack,popped)
            
        if stack:
            return False
        
        
        return True
            
            
    def check(self,lst,popped):
        
        if lst:
            if lst[len(lst)-1]==popped[0]:
                lst.pop()
                popped.pop(0)
                self.check(lst,popped)
            