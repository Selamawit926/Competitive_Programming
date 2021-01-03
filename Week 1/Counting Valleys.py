def countingValleys(steps, path):
    x=0
    lst=[]
    for i in path:
        if i == "U" or i=="u":
            x+=1
        
        if i == "D" or i=="d":
            x-=1
        
        lst.append(x)
    
    val=0
    for i in range(0,len(lst)):
        if lst[i]==0 and lst[i-1]<0:
            val+=1
    
    print(val)

steps=eval(input("Enter number of steps: "))
path=input("Enter path:")
countingValleys(steps,path)
