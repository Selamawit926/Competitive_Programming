n=input()
inp=n.split()
row=int(inp[0])
lst=[]
for i in range(row):
    col = input()
    cols=col.split()
    lst.append(cols)
color=False
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j]=="C" or lst[i][j]=="Y" or lst[i][j]=="M":
            print("#Color")
            color=True
            break
    if color:
        break
if not color:
    print("#Black&White")
