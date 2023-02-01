from typing import Deque


from collections import deque
def calculate(di,num):

    for i in range(len(num)):
        if num[i]=="0" or num[i]=="5":
            if num[i] in di:
                di[num[i]].appendleft(i)
            else:

                di[num[i]]=deque()
                di[num[i]].append(i)
        
    maxi=max(di.values())
    # print(maxi)
    prev=int(num[:maxi[0]+1])
    # print("first: ",prev)
    check=0
    options=[]
    while prev%25!=0:
        while maxi:
            i=0
            while prev>=25:
                prev=int(num[i:maxi[0]+1])
                if prev%25!=0:
                    check=int(num[i]+num[maxi[0]])
                    if check%25==0:
                        options.append(check)
                    i+=1
                else:
                    if prev!=0:
                        break
            
            maxi.popleft()
            # print("maxi: ",maxi, " prev: ", prev, " options: ",options)

        if prev%25==0 and prev!=0:
            break
        maxi=max(di.values())
        if maxi:
            # print("here: ",maxi)
            prev=int(num[:maxi[0]+1])
        else:
            break
    # print(len(str(prev)),len(num),99050%25)
    # print(options)
    changed=str(prev)
    if changed[0]=="0":
        i=0
        # print("on prev: ",changed)
        while changed[i]=="0":
            i+=1
            if i==len(changed):
                i-=1
                break
        prev=int(changed[i:])
    
    # print(options,prev)
    if options:
        maxi2=max(options)
        changed=str(maxi2)
        # print("on options: ",changed)
        if changed[0]=="0":
            i=0
            while changed[i]=="0":
                i+=1
                if i==len(changed):
                    i-=1
                    break
            maxi2=int(changed[i:])

        if len(num)-len(str(prev))>len(num)-len(str(maxi2)):
            print(len(num)-len(str(maxi2)))
        else:
            print(len(num)-len(str(prev))) 
    else:
       print(len(num)-len(str(prev))) 
    

n= eval(input())
lst=[]
for i in range(n):
    num= input()
    lst.append(num)
di={}
for num in lst:
    calculate(di,num)

