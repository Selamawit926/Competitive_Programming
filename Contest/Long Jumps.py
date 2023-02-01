# def dfs(i,lst,di,count):
#     if i>=len(lst):
#         return 0
#     if i in di:
#         count+=di[i]
#         return count

#     count=dfs(i+lst[i],lst,di,count)
#     count+=lst[i]
#     di[i]=count
#     return di[i]

def iterative(i,lst,di,count):
    while i<len(lst):
        if i in di:
            return count+di[i]
        count+=lst[i]
        i=i+lst[i]

    return count


test=eval(input())
ans=[]
for i in range(test):
    n=input()
    num=input().split(" ")
    lst=[]
    for i in num:
        lst.append(int(i))
    di={}
    for i in range(len(lst)-1,-1,-1):
        if i not in di:
            di[i]=iterative(i,lst,di,0)
    
    ans.append(max(di.values()))

for i in ans:
    print(i)