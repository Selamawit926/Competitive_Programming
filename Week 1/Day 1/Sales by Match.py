def sockMerchant(n, ar):
    a=0
    lst=[]
    for i in ar:
        if i in lst:
            continue
        else:
            if ar.count(i) % 2 ==0:
                c= ar.count(i)//2
                a =a + c
                lst.append(i)
                
            else:
                c= ar.count(i)//2
                a =a + c
                lst.append(i)
                     
                    
       
    return (a)


n=eval(input("Enter number of socks: "))
inp=input("Enter number of colors here: ")
ar=[eval(inp) for inp in inp.split()]
print(sockMerchant(n,ar))
