n=eval(input())
inp=input().split(" ")
lst=[]
for i in inp:
    lst.append(int(i))
lst.sort()
left=tot=0
right=len(lst)-1
count=len(lst)
prev=0
while left<right:
    if tot+lst[left]<lst[right]:
        tot+=lst[left]
        left+=1
    else:
        count-=((left-prev))
        tot=0
        right-=1
        prev=left
print(lst)
print(left,right)
print(count)


        