def superDigit(n, k):
    # n=n*k
    tot=0
    if len(n)==1:
        return n

    for i in range(0,len(n)):
        tot=tot+int(n[i])
        
    tot=tot*k
        
    return superDigit(str(tot),1)