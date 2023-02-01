n=eval(input())
di={}
for i in range(n):
    line=input().split(" ")
    if line[0] not in di:
        di[line[1]]=[line[0],line[1]]
    else:
        di[line[1]]=[di[line[0]][0],line[1]]
        di.pop(line[0])
    
print(len(di))
for i in di:
    print(di[i][0],di[i][1])