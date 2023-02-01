n=eval(input())
ans=[]
for i in range(n):
    num=input()
    row1=input().split(" ")
    row2=input().split(" ")
    prefix1=[]
    prefix2=[]
    tot=0
    for i in range(len(row1)):
        tot+=int(row1[i])
        prefix1.append(tot)

    tot=0
    for i in range(len(row2)-1,-1,-1):
        # print(i)
        tot+=int(row2[i])
        prefix2.append(tot)
    
    prefix2.reverse()
    # print(prefix1,prefix2)

    possible=[]
    for i in range(len(row1)):
        answer=max(prefix1[-1]-prefix1[i],prefix2[0]-prefix2[i])
        possible.append(answer)

    ans.append(min(possible))

for i in ans:
    print(i)

    
