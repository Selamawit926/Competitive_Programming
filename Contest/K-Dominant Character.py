
def reader():
    nums = input().split(' ')
    lst=nums[0]
    di={}
    for i in range(len(lst)):
        if lst[i] in di:
            # print(di[lst[i]][0])
            di[lst[i]][0]+=1
            di[lst[i]][1].append(i)
        else:
            di[lst[i]]=[1,[i]]
    
    potential=max(di.values())
    print(potential)
    maxi=0
    for i in range(1,len(potential[1])):
        maxi=max(maxi,potential[1][i]-potential[1][i-1])

    if maxi==0:
        if(len(lst) == 2):
            print(1)
        else:
            print((len(lst)//2)+1)
    else:
        maxi=max(maxi,potential[1][0])
        maxi=max(maxi,len(lst)-potential[1][-1])
        print(maxi)
    
reader()