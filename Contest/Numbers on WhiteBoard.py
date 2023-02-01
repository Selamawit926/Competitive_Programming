import math
from collections import deque
n=eval(input())
main=deque()
for i in range(n):
    num=eval(input())
    length=num
    lst=[]
    main.append(deque())
    for i in range(1,num+1):
        lst.append(i)
   
    if num==2:
        main[-1].append(int(math.ceil((1+2)/2)))
        main[-1].append([1,2])
        continue
    count=0
    mid=0
    while count<num-1:
        if count==0:
            main[-1].append([num-2,num])
            mid=int(math.ceil((num-2+num)/2))
        elif count==1:
            main[-1].append([mid,mid])
            mid=int(math.ceil((mid+mid)/2))
        
        else:
            main[-1].append([mid,mid-2])
            mid=int(math.ceil((mid+(mid-2))/2))
        
        count+=1
        
    main[-1].appendleft(mid)
            
# print(main)
for lst in main:
    for i in range(len(lst)):
        if i==0:
            print(lst[i])
        else:
            for j in lst[i]:
                print(j,end=" ")
            print()

                