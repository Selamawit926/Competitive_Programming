n=input().split(" ")
line=input().split(" ")
letter=input().split(" ")
lst=[]
for i in letter:
    lst.append(int(i))

saved=[]
start=0
for i in range(len(line)):
    end=(int(line[i])+start)
    saved.append(end)
    start=end

# print(saved)
ans=[]
prev=[-1,0]
for i in range(len(lst)):
    if lst[i]<=prev[1]:
        # print(lst[i],prev)
        if prev[0]==0:
            ans.append([prev[0]+1,lst[i]])
        else:
            ans.append([prev[0]+1,lst[i]-saved[prev[0]-1]])
        continue
    for j in range(prev[0]+1,len(saved)):
        # print(j,lst[i],saved[j])
        if lst[i]<=saved[j]:
            if j!=0:
                ans.append([j+1,lst[i]-saved[j-1]])
            else:
                ans.append([j+1,lst[i]])
            prev=[j,saved[j]]
            break
            
for i in ans:
    print(i[0],i[1])