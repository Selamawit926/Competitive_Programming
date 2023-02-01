n=input().split(" ")
lst=[]
for i in range(int(n[0])):
    line=input().split(" ")
    lst.append(int(line[0])*int(line[1]))

m=input().split(" ")
prefix=[]
tot=0
for i in lst:
    tot+=i
    prefix.append(tot)
# print(prefix)
ans=[]
for i in range(len(m)):
    num=int(m[i])
    if num<=prefix[0]:
        ans.append(1)
    elif num>=prefix[-1]:
        ans.append(int(n[0]))

    else:
        start=0
        end=len(prefix)
        while start<=end:
            mid=(start+end)//2
            if prefix[mid]==num:
                ans.append(mid+1)
                break
            if prefix[mid]>num:
                if mid-1>=0:
                    if prefix[mid-1]<num:
                        ans.append(mid+1)
                        break
                    else:
                        end=mid-1
                else:
                    ans.append(1)
            elif prefix[mid]<num:
                if mid+1<len(prefix):
                    if prefix[mid+1]>num:
                        ans.append(mid+2)
                        break
                    else:
                        start=mid+1
                else:
                    ans.append(int(n[0]))

for i in ans:
    print(i)