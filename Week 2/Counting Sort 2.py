def countingSort(arr):
    lst=[0]*(max(arr)+1)
    lst2=[]


    for i in arr:
        lst[i]+=1
    

    for i in range(0,len(lst)):
        for k in range(0,lst[i]):
            lst2.append(i)
   
    return lst2
    