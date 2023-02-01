n=input().split(" ")
num=int(n[0])
k=int(n[1])
gamesPlayed=num*(num-1)//(2)
if num*k>gamesPlayed:
    print(-1)
else:
    print(num*k)
    for i in range(1,num+1):
        for t in range(k):
            team=((i+t)%num)+1
            print(i,team)
