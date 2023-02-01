def find(arr,k):
    left=0
    right=k
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1

    return    

def pancake_sort(arr):
    length=len(arr)
    while length>=0:
        firstK=findMinimum(arr,length)
        find(arr,firstK)
        find(arr,length)
        length-=1

    return arr

def findMinimum(arr,length):
    mini=10001
    index=-1
    for i in range(length):
        if arr[i]<mini:
            mini=arr[i]
            index=i
    
    return index



