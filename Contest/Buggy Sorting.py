n=eval(input())
if n==1 or n==2:
    print(-1)
else:
    for i in range(n-1,n//2,-1):
        print(i,end=" ")
    print(n,end=" ")
    for i in range(1,(n//2)+1):
        print(i,end=" ")
