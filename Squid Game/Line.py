cases=eval(input())
output=[]
for i in range(cases):
    length=input()
    inp=input()
    curr=[]
    ans=[]
    for j in range(len(inp)):
        if inp[j]=="L":
            curr.append(j)
        else:
            curr.append((len(inp)-1)-j)
    tot=sum(curr)
    left=0
    right=len(inp)-1
    # print(tot)
    while left<right:
        if inp[left]=="L":
            tot-=curr[left]
            tot+=(len(inp)-1)-left
            # print("left",tot,left)
            ans.append(tot)
        if inp[right]=="R":
            tot-=curr[right]
            tot+=right
            # print(tot,right)
            ans.append(tot)
        left+=1
        right-=1
    while len(ans)<len(inp):
        ans.append(tot)
    output.append(ans)

for ans in output:
    for i in ans:
        print(i, end=" ")
    print()
    

    