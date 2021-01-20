def maximumToys(prices, k):
    count=0
    tot=0
    prices.sort()

    
    for i in range(0,len(prices)):
        tot=tot+prices[i]
        if tot<=k:
            count+=1
        else:break
            
    return count