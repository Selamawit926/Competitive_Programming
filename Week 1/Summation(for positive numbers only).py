
def add(a,b):
    c="0"
    lst=[]

    if len(a)>len(b):
        i=len(a)-len(b)
        m="0"*i
        b=m+b
            

    else:
        i=len(b)-len(a)
        m="0"*i
        a=m+a
            
    
    for i in range(len(a)-1,-1,-1):
        if b[i]!="":
            if c!="":
                d=int(a[i])+int(b[i])+int(c)
                c=""

                
            else:
                d=int(a[i])+int(b[i])
                c=""

                
            if len(str(d)) > 1:
                c = c + str(d)[0]
                d = str(d)[1] 

            lst.append(str(d))

        
        
    lst.reverse()
    z=""
    for i in lst:
        z = z + i

    print(z)

a=input("Enter number: ")
b=input("Enter number: ")
add(a,b)

