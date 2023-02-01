n=eval(input())
ans=[]
for i in range(n):
    num=input().split(" ")
    arr=input().split(" ")
    length=int(num[0])
    limit=int(num[1])
    lst=[]
    for i in arr:
        lst.append(int(i))
    
    start=len(lst)-1
    end=len(lst)-1
    lst.sort()
    teams=0
    while end>=0:
        if lst[end]*((start-end)+1)>=limit:
            teams+=1
            end-=1
            start=end
        else:
            end-=1

    ans.append(teams)

for i in ans:
    print(i)
    
