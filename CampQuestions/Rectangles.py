n=input().split(" ")
lst=[]
for i in range(int(n[0])):
    lst.append(input().split(" "))

sets=int(n[0])*int(n[1])
# di={"0":[],"1":[]}
# for i in range(len(lst)):
#     di["0"].append([])
#     di["1"].append([])
#     for j in range(len(lst[i])):
#         di[lst[i][j]][-1].append(j)

for row in lst:
    for i in range(len(row)):
        for j in range(i+2,len(row),2):
            if row[j]==row[i]:
                sets+=1
            else:
                break

for i in range(len(lst)):
    for j in range(len(lst[i])):
        for k in range(i+2,len(lst),2):
            if lst[i][j]==lst[k][j]:
                print("here: ",(i,j)," ",(k,j))
                sets+=1
            else:
                break
print(sets)


