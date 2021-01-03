def add(a,b):
    c="0"
    lst=[]

    if (a[0]!="-" and b[0]!="-") or (a[0]=="-" and b[0]=="-"):

        sub=0
        if a[0]=="-" and b[0]=="-":
            a=a.replace("-","")
            b=b.replace("-","")
            sub=1
            
      
        
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
        if sub==1:
            z= "-" + z

        print(z)

    elif (a[0] == "-" and b[0] != "-") or (a[0]!="-" and b[0]=="-"):
        
        #812
        #456
        if a[0]=="-":
            a = a.replace("-","")
            sub2=1
            
        elif b[0]=="-":
            b = b.replace("-","")
            sub2=0
            
            
        if len(a)>len(b):
            i =(len(a)-len(b))
            m = "0" * i
            b= m + b
            

        else:
            i =(len(b)-len(a))
            m = "0" * i
            a= m + a
            

        
        if int(b)<int(a):
            sub=1
            x=b
            b=a
            a=x
            #print(sub)

        else:
            sub=0

        

        lstb= list(b)
            
        for i in range(len(lstb)-1,-1,-1):
            
                
            if int(lstb[i]) >= int(a[i]):
                d = int(lstb[i])-int(a[i])

            else:
                if lstb[i-1]!="0" :
                    c=str(int(lstb[i-1])-1)
                    lstb[i-1]=c                    
                    d = (int(lstb[i])+10)-int(a[i])
                   
            
                else:
                    for j in range(i-1,-1,-1):
                        if lstb[j] !="0":
                            c=str(int(lstb[j])-1)
                            lstb[j]=c
                            
                            
                            d=(int(lstb[i])+10)-int(a[i])
                            d=str(d)
                            break
                    
                        else:
                            c="9"
                            lstb[j]=c
                                
            
                
                                
                        

                
            lst.append(str(d))

            
                

        lst.reverse()
        z=""
        for i in range(0,len(lst)):
            if lst[0]=="0":
                lst[0]=""
                z = z + lst[i]
            else:
                z = z + lst[i]


        if(sub2==1 and sub==1) or (sub2==0 and sub==0):
            print("-" + z)
        else:
            print(z)

        
   #  50000
   #  125 
      

a=input("Enter number: ")
b=input("Enter number: ")
add(a,b)
