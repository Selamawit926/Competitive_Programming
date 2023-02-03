class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[path[0]]
        word=[]
        nots={"/","."}
        i=1
        while i<len(path):
            if path[i] not in nots:
                word.append(path[i])
                i+=1
            else:
                if len(word)>0:
                    curr="".join(word)
                    stack.append(curr)
                    word=[]
                if path[i]=="/" and stack[-1]!="/":
                    stack.append(path[i])
                    i+=1
                elif path[i]==".":
                    dots=[]
                    while i<len(path) and path[i]==".":
                        dots.append(path[i])
                        i+=1
                    if len(dots)>=3 or stack[-1]!="/" or (i<len(path) and path[i] not in nots):
                        currD="".join(dots)
                        stack.append(currD)
                    elif len(dots)==2:
                        if len(stack)>1: stack.pop()
                        while stack[-1]!="/":
                            stack.pop()
                else:
                    i+=1
        if word:
            stack.append("".join(word))
        if stack[-1]=="/" and len(stack)>1:stack.pop()
        return "".join(stack)
                    