def find(x,parents):
    if parents[x-1]==x:
        return x
    parents[x-1]=find(parents[x-1],parents)
    return parents[x-1]
def union(x,y,parents,size):
    if size[x-1]>=size[y-1]:
        parents[y-1]=x
        size[y-1]+=1
    elif size[x-1]<size[y-1]:
        parents[x-1]=y
        size[x-1]+=1
    return

n= input().split(" ")
mocha=int(n[1])
diana=int(n[2])
nodes=int(n[0])
mochaDi=set()
dianaDi=set()
mochaParents=[]
dianaParents=[]
sizeM=[0]*nodes
sizeD=[0]*nodes
for i in range(1,nodes+1):
    mochaParents.append(i)
    dianaParents.append(i)

for i in range(mocha):
    line=input().split(" ")
    mochaDi.add((int(line[0]),int(line[1])))
    parentx=find(int(line[0]),mochaParents)
    parenty=find(int(line[1]),mochaParents)
    union(parentx,parenty,mochaParents,sizeM)

for i in range(diana):
    line=input().split(" ")
    dianaDi.add((int(line[0]),int(line[1]))) 
    parentx=find(int(line[0]),dianaParents)
    parenty=find(int(line[1]),dianaParents)
    union(parentx,parenty,dianaParents,sizeD)

count=0
ans=[]
# print(mochaDi,dianaDi)
# print("here ",mochaParents,dianaParents)
for i in range(len(mochaParents)):
    parentxMocha=find(i+1,mochaParents)
    parentxDiana=find(i+1,dianaParents)
    for j in range(i+1,len(mochaParents)):
        parentyMocha=find(j+1,mochaParents)
        parentyDiana=find(j+1,dianaParents)
        if parentxMocha!=parentyMocha and parentxDiana!=parentyDiana:
            if (i+1,j+1) not in dianaDi and (i+1,j+1) not in mochaDi and (j+1,i+1) not in mochaDi and (j+1,i+1) not in dianaDi:
                # print(i+1,j+1)
                # print(parentxMocha,parentyMocha)
                # print(mochaParents,dianaParents)
                union(parentxMocha,parentyMocha,mochaParents,sizeM)
                union(parentxDiana,parentyDiana,dianaParents,sizeD)
                # print(mochaParents,dianaParents)
                count+=1
                ans.append((i+1,j+1))
                

print(count)
for i in ans:
    print(i[0],i[1])
