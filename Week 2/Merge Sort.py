def mergeSort(lst,start,end):
    if start<end:
        mid=(start+end)//2
        mergeSort(lst,start,mid)
        mergeSort(lst,mid+1,end)
        
    elif end-start==1:
        return lst[end]


lst=[2,3,1,4]
print(mergeSort(lst,0,len(lst)))