class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        left=stars=0
        for i in range(len(s)):
            if s[i]=="(":
                left+=1
                stack.append(s[i])
            elif s[i]=="*":
                stars+=1
                stack.append(s[i])
            else:
                if left==0:
                    if stars>0:
                        stack.pop()
                        stars-=1
                    else:return False
                else:
                    count=0
                    while stack[-1]=="*":
                        stack.pop()
                        count+=1
                    stack.pop()
                    left-=1
                    for j in range(count):
                        stack.append("*")
        # print(stack)
        if left>0:
            count=0
            for i in range(len(stack)-1,-1,-1):
                if stack[i]=="(":
                    if count>0:
                        left-=1
                        count-=1
                    else:return False
                else:
                    count+=1

        return left==0