def mergeSort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=mergeSort(arr[:mid])
    right=mergeSort(arr[mid:])
    lst=[]
    pointer1=pointer2=0
    while pointer1<len(left) and pointer2<len(right):
        if left[pointer1]<right[pointer2]:
            lst.append(left[pointer1])
            pointer1+=1
        else:
            lst.append(right[pointer2])
            pointer2+=1
    if pointer1<len(left):
        for i in range(pointer1,len(left)):
            lst.append(left[i])
    if pointer2<len(right):
        for i in range(pointer2,len(right)):
            lst.append(right[i])
    
    return lst

arr=[12,11,13,5,6,-7]
print(mergeSort(arr))