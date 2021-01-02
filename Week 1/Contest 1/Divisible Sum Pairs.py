def divisibleSumPairs(n, k, ar):
    lst=[]
    for i in range(0,len(ar)):
        for j in range(i+1,len(ar)):
            if ((ar[i]+ar[j])%k==0) and i<j:
                lst.append(ar[i])
                lst.append(ar[j])
            else:
                continue
    
    
    print(len(lst)//2)

n=eval(input("Enter number of list: "))
a=input("Enter list of numbers: ")
ar=[eval(a) for a in a.split()]
k=eval(input("Enter number here: "))
divisibleSumPairs(n,k,ar)