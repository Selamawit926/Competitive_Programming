a="100000000"
b="500000"
def divide(a,b):
    c=""

    if (b=="0") or (a=="0" and b=="0"):
        return "Undefined"

    if len(a)==1 and len(b)==1:
        f=str(int(a)//int(b))
        c = c + f
        # print(c)
        tot=int(a)-(int(f)*int(b))
        if tot!=0:
            c = c + "."
            # print(c)
            while tot!=0:
                tot=tot*10
                f=str(tot//int(b))
                c = c + f
                tot=tot-(int(f)*int(b))

    else:
        d=a[0]
        c=""
        for i in range(1,len(a)):

            if int(d)>=int(b):
                f=str(int(d)//int(b))
                c = c + f
                # print(c)
                tot=int(d)-(int(f)*int(b))
                d=str(tot)+a[i]

                if int(d)==0:
                    c=c+"0"
                
                if int(d)!=0 and i==len(a)-1:
                    f=str(int(d)//int(b))
                    c=c+f
                    # print(c)
                    tot=int(d)-(int(f)*int(b))
                    if tot!=0:
                        c = c + "."
                        # print(c)
                        while tot!=0:
                            tot=tot*10
                            f=str(tot//int(b))
                            c = c + f
                            tot=tot-(int(f)*int(b))
                
            

            else:
                d = d + a[i]
                if int(d)==0:
                    c=c+"0"
                if len(a)==len(d):
                    f=str(int(d)//int(b))
                    c=c+f
                    tot=int(d)-(int(f)*int(b))
                    if tot!=0:
                        c = c + "."
                        # print(c)
                        while tot!=0:
                            tot=tot*10
                            f=str(tot//int(b))
                            c = c + f
                            tot=tot-(int(f)*int(b))
                
            
    return c


print(divide(a,b))
        