a=input("Enter number: ")
b=input("Enter number: ")
c="0"
y=""
z=""
t=1
lst2=[]

if (a[0]=="-" and b[0]!="-") or (a[0]!="-" and b[0]=="-"):
    mul=1
else:
    mul=0

if a[0]=="-":
    a=a.replace("-","")
if b[0]=="-":
    b=b.replace("-","")
    
for i in range(len(b)-1,-1,-1):
    x=""
    for j in range(len(a)-1,-1,-1):
        if b!="":
            if c!="":
                d= (int(b[i]) * int(a[j])) + int(c)
                c=""

            else:
                d= int(b[i]) * int(a[j])
                c=""

            if len(str(d))>1:
                c = c + str(d)[0]
                d = str(d)[1]
            x = x + str(d)
            
    for k in range(len(x)-1,-1,-1):
        y = y+x[k]
                  

    y = y + z
    lst2.append(y)
    y=""
    z=""
    z= z + "0"
    z=z*t
    t+=1

#print(lst)

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

      
   
        
        # 12300
        # 049
        
           
        
        
            
            

        
    lst.reverse()
    z=""
    for i in lst:
        z = z + i

    return int(z)


tot=0
for i in range(0,len(lst2)):
    tot= add(lst2[i],str(tot))

if mul==1:
    print("-" + str(tot))
else:
    print(tot)
        

