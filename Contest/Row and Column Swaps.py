from collections import defaultdict
inp= input().split()
n=int(inp[0])
k=int(inp[1])
rows=defaultdict(int)
cols=defaultdict(int)
matrix=[]
for i in range(n):
    matrix.append([])
    nums=input().split()
    for j in nums:
        matrix[-1].append(int(j))
    rows[i]=i
    cols[i]=i
output=[]
for i in range(k):
    inp=input().split()
    if inp[0]=="A":
        row=int(inp[1])-1
        col=int(inp[2])-1

        output.append(matrix[rows[row]][cols[col]])
    elif inp[0]=="R":
        row1=int(inp[1])-1
        row2=int(inp[2])-1

        temp=rows[row1]
        rows[row1]=rows[row2]
        rows[row2]=temp
    else:
        col1=int(inp[1])-1
        col2=int(inp[2])-1
        temp=cols[col1]
        cols[col1]=cols[col2]
        cols[col2]=temp
        
for num in output:
    print(num)

    