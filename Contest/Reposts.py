def dfs(di,name1,count,track):
    if name1 not in di:
        count+=1
        track.append(count)
        return 
    count+=1
    # print(name1, " ",count)
    for i in di[name1]:
        if i not in visited:
            visited.add(i)
            dfs(di,i,count,track)
    return 

n=eval(input())
di={}
for i in range(n):
    line=input().split(" ")
    if line[2].lower() in di:
        di[line[2].lower()].append(line[0].lower())
    else:
        di[line[2].lower()]=[line[0].lower()]

count=1
visited=set()
track=[]
for i in di["polycarp"]:
    count=1
    if i not in visited:
        visited.add(i)
        dfs(di,i,count,track)

print(max(track))