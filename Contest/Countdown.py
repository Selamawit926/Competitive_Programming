test=eval(input())
ans=[]
for i in range(test):
    n=input()
    num=input()
    lst=[]
    for i in num:
        lst.append(int(i))
    left=0
    right=len(lst)-1
    count=0
    while left<=right:
        if left==right:
            count+=lst[right]
            break
        elif lst[left]!=0 and lst[right]!=0:
            count+=lst[right]
            lst[right]=0
        elif lst[left]!=0 and lst[right]==0:
            count+=1
            lst[left],lst[right]=lst[right],lst[left]
        elif lst[left]==0 and lst[right]!=0:
            count+=lst[right]
            lst[right]=0
            left+=1
        elif lst[left]==0 and lst[right]==0:
            left+=1

    ans.append(count)

for i in ans:
    print(i)