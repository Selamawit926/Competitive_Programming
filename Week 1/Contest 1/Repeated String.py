def repeatedString(s, n):

    tot=0
    count=0
    if len(s)==1 and s=="a":
        return n
    
    
    m=n//len(s)
    count=s.count("a")
    count= count*m
    
    if n%len(s)!=0:
        m=n%len(s)
        st=""
        for i in range(0,m):
            st= st + s[i]
    
        tot=st.count("a")

    return count+tot

       

