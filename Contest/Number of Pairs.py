def check(arr,left,right,ans):
    arr.sort()
    count=0
    for i in range(len(arr)):
        diff1=left-arr[i]
        diff2=right-arr[i]
        start=0
        end=len(arr)
        lst=[]
        while start<end:
            mid=(start+end)//2
            if arr[mid]==diff1:
                lst.append(mid)
                if len(lst)==2 or diff2>arr[-1] or diff2==diff1:
                    break
                start=mid+1
            elif arr[mid]==diff2:
                lst.append(mid)
                if len(lst)==2 or diff1<arr[0] or diff2==diff1:
                    break
                end=mid-1
            else:
                if arr[mid]>diff1:
                    if diff1>=arr[0]:
                        end=mid-1
                    else:
                        start=mid+1
                elif arr[mid]<diff1:
                    if diff1<=arr[-1]:
                        start=mid+1
                    else:
                        break
        if len(lst)==1:
            count+=1
        elif len(lst)>1:
            count+=abs(lst[0]-lst[1])

        print("for ",arr[i]," ",lst," count: ",count)
          



n= eval(input())
ans=[]
for i in range(n):
    limit=input().split(" ")
    left=int(limit[1])
    right=int(limit[2])
    lst=input().split(" ")
    arr=[]
    for i in lst:
        arr.append(int(i))

    check(arr,left,right,ans)


    
