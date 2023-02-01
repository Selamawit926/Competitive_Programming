n=eval(input())
ans=[]
possible=set()
found=False
count=0
for i in range(n):
    s=input()
    t=input()
    first=t[0]
    if not found and count>0:
        if len(possible)==2:
            ans.append("YES")
        else:
            # print("here")
            ans.append("NO")
        found=False
    possible=set()
    pos=[]
    for i in range(len(s)):
        if s[i]==first:
            pos.append(i)

    for index in range(len(pos)):
        pointer=pos[index]
        left=0
        toRight=True
        toLeft=False
        reverse=True
        lst=[]
        visited=set()
        while pointer<len(s) and pointer>=0 and left<len(t):
            # print(pointer,left)
            if (pointer,left) not in visited:
                visited.add((pointer,left))
                if s[pointer]==t[left] and toRight:
                    lst.append(s[pointer])
                    if pointer+1<len(s):
                        pointer+=1
                    else:
                        toRight=False
                        toLeft=True
                        pointer-=1
                    left+=1
                elif s[pointer]==t[left] and toLeft:
                    lst.append(s[pointer])
                    pointer-=1
                    left+=1
                elif s[pointer]!=t[left] and toRight:
                    toRight=False
                    toLeft=True
                    pointer-=1
                    left-=1
                elif s[pointer]!=t[left] and toLeft:
                    reverse=False
                    break
            else:
                pointer-=1
                left+=1
        print(lst,reverse)
        word="".join(lst)
        if reverse and word==t:
            ans.append("YES")
            found=True
            break
        elif index==len(pos)-1 and not reverse: 
            possible.add("NO")

        elif reverse and word!=t:
            possible.add("NO")
        
        count+=1
for i in ans:
    print(i)
