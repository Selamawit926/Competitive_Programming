def dfs(matrix,i,j,tot,maxi,visited):
    for i in range(i,len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==1 and (i,j) not in visited:
                # print(i,j)
                visited.add((i,j))
                current=tot
                tot+=1
                maxi=dfs(matrix,j,0,tot,maxi,visited)
                tot=current
                # print(i,j,tot)

        break

    maxi=max(tot,maxi)
    # print(maxi)

    return maxi


num=eval(input("Enter number of spiders: "))
# num=1
count=0
for i in range(num):
    lst=input("Enter number of bead and pairs: ").split()
    # lst=["5","1","2","2","3","3","4","3","5"]
    # lst=["7","3","4","1","2","2","4","4","6","2","7","6","5"]
    
    matrix=[]
    visited=set()

    if lst[0]=="3":
        count+=2
        continue

    if lst[0]=="2":
        count+=1
        continue

    for i in range(int(lst[0])):
        matrix.append([])
        for j in range(int(lst[0])):
            matrix[i].append(0)

    for i in range(1,len(lst),2):    
        matrix[int(lst[i])-1][int(lst[i+1])-1]=1

    count+=dfs(matrix,0,0,0,0,visited)
   

print(count)
    