class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst=[]
        self.generate(n,n,[],lst)
        output=[]
        for i in lst:
            stack=[]
            if self.check(stack,i):
                output.append(i)
        return output
        
        
    def generate(self,opens,closed,curr,lst):
        if closed==0 and opens==0:
            new="".join(curr)
            lst.append(new)
            curr.pop()
            return
        
        if opens>0:
            self.generate(opens-1,closed,curr+["("],lst)
        if closed>0:
            self.generate(opens,closed-1,curr+[")"],lst)
        
        if curr:curr.pop()
        return

    def check(self,stack,curr):
        for i in curr:
            if stack:
                if i==")":
                    if stack[-1]=="(":
                        stack.pop()
                    else:return False
                else:
                    stack.append(i)
            else:
                if i==")":
                    return False
                stack.append(i)
        return len(stack)==0