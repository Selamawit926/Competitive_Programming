# arr1 = [2,3,1,3,2,4,6,7,9,2,19,19,19,7]
# arr2 = [2,1,4,3,9,6]
def relativeSortArray(arr1,arr2):
    lst=[]
    for i in arr1:
        if i not in arr2:
            lst.append(i)
            # print(lst)
            
    lst2=[0]*(len(arr1))
    k=0
    count=0
    for i in arr2:  
        for j in range(0,len(arr1)):
            if arr1[j]==i:
                count+=1
        #print(i,count)
        for m in range(k,count):
        # print(count,m)
            lst2[m]=i
            k+=1
            # print(lst2)
        #    k+=1
        #    print(arr1)
        
    for i in range(0,len(lst)):
        lst2[k]=min(lst)
        k+=1
        lst.remove(min(lst))
        # print(lst)


    # print(arr2)
    print(lst2)
    # print(lst)
    # print(arr1)

# relativeSortArray(arr1,arr2)