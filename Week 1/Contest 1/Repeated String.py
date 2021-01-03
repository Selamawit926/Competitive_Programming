def repeatedString(s, n):
    if len(s)==1 and s=="a":
        return n
    

    if n%len(s)==0:
        m=n//len(s)
        s=s*m

    else:
        m=n//len(s)
        s=s*m
        m=n%len(s)
        
        '''
        m=n-len(s)
        j=0
        for i in range(0,m):
            s = s + s[j]
            j+=1
                
        '''
   # return s   
    return s.count("a")

print(repeatedString("aba",10))