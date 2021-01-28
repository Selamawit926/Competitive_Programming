class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(0,len(tokens)):
            if tokens[i] not in ["+","-","/","*"]:
                stack.append(tokens[i])
                
            else:
                if tokens[i]=="+":
                    stack.append(self.operation("+",stack.pop(),stack.pop()))
                    
                elif tokens[i]=="-":
                    stack.append(self.operation("-",stack.pop(),stack.pop()))
                    
                elif tokens[i]=="*":
                    stack.append(self.operation("*",stack.pop(),stack.pop()))
                    
                else:
                    stack.append(self.operation("/",stack.pop(),stack.pop()))
                    
                    
                  
        return int(stack[0])
                    
                    
    
    
    def operation(self,op,inp1,inp2):
        if op=="+":
            ans=int(inp1)+int(inp2)
            return ans
        elif op=="-":
            ans=int(inp2)-int(inp1)
            return ans
        
        elif op=="*":
            ans=int(inp1)*int(inp2)
            return ans
        
        else:
            ans=int(inp2)/int(inp1)
            return ans