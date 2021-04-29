def pairs(k, arr):
    
    # Write your code here
    arr.sort()
    count=0
    save=set()
    for i in range(len(arr)):
        if arr[i]<=k:
            save.add(arr[i])
            continue
        
        if arr[i]-k in save:
            count+=1
        
        save.add(arr[i])
            
            
    return count