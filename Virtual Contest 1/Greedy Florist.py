def getMinimumCost(k, c):
    
    c.sort()
    # print(c)
    
    if k>=len(c):
        return sum(c)
    
    else:
        tot=0
        count=0
        j=1
        for i in range(len(c)-1,len(c)-k-1,-1):
            tot+=c[i]
            
        for i in range(len(c)-k-1,-1,-1):
            if count==k:
                j+=1
                count=0
        
            tot+=(j+1)*c[i]
            count+=1
            
        return tot