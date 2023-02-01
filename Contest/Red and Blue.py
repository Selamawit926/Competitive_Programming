n=eval(input())
ans=[]
for i in range(n):
    num1=eval(input())
    line1=input().split(" ")
    num2=eval(input())
    line2=input().split(" ")
    tot=maxi1=maxi2=0
    for i in range(len(line1)):
        tot+=int(line1[i])
        maxi1=max(maxi1,tot)
    tot=0
    for i in range(len(line2)):
        tot+=int(line2[i])
        maxi2=max(maxi2,tot)

    ans.append(maxi1+maxi2)

for i in ans:
    print(i)